---
article_html: "<p>Markata is a fully plugins all the way down static site generator
  for\nfolks who just want their site to get started quickly and build great\ncontent,
  with the ability to tinker with everything under the hood if\nthey want to.</p>\n<h2
  id=\"quickstart\">QuickStart</h2>\n<p>Markata is fully configurable through a <code>markata.toml</code>
  file, but the defaults\nallow to build your site right out of the box with nothing
  more than markdown.</p>\n<h3 id=\"create-some-content\">Create Some Content</h3>\n<div
  class=\"highlight\"><pre><span></span><code>mkdir pages\necho &#39;# My First Post&#39;
  &gt; first-post.md\necho &#39;# Hello World&#39; &gt; hello-world.md\n</code></pre></div>\n<h3
  id=\"build-your-site\">Build your site</h3>\n<div class=\"highlight\"><pre><span></span><code>pip
  install markata\nmarkata build\n\n<span class=\"c1\"># or if pipx is your thing</span>\npix
  run markata build\n</code></pre></div>\n<h3 id=\"frontmatter\">Frontmatter</h3>\n<p>You
  will likely want to set things like <code>title</code>, <code>date</code>, <code>description</code>,\n<code>status</code>,
  or <code>template</code> per post, this can all be done inside yaml frontmatter.</p>\n<div
  class=\"highlight\"><pre><span></span><code>---\ntemplateKey: blog-post\ntags: [&#39;python&#39;,]\ntitle:
  \ My Awesome Post\ndate: 2022-01-21T16:40:34\nstatus: draft\n\n---\n\nThis is my
  awesome post.\n</code></pre></div>\n<blockquote>\n<p>Frontmatter is not required,
  but definitely gives you more control over your site.</p>\n</blockquote>\n<h2 id=\"next-steps\">Next
  steps</h2>\n<ul>\n<li><a href=\"https://markata.dev/home-page/\">create your home
  page</a></li>\n</ul>\n<h2 id=\"source-code\">Source Code</h2>\n<p>If you have comments,
  questions, issues, or like it enough to give a ⭐\ncheck out\n<a href=\"https://github.com/WaylonWalker/markata\">waylonwalker/markata</a></p>\n<h2
  id=\"markata-docs\">Markata Docs</h2>\n<p>Not much is documented yet, lots of work
  to do on the docs.  Checkout\n<a href=\"https://markata.dev/markata/lifecycle/\">LifeCycle</a>
  to see what a more\nfinished one looks like.</p>\n<p>UPDATE - the \n<a href=\"https://markata.dev/markata/plugins/base_cli/\"><code>base_cli</code></a>
  is also up to\ndate and includes a lot of examples of how to use the markata cli.</p>\n<blockquote>\n<p><strong>Yes</strong>
  this library generates it's own docs</p>\n</blockquote>\n<ul>\n<li><a href=\"https://markata.dev/autodoc/\">All
  Modules</a></li>\n<li><a href=\"https://markata.dev/core_modules/\">Core Modules</a></li>\n<li><a
  href=\"https://markata.dev/plugins/\">Plugins</a></li>\n</ul>"
content: ''
cover: ''
datetime: null
description: Guide to get going with Markata
long_description: ''
now: 2022-02-05 19:38:00.891344
path: docs/index.md
slug: index
status: draft
tags: []
templateKey: ''
title: Getting Started with Markata
today: 2022-02-05
---

Markata is a fully plugins all the way down static site generator for
folks who just want their site to get started quickly and build great
content, with the ability to tinker with everything under the hood if
they want to.

## QuickStart

Markata is fully configurable through a `markata.toml` file, but the defaults
allow to build your site right out of the box with nothing more than markdown.

### Create Some Content

```
mkdir pages
echo '# My First Post' > first-post.md
echo '# Hello World' > hello-world.md
```

### Build your site

``` bash
pip install markata
markata build

# or if pipx is your thing
pix run markata build
```

### Frontmatter

You will likely want to set things like `title`, `date`, `description`,
`status`, or `template` per post, this can all be done inside yaml frontmatter.

``` markdown
---
templateKey: blog-post
tags: ['python',]
title:  My Awesome Post
date: 2022-01-21T16:40:34
status: draft

---

This is my awesome post.

```

> Frontmatter is not required, but definitely gives you more control over your site.

## Next steps

* [create your home page](https://markata.dev/home-page/)

## Source Code

If you have comments, questions, issues, or like it enough to give a ⭐
check out
[waylonwalker/markata](https://github.com/WaylonWalker/markata)

## Markata Docs

Not much is documented yet, lots of work to do on the docs.  Checkout
[LifeCycle](https://markata.dev/markata/lifecycle/) to see what a more
finished one looks like.

UPDATE - the 
[`base_cli`](https://markata.dev/markata/plugins/base_cli/) is also up to
date and includes a lot of examples of how to use the markata cli.

> **Yes** this library generates it's own docs

* [All Modules](https://markata.dev/autodoc/)
* [Core Modules](https://markata.dev/core_modules/)
* [Plugins](https://markata.dev/plugins/)