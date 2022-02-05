---
article_html: "<p>add generator meta tag</p>\n<hr />\n<h2 id=\"render-function\">render
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>render source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">render</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"p\">:</span> <span
  class=\"n\">Markata</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n    <span class=\"k\">for</span>
  <span class=\"n\">article</span> <span class=\"ow\">in</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">iter_articles</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;add ssg tag&quot;</span><span class=\"p\">):</span>\n        <span
  class=\"n\">soup</span> <span class=\"o\">=</span> <span class=\"n\">BeautifulSoup</span><span
  class=\"p\">(</span><span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">html</span><span class=\"p\">,</span> <span class=\"n\">features</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;lxml&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"n\">tag</span> <span class=\"o\">=</span> <span class=\"n\">soup</span><span
  class=\"o\">.</span><span class=\"n\">new_tag</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;meta&quot;</span><span class=\"p\">)</span>\n        <span class=\"n\">tag</span><span
  class=\"o\">.</span><span class=\"n\">attrs</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;content&quot;</span><span class=\"p\">]</span> <span class=\"o\">=</span>
  <span class=\"sa\">f</span><span class=\"s2\">&quot;markata </span><span class=\"si\">{</span><span
  class=\"n\">__version__</span><span class=\"si\">}</span><span class=\"s2\">&quot;</span>\n
  \       <span class=\"n\">tag</span><span class=\"o\">.</span><span class=\"n\">attrs</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;name&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"s2\">&quot;generator&quot;</span>\n        <span
  class=\"n\">soup</span><span class=\"o\">.</span><span class=\"n\">head</span><span
  class=\"o\">.</span><span class=\"n\">append</span><span class=\"p\">(</span><span
  class=\"n\">tag</span><span class=\"p\">)</span>\n        <span class=\"n\">article</span><span
  class=\"o\">.</span><span class=\"n\">soup</span> <span class=\"o\">=</span> <span
  class=\"n\">soup</span>\n        <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">html</span> <span class=\"o\">=</span> <span class=\"n\">soup</span><span
  class=\"o\">.</span><span class=\"n\">prettify</span><span class=\"p\">()</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for generator
long_description: ''
now: 2022-02-05 19:38:00.891434
path: generator.md
slug: markata/plugins/generator
status: published
title: generator.py
today: 2022-02-05
---

add generator meta tag


---

## render `function`

None

??? "render source"
    ``` python
    def render(markata: Markata) -> None:
        for article in markata.iter_articles("add ssg tag"):
            soup = BeautifulSoup(article.html, features="lxml")
            tag = soup.new_tag("meta")
            tag.attrs["content"] = f"markata {__version__}"
            tag.attrs["name"] = "generator"
            soup.head.append(tag)
            article.soup = soup
            article.html = soup.prettify()
    ```