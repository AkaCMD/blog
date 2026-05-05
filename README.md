# Memex Blog

Marmite static blog. Content in `content/`; output in `site/`.

## Serve Locally

Install Marmite:

```sh
cargo install marmite
```

Preview setup:

```sh
marmite . site
ln -sfn . site/blog
```

Serve:

```sh
python3 -m http.server 8000 --directory site
```

Open `http://localhost:8000/blog/`. Recreate `site/blog` if `site/` is deleted.

Optional live rebuild in another terminal:

```sh
marmite --watch . site
```

Build only:

```sh
marmite . site
```

Image resizing is enabled: regular images max 800px, banner images max 1200px
For faster local preview, skip image resizing:

```sh
marmite . site --skip-image-resize true
```

Check links:

```sh
lychee http://localhost:8000
lychee --verbose http://localhost:8000 --extensions html
lychee --verbose ./site --extensions html
```

## Deploy

GitHub Pages deploy via `.github/workflows/main.yaml`.

1. Commit and push blog changes.
2. Open GitHub repo Actions tab.
3. Run `GH Pages Deploy` workflow manually.
4. Workflow builds `site/` and deploys to GitHub Pages.

Published URL:

```txt
https://AkaCMD.github.io/blog
```

## Notes

- `site/` is generated and ignored.
- Config: `marmite.yaml`.
- Posts: `content/`.
