# Memex

A static blog built with Marmite 0.4.2: [Visit the blog](https://AkaCMD.github.io/blog/).

## Structure

- `content/posts/`: new posts
- `content/old-posts/`: imported posts with shared stream settings
- `content/pages/`: standalone pages
- `content/media/`: article images
- `templates/`: template overrides
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

## Build and deploy

```sh
marmite . site
python3 scripts/check_site.py site
```

Push changes, then manually run **GH Pages Deploy** in GitHub Actions. The workflow checks local links and assets before publishing.
