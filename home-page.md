---
article_html: '<p>There are several ways to create your home/landing page, lets walk
  through

  them.</p>

  <h2 id="default-behavior">Default Behavior</h2>

  <p><em>feed</em></p>

  <p>By default if there is no index page, the <a href="/markata/plugins/feeds/">feed

  plugin</a> will make a home page for you that simply

  lists all the the articles by title.</p>

  <h2 id="indexmd">index.md</h2>

  <p><em>markdown</em></p>

  <p>You can also have an <code>index.md</code> in your pages directory, and it will
  become the

  <code>index.html</code> on at render time.  This is how <a href="https://markata.dev">markata.dev</a>

  achieves it''s own home page.</p>

  <h2 id="staticindexhtml">static/index.html</h2>

  <p><em>html</em></p>

  <p>If you want something more complicated (i.e. not easily done in markdown), you

  can simply just make an <code>index.html</code> in your <code>Markata().config[''assets_dir'']</code>

  and it will become your home page. </p>

  <div class="admonition note">

  <p class="admonition-title">Note</p>

  <p>your default <code>assets_dir</code> will be the static diretory in the root
  of your

  project.  You can change this by adding to your <code>markata.toml</code> settings

  file.</p>

  <div class="highlight"><pre><span></span><code><span class="k">[markata]</span><span
  class="w"></span>

  <span class="n">assets_dir</span><span class="w"> </span><span class="o">=</span><span
  class="w"> </span><span class="s">&quot;assets&quot;</span><span class="w"></span>

  </code></pre></div>

  </div>

  <p>This is how the homepage of <a href="https://waylonwalker.com">waylonwalker.com</a>
  is achieved.</p>'
content: ''
cover: ''
datetime: null
description: There are several ways to create your home/landing page, lets walk through
  them.
long_description: ''
now: 2022-02-05 19:38:00.891350
path: docs/home-page.md
slug: home-page
status: draft
tags: []
templateKey: ''
title: Creating your Home Page
today: 2022-02-05
---

There are several ways to create your home/landing page, lets walk through
them.

## Default Behavior
_feed_

By default if there is no index page, the [feed
plugin](/markata/plugins/feeds/) will make a home page for you that simply
lists all the the articles by title.

## index.md
_markdown_

You can also have an `index.md` in your pages directory, and it will become the
`index.html` on at render time.  This is how [markata.dev](https://markata.dev)
achieves it's own home page.

## static/index.html
_html_

If you want something more complicated (i.e. not easily done in markdown), you
can simply just make an `index.html` in your `Markata().config['assets_dir']`
and it will become your home page. 

!!! note
    your default `assets_dir` will be the static diretory in the root of your
    project.  You can change this by adding to your `markata.toml` settings
    file.

    ```toml
    [markata]
    assets_dir = "assets"
    ```

This is how the homepage of [waylonwalker.com](https://waylonwalker.com) is achieved.