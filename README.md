# Memex Blog

使用 Marmite 0.4.2 构建的静态博客，发布到 https://AkaCMD.github.io/blog。

## 目录

```text
content/
  posts/                 新文章
  old-posts/             从其他平台迁移的旧文章
    frontmatter.yaml     旧文章共用的 stream 设置
  pages/                 关于等独立页面
  media/                 文章图片，按文章分目录
    old-posts/           旧文章图片
  _*.md                  可选的首页、页脚等布局片段
scripts/check_site.py    本地链接、媒体及图标检查
templates/             自定义模板（其余使用 Marmite 默认模板）
marmite.yaml            网站配置
custom.css              自定义样式
favicon.ico             网站图标
site/                   构建结果，不提交到 Git
```

`custom.css` 和 `favicon.ico` 保留在项目根目录：Marmite 0.4.2 对这两个文件有专门的读取逻辑，避免复制静态文件到自身而产生空文件。其他样式、脚本、字体可放在 `static/`。

## 安装和预览

```sh
cargo install marmite --version 0.4.2 --locked
marmite . site --serve --watch --bind 127.0.0.1:8000 --url http://127.0.0.1:8000
```

打开 http://127.0.0.1:8000/。本地 URL 由命令行覆盖；正式发布地址保留在 `marmite.yaml` 中。

需要加快预览时，在命令末尾添加 `--skip-image-resize true`。

## 写作

创建新文章或页面：

```sh
marmite . --new "文章标题" -t "随笔"
marmite . --new "页面标题" -p
```

Marmite 会自动把新文章放到 `content/posts/`，独立页面放到 `content/pages/`。文章带 `date`，独立页面不带 `date`。常用标签为：游戏设计、游戏评论、开发日志、笔记、随笔、迁移。

旧文章放在 `content/old-posts/`，由该目录的 `frontmatter.yaml` 统一设置 `stream: old-posts`。文章本身保留发布日期、标签和原文来源。

文章中的本地图片仍使用站点相对地址，例如：

```markdown
![图片说明](media/old-posts/文章目录/example.png)
```

不要因源文件移入子目录而改成 `../../media/`：文章最终输出仍是站点根目录的 HTML 文件。

已有文件名参与 URL 生成。移动文件时保留文件名和文章流；重命名或修改 slug 前先确认旧 URL 并设置重定向。现有 `hello_blog` 的下划线是旧 URL 的一部分，保留以兼容已有链接。

## 构建与检查

```sh
marmite . site
python3 scripts/check_site.py site
```

检查脚本会检查生成 HTML 中的本地链接、媒体和图标，正确处理 `/blog/` 部署前缀及中文路径编码。外部链接不在此检查范围内。

## 发布

提交并推送修改后，在 GitHub Actions 手动运行 `GH Pages Deploy`。流程使用固定版本的 Marmite 构建，通过链接检查后发布到 GitHub Pages。

`site/` 是构建产物，不提交到 Git。已移除 Obsidian 本机设置，`.gitignore` 保留排除规则，防止再次误提交。`.agents/skills/` 保存 Marmite 的代理技能文档。
