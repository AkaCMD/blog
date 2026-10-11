#!/usr/bin/env python3
"""检查 Marmite 输出中的本地链接、媒体和 favicon，无需第三方依赖。"""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if value and key in {"href", "src", "poster"}:
                self.urls.append(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", nargs="?", default="site", type=Path)
    args = parser.parse_args()
    root = args.site.resolve()
    config = json.loads((root / "marmite.json").read_text())["config"]
    base = urlsplit(config["url"])
    prefix = base.path.rstrip("/")
    errors = set()
    pages = sorted(root.glob("*.html"))
    if not pages:
        errors.add("没有生成 HTML 页面")
    for page in pages:
        links = Links()
        links.feed(page.read_text())
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
    if errors:
        for error in sorted(errors):
            print(error)
        raise SystemExit(f"检查失败：{len(errors)} 个问题")
    print(f"检查通过：{len(pages)} 个 HTML 页面的本地链接、媒体和 favicon。")


if __name__ == "__main__":
    main()
