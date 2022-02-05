---
article_html: "<hr />\n<h2 id=\"pre_render-function\">pre_render <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>pre_render
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">pre_render</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n    <span class=\"k\">for</span> <span class=\"n\">article</span>
  <span class=\"ow\">in</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">filter</span><span class=\"p\">(</span><span class=\"s1\">&#39;title==&quot;&quot;&#39;</span><span
  class=\"p\">):</span>\n        <span class=\"n\">article</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;title&quot;</span><span class=\"p\">]</span> <span class=\"o\">=</span>
  <span class=\"p\">(</span>\n            <span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"n\">article</span><span class=\"p\">[</span><span class=\"s2\">&quot;path&quot;</span><span
  class=\"p\">])</span><span class=\"o\">.</span><span class=\"n\">stem</span><span
  class=\"o\">.</span><span class=\"n\">replace</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;-&quot;</span><span class=\"p\">,</span> <span class=\"s2\">&quot;
  &quot;</span><span class=\"p\">)</span><span class=\"o\">.</span><span class=\"n\">replace</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;_&quot;</span><span class=\"p\">,</span>
  <span class=\"s2\">&quot; &quot;</span><span class=\"p\">)</span><span class=\"o\">.</span><span
  class=\"n\">title</span><span class=\"p\">()</span>\n        <span class=\"p\">)</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for auto_title
long_description: ''
now: 2022-02-05 19:38:00.891379
path: auto_title.md
slug: markata/plugins/auto_title
status: published
title: auto_title.py
today: 2022-02-05
---

---

## pre_render `function`

None

??? "pre_render source"
    ``` python
    def pre_render(markata) -> None:
        for article in markata.filter('title==""'):
            article["title"] = (
                Path(article["path"]).stem.replace("-", " ").replace("_", " ").title()
            )
    ```