---
article_html: "<hr />\n<h2 id=\"render-function\">render <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>render
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">render</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">config</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">get_plugin_config</span><span class=\"p\">(</span><span
  class=\"vm\">__file__</span><span class=\"p\">)</span>\n    <span class=\"k\">with</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">cache</span>
  <span class=\"k\">as</span> <span class=\"n\">cache</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">for</span> <span class=\"n\">article</span> <span class=\"ow\">in</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">iter_articles</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;setting long description&quot;</span><span
  class=\"p\">):</span>\n\n            <span class=\"n\">key</span> <span class=\"o\">=</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">make_hash</span><span
  class=\"p\">(</span>\n                <span class=\"s2\">&quot;long_description&quot;</span><span
  class=\"p\">,</span>\n                <span class=\"s2\">&quot;render&quot;</span><span
  class=\"p\">,</span>\n                <span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"vm\">__file__</span><span class=\"p\">)</span><span class=\"o\">.</span><span
  class=\"n\">read_text</span><span class=\"p\">(),</span>\n                <span
  class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">content</span><span
  class=\"p\">,</span>\n                <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">html</span><span class=\"p\">,</span>\n            <span class=\"p\">)</span>\n\n
  \           <span class=\"n\">description_from_cache</span> <span class=\"o\">=</span>
  <span class=\"n\">cache</span><span class=\"o\">.</span><span class=\"n\">get</span><span
  class=\"p\">(</span><span class=\"n\">key</span><span class=\"p\">)</span>\n\n            <span
  class=\"k\">if</span> <span class=\"n\">description_from_cache</span> <span class=\"ow\">is</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n\n                <span
  class=\"k\">if</span> <span class=\"s2\">&quot;long_description&quot;</span> <span
  class=\"ow\">in</span> <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">:</span>\n                    <span
  class=\"n\">description</span> <span class=\"o\">=</span> <span class=\"n\">article</span><span
  class=\"o\">.</span><span class=\"n\">metadata</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;long_description&quot;</span><span class=\"p\">]</span>\n\n                <span
  class=\"k\">else</span><span class=\"p\">:</span>\n                    <span class=\"k\">try</span><span
  class=\"p\">:</span>\n                        <span class=\"n\">soup</span> <span
  class=\"o\">=</span> <span class=\"n\">BeautifulSoup</span><span class=\"p\">(</span><span
  class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">html</span><span
  class=\"p\">,</span> <span class=\"n\">features</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;lxml&quot;</span><span class=\"p\">)</span>\n                        <span
  class=\"n\">description</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;
  &quot;</span><span class=\"o\">.</span><span class=\"n\">join</span><span class=\"p\">(</span>\n
  \                           <span class=\"p\">[</span><span class=\"n\">p</span><span
  class=\"o\">.</span><span class=\"n\">text</span> <span class=\"k\">for</span> <span
  class=\"n\">p</span> <span class=\"ow\">in</span> <span class=\"n\">soup</span><span
  class=\"o\">.</span><span class=\"n\">find</span><span class=\"p\">(</span><span
  class=\"nb\">id</span><span class=\"o\">=</span><span class=\"s2\">&quot;post-body&quot;</span><span
  class=\"p\">)</span><span class=\"o\">.</span><span class=\"n\">find_all</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;p&quot;</span><span class=\"p\">)]</span>\n
  \                       <span class=\"p\">)</span><span class=\"o\">.</span><span
  class=\"n\">strip</span><span class=\"p\">()[:</span><span class=\"mi\">250</span><span
  class=\"p\">]</span>\n                    <span class=\"k\">except</span> <span
  class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n                        <span
  class=\"n\">description</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;&quot;</span>\n\n
  \               <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">cache</span><span class=\"o\">.</span><span class=\"n\">add</span><span
  class=\"p\">(</span><span class=\"n\">key</span><span class=\"p\">,</span> <span
  class=\"n\">description</span><span class=\"p\">,</span> <span class=\"n\">expire</span><span
  class=\"o\">=</span><span class=\"n\">config</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;cache_expire&quot;</span><span class=\"p\">])</span>\n\n            <span
  class=\"k\">else</span><span class=\"p\">:</span>\n                <span class=\"n\">description</span>
  <span class=\"o\">=</span> <span class=\"n\">description_from_cache</span>\n\n            <span
  class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">metadata</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;long_description&quot;</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"n\">description</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for long_description
long_description: ''
now: 2022-02-05 19:38:00.891407
path: long_description.md
slug: markata/plugins/long_description
status: published
title: long_description.py
today: 2022-02-05
---

---

## render `function`

None

??? "render source"
    ``` python
    def render(markata: "Markata") -> None:
        config = markata.get_plugin_config(__file__)
        with markata.cache as cache:
            for article in markata.iter_articles("setting long description"):

                key = markata.make_hash(
                    "long_description",
                    "render",
                    Path(__file__).read_text(),
                    article.content,
                    article.html,
                )

                description_from_cache = cache.get(key)

                if description_from_cache is None:

                    if "long_description" in article.metadata:
                        description = article.metadata["long_description"]

                    else:
                        try:
                            soup = BeautifulSoup(article.html, features="lxml")
                            description = " ".join(
                                [p.text for p in soup.find(id="post-body").find_all("p")]
                            ).strip()[:250]
                        except AttributeError:
                            description = ""

                    markata.cache.add(key, description, expire=config["cache_expire"])

                else:
                    description = description_from_cache

                article.metadata["long_description"] = description
    ```