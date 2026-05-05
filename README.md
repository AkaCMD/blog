# Memex Blog

Marmite-powered static blog. Source content lives in `content/`; generated site goes to `site/`.

## Serve Locally

Install Marmite if needed:

```sh
cargo install marmite
```

Build and serve with live rebuild:

```sh
marmite --watch --serve --url http://localhost:8000 . site
```

Open `http://localhost:8000`.

One-time build only:

```sh
marmite . site
```

Run link checker, if installed:

```sh
# Basic link checking
lychee http://localhost:8000

# More verbose output with HTML file checking
lychee --verbose http://localhost:8000 --extensions html

# Check the built files directly (offline mode)
lychee --verbose ./site --extensions html
```

## Deploy

Deployment uses GitHub Pages via `.github/workflows/main.yaml`.

1. Commit and push blog changes.
2. Open GitHub repo Actions tab.
3. Run `GH Pages Deploy` workflow manually.
4. Workflow installs Marmite, builds with `marmite . site`, uploads `site/`, then deploys to GitHub Pages.

Published URL comes from `marmite.yaml`:

```txt
https://AkaCMD.github.io/blog
```

## Notes

- `site/` is generated output and ignored by git.
- Edit site config in `marmite.yaml`.
- Local serve needs `--url http://localhost:8000`; otherwise `url: https://AkaCMD.github.io/blog` makes CSS paths start with `/blog/`.
- Add or update posts under `content/`.
