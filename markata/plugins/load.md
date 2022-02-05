---
article_html: "<p>Default load plugin.</p>\n<hr />\n<h2 id=\"load-function\">load
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>load source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">load</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"p\">:</span> <span
  class=\"s2\">&quot;MarkataMarkdown&quot;</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">progress</span> <span class=\"o\">=</span> <span class=\"n\">Progress</span><span
  class=\"p\">(</span>\n        <span class=\"n\">BarColumn</span><span class=\"p\">(</span><span
  class=\"n\">bar_width</span><span class=\"o\">=</span><span class=\"kc\">None</span><span
  class=\"p\">),</span> <span class=\"n\">transient</span><span class=\"o\">=</span><span
  class=\"kc\">True</span><span class=\"p\">,</span> <span class=\"n\">console</span><span
  class=\"o\">=</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">console</span>\n    <span class=\"p\">)</span>\n\n    <span class=\"n\">futures</span>
  <span class=\"o\">=</span> <span class=\"p\">[</span><span class=\"n\">get_post</span><span
  class=\"p\">(</span><span class=\"n\">article</span><span class=\"p\">,</span> <span
  class=\"n\">markata</span><span class=\"p\">)</span> <span class=\"k\">for</span>
  <span class=\"n\">article</span> <span class=\"ow\">in</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">files</span><span class=\"p\">]</span>\n    <span
  class=\"n\">task_id</span> <span class=\"o\">=</span> <span class=\"n\">progress</span><span
  class=\"o\">.</span><span class=\"n\">add_task</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;loading markdown&quot;</span><span class=\"p\">)</span>\n    <span
  class=\"n\">progress</span><span class=\"o\">.</span><span class=\"n\">update</span><span
  class=\"p\">(</span><span class=\"n\">task_id</span><span class=\"p\">,</span> <span
  class=\"n\">total</span><span class=\"o\">=</span><span class=\"nb\">len</span><span
  class=\"p\">(</span><span class=\"n\">futures</span><span class=\"p\">))</span>\n
  \   <span class=\"k\">with</span> <span class=\"n\">progress</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">while</span> <span class=\"ow\">not</span> <span class=\"nb\">all</span><span
  class=\"p\">([</span><span class=\"n\">f</span><span class=\"o\">.</span><span class=\"n\">done</span><span
  class=\"p\">()</span> <span class=\"k\">for</span> <span class=\"n\">f</span> <span
  class=\"ow\">in</span> <span class=\"n\">futures</span><span class=\"p\">]):</span>\n
  \           <span class=\"n\">time</span><span class=\"o\">.</span><span class=\"n\">sleep</span><span
  class=\"p\">(</span><span class=\"mf\">0.1</span><span class=\"p\">)</span>\n            <span
  class=\"n\">progress</span><span class=\"o\">.</span><span class=\"n\">update</span><span
  class=\"p\">(</span><span class=\"n\">task_id</span><span class=\"p\">,</span> <span
  class=\"n\">total</span><span class=\"o\">=</span><span class=\"nb\">len</span><span
  class=\"p\">([</span><span class=\"n\">f</span> <span class=\"k\">for</span> <span
  class=\"n\">f</span> <span class=\"ow\">in</span> <span class=\"n\">futures</span>
  <span class=\"k\">if</span> <span class=\"n\">f</span><span class=\"o\">.</span><span
  class=\"n\">done</span><span class=\"p\">()]))</span>\n    <span class=\"n\">articles</span>
  <span class=\"o\">=</span> <span class=\"p\">[</span><span class=\"n\">f</span><span
  class=\"o\">.</span><span class=\"n\">result</span><span class=\"p\">()</span> <span
  class=\"k\">for</span> <span class=\"n\">f</span> <span class=\"ow\">in</span> <span
  class=\"n\">futures</span><span class=\"p\">]</span>\n    <span class=\"n\">articles</span>
  <span class=\"o\">=</span> <span class=\"p\">[</span><span class=\"n\">a</span>
  <span class=\"k\">for</span> <span class=\"n\">a</span> <span class=\"ow\">in</span>
  <span class=\"n\">articles</span> <span class=\"k\">if</span> <span class=\"n\">a</span><span
  class=\"p\">]</span>\n    <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">articles</span> <span class=\"o\">=</span> <span class=\"n\">articles</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"get_post-function\">get_post <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>get_post
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">get_post</span><span class=\"p\">(</span><span class=\"n\">path</span><span
  class=\"p\">:</span> <span class=\"n\">Path</span><span class=\"p\">,</span> <span
  class=\"n\">markata</span><span class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Optional</span><span
  class=\"p\">[</span><span class=\"n\">Callable</span><span class=\"p\">]:</span>\n
  \   <span class=\"c1\"># -&gt; Optional[&quot;Post&quot;]:</span>\n    <span class=\"n\">default</span>
  <span class=\"o\">=</span> <span class=\"p\">{</span>\n        <span class=\"s2\">&quot;cover&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;&quot;</span><span class=\"p\">,</span>\n
  \       <span class=\"s2\">&quot;title&quot;</span><span class=\"p\">:</span> <span
  class=\"s2\">&quot;&quot;</span><span class=\"p\">,</span>\n        <span class=\"s2\">&quot;tags&quot;</span><span
  class=\"p\">:</span> <span class=\"p\">[],</span>\n        <span class=\"s2\">&quot;status&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;draft&quot;</span><span class=\"p\">,</span>\n
  \       <span class=\"s2\">&quot;templateKey&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;&quot;</span><span class=\"p\">,</span>\n        <span
  class=\"s2\">&quot;path&quot;</span><span class=\"p\">:</span> <span class=\"nb\">str</span><span
  class=\"p\">(</span><span class=\"n\">path</span><span class=\"p\">),</span>\n        <span
  class=\"s2\">&quot;description&quot;</span><span class=\"p\">:</span> <span class=\"s2\">&quot;&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"s2\">&quot;content&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;&quot;</span><span class=\"p\">,</span>\n
  \   <span class=\"p\">}</span>\n    <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \       <span class=\"n\">post</span><span class=\"p\">:</span> <span class=\"s2\">&quot;Post&quot;</span>
  <span class=\"o\">=</span> <span class=\"n\">frontmatter</span><span class=\"o\">.</span><span
  class=\"n\">load</span><span class=\"p\">(</span><span class=\"n\">path</span><span
  class=\"p\">)</span>\n        <span class=\"n\">post</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span> <span class=\"o\">=</span> <span class=\"p\">{</span><span
  class=\"o\">**</span><span class=\"n\">default</span><span class=\"p\">,</span>
  <span class=\"o\">**</span><span class=\"n\">post</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">}</span>\n    <span class=\"k\">except</span>
  <span class=\"n\">ParserError</span><span class=\"p\">:</span>\n        <span class=\"k\">return</span>
  <span class=\"kc\">None</span>\n        <span class=\"n\">post</span> <span class=\"o\">=</span>
  <span class=\"n\">default</span>\n    <span class=\"k\">except</span> <span class=\"ne\">ValueError</span><span
  class=\"p\">:</span>\n        <span class=\"k\">return</span> <span class=\"kc\">None</span>\n
  \       <span class=\"n\">post</span> <span class=\"o\">=</span> <span class=\"n\">default</span>\n
  \   <span class=\"n\">post</span><span class=\"o\">.</span><span class=\"n\">metadata</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;path&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"n\">path</span><span class=\"p\">)</span>\n    <span class=\"k\">return</span>
  <span class=\"n\">post</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"markatamarkdown-class\">MarkataMarkdown
  <code>class</code></h2>\n<p>None</p>\n<details>\n<summary>MarkataMarkdown source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span> <span
  class=\"nc\">MarkataMarkdown</span><span class=\"p\">(</span><span class=\"n\">Markata</span><span
  class=\"p\">):</span>\n        <span class=\"n\">articles</span><span class=\"p\">:</span>
  <span class=\"n\">List</span> <span class=\"o\">=</span> <span class=\"p\">[]</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for load
