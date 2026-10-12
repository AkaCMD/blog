# Memex

A static blog built with Marmite: [Visit the blog](https://AkaCMD.github.io/blog/).

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
rustup update stable --no-self-update
cargo +stable install marmite --version "$(python3 scripts/latest_marmite.py)" --locked --force
marmite . site --serve --watch --bind 127.0.0.1:8000 --url http://127.0.0.1:8000
```

Open [localhost](http://127.0.0.1:8000/).

## Write

```sh
marmite . --new "Post title" -t "随笔"
marmite . --new "Page title" -p
```

Keep existing filenames and streams to preserve URLs. Use site-relative image paths such as `media/example.png`.

## Friend links

The friend links menu entry points to `links.html`. Manage links in `extra.friend_links` in `marmite.yaml`; cards appear in the configured order:

```yaml
extra:
  friend_links:
    - name: A friend's blog
      url: https://example.com/
      description: A short introduction (optional)
```

Merge these entries into the existing `extra` configuration and use full `https://` or `http://` URLs. Keep `friend_links: []` when the list is empty.

The friend links page is defined in `content/pages/links.md`. The `<!-- .friend_links -->` shortcode renders cards that support light and dark themes and mobile screens. Rebuild the site after making changes.

## Build and deploy

```sh
marmite . site
python3 scripts/check_site.py site
```

Push changes, then manually run **GH Pages Deploy** in GitHub Actions. Deployment remains manual; pushing a commit does not publish the site.

Local installation and each deployment resolve the latest stable Marmite release from crates.io using `scripts/latest_marmite.py` and install it with locked dependencies. Run the installation command above before building locally to stay current. The build job caches the binary by version and checks rendered pages, local links and assets before uploading the site. Shortcode rendering errors fail validation. A separate deployment job publishes the validated artifact to the `github-pages` environment; only that job has publishing permissions.
