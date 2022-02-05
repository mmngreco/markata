---
article_html: "<p>Flat Slug Plugin</p>\n<p>Creates a slug in article.metadata if missing
  based on filename.</p>\n<hr />\n<h2 id=\"pre_render-function\">pre_render <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>pre_render
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">pre_render</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"k\">for</span> <span class=\"n\">article</span> <span class=\"ow\">in</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">iter_articles</span><span
  class=\"p\">(</span><span class=\"n\">description</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;creating slugs&quot;</span><span class=\"p\">):</span>\n        <span
  class=\"k\">try</span><span class=\"p\">:</span>\n            <span class=\"n\">article</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;slug&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">[</span><span class=\"s2\">&quot;slug&quot;</span><span
  class=\"p\">]</span>\n        <span class=\"k\">except</span> <span class=\"ne\">KeyError</span><span
  class=\"p\">:</span>\n            <span class=\"n\">article</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;slug&quot;</span><span class=\"p\">]</span> <span class=\"o\">=</span>
  <span class=\"n\">Path</span><span class=\"p\">(</span><span class=\"n\">article</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;path&quot;</span><span class=\"p\">])</span><span
  class=\"o\">.</span><span class=\"n\">stem</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for flat_slug
long_description: ''
now: 2022-02-05 19:38:00.891410
path: flat_slug.md
slug: markata/plugins/flat_slug
status: published
title: flat_slug.py
today: 2022-02-05
---

Flat Slug Plugin

Creates a slug in article.metadata if missing based on filename.


---

## pre_render `function`

None

??? "pre_render source"
    ``` python
    def pre_render(markata: "Markata") -> None:
        for article in markata.iter_articles(description="creating slugs"):
            try:
                article["slug"] = article.metadata["slug"]
            except KeyError:
                article["slug"] = Path(article["path"]).stem
    ```