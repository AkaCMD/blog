# Memex

A static blog built with Marmite 0.4.2: [Visit the blog](https://AkaCMD.github.io/blog/).

## Structure

- `content/posts/`: new posts
- `content/old-posts/`: imported posts with shared stream settings
- `content/pages/`: standalone pages
- `content/media/`: article images
- `templates/`: template overrides
- `shortcodes/`: reusable content blocks, including friend links
- `marmite.yaml`: site configuration
- `custom.css` and `favicon.ico`: site assets
- `site/`: generated output, ignored by Git

Local agent skills in `.agents/skills/` are also ignored.

## Preview

```sh
cargo install marmite --version 0.4.2 --locked
marmite . site --serve --watch --bind 127.0.0.1:8000 --url http://127.0.0.1:8000
```

Open [localhost](http://127.0.0.1:8000/).

## Write

```sh
marmite . --new "Post title" -t "随笔"
marmite . --new "Page title" -p
```

Keep existing filenames and streams to preserve URLs. Use site-relative image paths such as `media/example.png`.

## 友链

导航中的「友链」指向 `links.html`。在 `marmite.yaml` 的 `extra.friend_links` 中维护名单，按配置顺序展示：

```yaml
extra:
  friend_links:
    - name: 朋友的博客
      url: https://example.com/
      description: 一句话介绍这个站点（可省略）
```

将条目合并到已有的 `extra` 配置中，网址使用完整的 `https://` 或 `http://` 地址。没有友链时保留 `friend_links: []`。页面介绍和交换方式在 `content/pages/links.md` 中修改；`<!-- .friend_links -->` 会生成适配明暗主题和手机屏幕的友链卡片。修改后重新构建即可。

## Build and deploy

```sh
marmite . site
python3 scripts/check_site.py site
```

Push changes, then manually run **GH Pages Deploy** in GitHub Actions. The workflow checks local links and assets before publishing.
