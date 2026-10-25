#!/usr/bin/env python3
"""检查 Marmite 输出中的渲染错误、本地链接、源码链接、媒体和 favicon，无需第三方依赖。"""
import argparse
import json
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.shortcode_error = False
        self.feeds = []
        self.rss_buttons = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "link" and attributes.get("type") in {"application/rss+xml", "application/atom+xml", "application/feed+json"}:
            self.feeds.append(attributes.get("href"))
        if tag == "button" and "rss-copy-button" in attributes.get("class", "").split():
            self.rss_buttons.append(attributes)
        if "shortcode-error" in (dict(attrs).get("class") or "").split():
            self.shortcode_error = True
        for key, value in attrs:
            if value and key in {"href", "src", "poster"}:
                self.urls.append(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", nargs="?", default="site", type=Path)
    args = parser.parse_args()
    root = args.site.resolve()
    manifest = json.loads((root / "marmite.json").read_text())
    config = manifest["config"]
    base = urlsplit(config["url"])
    prefix = base.path.rstrip("/")
    errors = set()
    feed_url = config["url"].rstrip("/") + "/author-trioduckk.rss"
    pages = sorted(root.glob("*.html"))
    if not pages:
        errors.add("没有生成 HTML 页面")
    for page in pages:
        links = Links()
        links.feed(page.read_text())
        if links.feeds != [feed_url]:
            errors.add(f"{page.name}: 应只声明全站 RSS {feed_url}")
        if len(links.rss_buttons) != 1 or any(
            link.get("type") != "button"
            or link.get("title") != "Copy RSS feed URL"
            or link.get("aria-label") != "Copy RSS feed URL"
            for link in links.rss_buttons
        ):
            errors.add(f"{page.name}: RSS 应为带英文提示和无障碍名称的复制按钮")
        if links.shortcode_error:
            errors.add(f"{page.name}: Shortcode 渲染失败")
        for raw in links.urls:
            if raw.startswith("#"):
                continue
            current = config["url"].rstrip("/") + "/" + page.name
            url = urlsplit(urljoin(current, raw))
            if url.scheme not in {"http", "https"} or url.netloc != base.netloc:
                continue
            path = unquote(url.path)
            if prefix and path != prefix and not path.startswith(prefix + "/"):
                continue  # 同域的其他网站不属于本次构建。
            relative = path[len(prefix):].lstrip("/") if prefix else path.lstrip("/")
            target = root / relative
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                errors.add(f"{page.name}: {raw}")
    for relative in ("favicon.ico", "static/favicon.ico"):
        target = root / relative
        if not target.is_file() or target.stat().st_size == 0:
            errors.add(f"图标缺失或为空: {relative}")
    custom_script = root / "static/custom.js"
    if not custom_script.is_file() or any(
        marker not in custom_script.read_text()
        for marker in ("navigator.clipboard.writeText(rssFeed.href)", "rss-copy-status")
    ):
        errors.add("RSS 按钮缺少复制订阅链接的点击处理")
    repository = config.get("source_repository")
    if repository:
        project = Path(__file__).resolve().parent.parent
        for item in manifest["posts"] + manifest["pages"]:
            source = Path(item["source_path"])
            page = root / (item["slug"] + ".html")
            if not (project / source).is_file():
                errors.add(f"源码文件不存在: {source}")
            if not page.is_file():
                errors.add(f"内容页面不存在: {page.name}")
                continue
            links = Links()
            links.feed(page.read_text())
            expected = repository.rstrip("/") + "/" + source.as_posix()
            if expected not in {unquote(url) for url in links.urls}:
                errors.add(f"{page.name}: 源码链接缺失或路径错误，应为 {expected}")
    try:
        feed = ET.parse(root / "author-trioduckk.rss")
        items = feed.findall("./channel/item")
        posts = [p for p in manifest["posts"] if p.get("date") and p.get("stream") != "draft"]
        # Marmite's native RSS retains 15 items, prioritizing pinned posts.
        posts.sort(key=lambda p: (bool(p.get("pinned")), p["date"]), reverse=True)
        expected = {config["url"].rstrip("/") + "/" + p["slug"] + ".html" for p in posts[:15]}
        actual = [item.findtext("guid") for item in items]
        if set(actual) != expected or len(actual) != len(expected):
            errors.add("RSS 应覆盖跨栏目的最近 15 篇非草稿文章（置顶优先），且没有重复条目")
        dates = [parsedate_to_datetime(item.findtext("pubDate")) for item in items]
        if not any(p.get("pinned") for p in posts) and dates != sorted(dates, reverse=True):
            errors.add("RSS 文章应按发布时间倒序排列")
        for item in items:
            if not item.findtext("title") or not item.findtext("{http://purl.org/rss/1.0/modules/content/}encoded"):
                errors.add("RSS 文章缺少标题或全文")
    except (ET.ParseError, OSError, ValueError, TypeError) as error:
        errors.add(f"RSS 无法解析: {error}")
    if errors:
        for error in sorted(errors):
            print(error)
        raise SystemExit(f"检查失败：{len(errors)} 个问题")
    print(f"检查通过：{len(pages)} 个 HTML 页面的渲染、本地链接、源码链接、媒体和 favicon。")
    print(f"RSS 检查通过：唯一订阅地址、复制按钮、全文和 {len(items)} 篇文章。")


if __name__ == "__main__":
    main()
