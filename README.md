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
- [UI TODO](TODO.md): visual improvements and completion checklist

Local agent skills in `.agents/skills/` are also ignored.

## Preview

```sh
bash scripts/marmite.sh . site --serve --watch --bind 127.0.0.1:8000 --url http://127.0.0.1:8000
```

Open [localhost](http://127.0.0.1:8000/).

## Fonts

The site serves Libron and Source Han Serif locally from `content/media/fonts/`, including their licenses and source URLs in `sources.json`. Source Han Serif uses character subsets named Memex Han Serif. The subsets cover the source font's characters outside Libron's coverage, so new posts do not require rebuilding fonts. The Memex wordmark retains Atkinson Hyperlegible Next.

Normal site builds copy the prepared font assets. To regenerate them, install `fonttools` and `brotli` in a Python environment, then run `python3 scripts/prepare_fonts.py`. The script downloads pinned font sources; it requires network access.

## Write

```sh
bash scripts/marmite.sh . --new "Post title" -t "随笔"
bash scripts/marmite.sh . --new "Page title" -p
```

Keep existing filenames and streams to preserve URLs. Use site-relative image paths such as `media/example.png`.

## Friend links

The friend links menu entry points to `links.html`. Manage links in `extra.friend_links` in `marmite.yaml`; cards appear in the configured order:

```yaml
extra:
  friend_links:
    - name: A friend's blog
      url: https://example.com/
      avatar: media/friend-links/example.png
      description: A short introduction (optional)
```

Merge these entries into the existing `extra` configuration and use full `https://` or `http://` URLs. Keep `friend_links: []` when the list is empty.

Keep entries in alphabetical order by site name, using pinyin for Chinese names. Both `avatar` and `description` are optional. Store avatars or site icons in `content/media/friend-links/` and reference them with site-relative paths as shown above; full image URLs also work. Cards without an avatar display the first character of the site name.

The friend links page is defined in `content/pages/links.md`. The `<!-- .friend_links -->` shortcode renders cards that support light and dark themes and mobile screens. Rebuild the site after making changes.

## Build and deploy

```sh
bash scripts/build_site.sh
```

Push changes, then manually run **GH Pages Deploy** in GitHub Actions. Deployment remains manual; pushing a commit does not publish the site.

Requires Rust/Cargo and Python 3. The scripts install Marmite automatically when needed.

Builds check rendered pages, local links and assets before deployment. Shortcode rendering errors fail validation.

## Upgrade Marmite

Upgrade to the latest stable release and validate:

```sh
python3 scripts/latest_marmite.py --update
bash scripts/build_site.sh
```

Preview the site, then commit `.marmite-version` with any compatibility fixes.