long_description: ''
now: 2022-02-05 19:38:00.891401
path: load.md
slug: markata/plugins/load
status: published
title: load.py
today: 2022-02-05
---

Default load plugin.


---

## load `function`

None

??? "load source"
    ``` python
    def load(markata: "MarkataMarkdown") -> None:
        progress = Progress(
            BarColumn(bar_width=None), transient=True, console=markata.console
        )

        futures = [get_post(article, markata) for article in markata.files]
        task_id = progress.add_task("loading markdown")
        progress.update(task_id, total=len(futures))
        with progress:
            while not all([f.done() for f in futures]):
                time.sleep(0.1)
                progress.update(task_id, total=len([f for f in futures if f.done()]))
        articles = [f.result() for f in futures]
        articles = [a for a in articles if a]
        markata.articles = articles
    ```


---

## get_post `function`

None

??? "get_post source"
    ``` python
    def get_post(path: Path, markata: "Markata") -> Optional[Callable]:
        # -> Optional["Post"]:
        default = {
            "cover": "",
            "title": "",
            "tags": [],
            "status": "draft",
            "templateKey": "",
            "path": str(path),
            "description": "",
            "content": "",
        }
        try:
            post: "Post" = frontmatter.load(path)
            post.metadata = {**default, **post.metadata}
        except ParserError:
            return None
            post = default
        except ValueError:
            return None
            post = default
        post.metadata["path"] = str(path)
        return post
    ```


---

## MarkataMarkdown `class`

None

??? "MarkataMarkdown source"
    ``` python
    class MarkataMarkdown(Markata):
            articles: List = []
    ```