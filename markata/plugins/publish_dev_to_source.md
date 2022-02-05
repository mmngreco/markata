---
article_html: "<hr />\n<h2 id=\"should_join-function\">should_join <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>should_join
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">should_join</span><span class=\"p\">(</span><span class=\"n\">line</span><span
  class=\"p\">):</span>\n    <span class=\"k\">if</span> <span class=\"n\">line</span>
  <span class=\"o\">==</span> <span class=\"s2\">&quot;&quot;</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">return</span> <span class=\"kc\">False</span>\n    <span
  class=\"k\">if</span> <span class=\"n\">line</span> <span class=\"ow\">is</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n        <span class=\"k\">return</span>
  <span class=\"kc\">False</span>\n    <span class=\"k\">if</span> <span class=\"n\">line</span><span
  class=\"p\">[</span><span class=\"mi\">0</span><span class=\"p\">]</span><span class=\"o\">.</span><span
  class=\"n\">isalpha</span><span class=\"p\">():</span>\n        <span class=\"k\">return</span>
  <span class=\"kc\">True</span>\n    <span class=\"k\">if</span> <span class=\"n\">line</span><span
  class=\"p\">[</span><span class=\"mi\">0</span><span class=\"p\">]</span><span class=\"o\">.</span><span
  class=\"n\">startswith</span><span class=\"p\">(</span><span class=\"s2\">&quot;[&quot;</span><span
  class=\"p\">):</span>\n        <span class=\"k\">return</span> <span class=\"kc\">True</span>\n
  \   <span class=\"k\">if</span> <span class=\"n\">line</span><span class=\"p\">[</span><span
  class=\"mi\">0</span><span class=\"p\">]</span><span class=\"o\">.</span><span class=\"n\">startswith</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;!&quot;</span><span class=\"p\">):</span>\n
  \       <span class=\"k\">return</span> <span class=\"kc\">True</span>\n    <span
  class=\"k\">return</span> <span class=\"kc\">False</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"join_lines-function\">join_lines <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>join_lines
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">join_lines</span><span class=\"p\">(</span><span class=\"n\">article</span><span
  class=\"p\">):</span>\n    <span class=\"n\">lines</span> <span class=\"o\">=</span>
  <span class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">split</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;</span><span class=\"se\">\\n</span><span
  class=\"s2\">&quot;</span><span class=\"p\">)</span>\n    <span class=\"n\">line_number</span>
  <span class=\"o\">=</span> <span class=\"mi\">0</span>\n    <span class=\"k\">while</span>
  <span class=\"n\">line_number</span> <span class=\"o\">+</span> <span class=\"mi\">1</span>
  <span class=\"o\">&lt;</span> <span class=\"nb\">len</span><span class=\"p\">(</span><span
  class=\"n\">lines</span><span class=\"p\">):</span>\n        <span class=\"n\">line</span>
  <span class=\"o\">=</span> <span class=\"n\">lines</span><span class=\"p\">[</span><span
  class=\"n\">line_number</span><span class=\"p\">]</span>\n        <span class=\"n\">nextline</span>
  <span class=\"o\">=</span> <span class=\"n\">lines</span><span class=\"p\">[</span><span
  class=\"n\">line_number</span> <span class=\"o\">+</span> <span class=\"mi\">1</span><span
  class=\"p\">]</span>\n        <span class=\"k\">if</span> <span class=\"n\">should_join</span><span
  class=\"p\">(</span><span class=\"n\">line</span><span class=\"p\">)</span> <span
  class=\"ow\">and</span> <span class=\"n\">should_join</span><span class=\"p\">(</span><span
  class=\"n\">nextline</span><span class=\"p\">):</span>\n            <span class=\"n\">lines</span><span
  class=\"p\">[</span><span class=\"n\">line_number</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"sa\">f</span><span class=\"s2\">&quot;</span><span
  class=\"si\">{</span><span class=\"n\">line</span><span class=\"si\">}</span><span
  class=\"s2\"> </span><span class=\"si\">{</span><span class=\"n\">nextline</span><span
  class=\"si\">}</span><span class=\"s2\">&quot;</span>\n            <span class=\"n\">lines</span><span
  class=\"o\">.</span><span class=\"n\">pop</span><span class=\"p\">(</span><span
  class=\"n\">line_number</span> <span class=\"o\">+</span> <span class=\"mi\">1</span><span
  class=\"p\">)</span>\n        <span class=\"k\">else</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">line_number</span> <span class=\"o\">+=</span> <span
  class=\"mi\">1</span>\n\n    <span class=\"k\">return</span> <span class=\"s2\">&quot;</span><span
  class=\"se\">\\n</span><span class=\"s2\">&quot;</span><span class=\"o\">.</span><span
  class=\"n\">join</span><span class=\"p\">(</span><span class=\"n\">lines</span><span
  class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"post_render-function\">post_render
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>post_render source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">post_render</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"p\">:</span> <span
  class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n    <span class=\"k\">for</span>
  <span class=\"n\">post</span> <span class=\"ow\">in</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">iter_articles</span><span class=\"p\">(</span><span
  class=\"n\">description</span><span class=\"o\">=</span><span class=\"s2\">&quot;saving
  source documents&quot;</span><span class=\"p\">):</span>\n        <span class=\"kn\">from</span>
  <span class=\"nn\">copy</span> <span class=\"kn\">import</span> <span class=\"n\">copy</span><span
  class=\"p\">,</span> <span class=\"n\">deepcopy</span>\n\n        <span class=\"n\">article</span>
  <span class=\"o\">=</span> <span class=\"n\">deepcopy</span><span class=\"p\">(</span><span
  class=\"n\">post</span><span class=\"p\">)</span>\n\n        <span class=\"n\">before_keys</span>
  <span class=\"o\">=</span> <span class=\"n\">copy</span><span class=\"p\">(</span><span
  class=\"nb\">list</span><span class=\"p\">(</span><span class=\"n\">article</span><span
  class=\"o\">.</span><span class=\"n\">keys</span><span class=\"p\">()))</span>\n
  \       <span class=\"k\">for</span> <span class=\"n\">key</span> <span class=\"ow\">in</span>
  <span class=\"n\">before_keys</span><span class=\"p\">:</span>\n            <span
  class=\"k\">if</span> <span class=\"n\">key</span> <span class=\"ow\">not</span>
  <span class=\"ow\">in</span> <span class=\"n\">DEV_TO_FRONTMATTER</span><span class=\"p\">:</span>\n
  \               <span class=\"k\">del</span> <span class=\"n\">article</span><span
  class=\"p\">[</span><span class=\"n\">key</span><span class=\"p\">]</span>\n\n        <span
  class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">content</span>
  <span class=\"o\">=</span> <span class=\"n\">join_lines</span><span class=\"p\">(</span><span
  class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">content</span><span
  class=\"p\">)</span>\n        <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">content</span> <span class=\"o\">=</span> <span class=\"n\">join_lines</span><span
  class=\"p\">(</span><span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">content</span><span class=\"p\">)</span>\n\n        <span class=\"k\">if</span>
  <span class=\"s2\">&quot;canonical_url&quot;</span> <span class=\"ow\">not</span>
  <span class=\"ow\">in</span> <span class=\"n\">article</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">article</span><span class=\"p\">[</span><span class=\"s2\">&quot;canonical_url&quot;</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"sa\">f</span><span
  class=\"s1\">&#39;</span><span class=\"si\">{</span><span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;url&quot;</span><span class=\"p\">]</span><span class=\"si\">}</span><span
  class=\"s1\">/</span><span class=\"si\">{</span><span class=\"n\">post</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;slug&quot;</span><span class=\"p\">]</span><span
  class=\"si\">}</span><span class=\"s1\">/&#39;</span>\n\n        <span class=\"k\">if</span>
  <span class=\"s2\">&quot;published&quot;</span> <span class=\"ow\">not</span> <span
  class=\"ow\">in</span> <span class=\"n\">article</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">article</span><span class=\"p\">[</span><span class=\"s2\">&quot;published&quot;</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"kc\">True</span>\n\n
  \       <span class=\"k\">if</span> <span class=\"s2\">&quot;cover_image&quot;</span>
  <span class=\"ow\">not</span> <span class=\"ow\">in</span> <span class=\"n\">article</span><span
  class=\"p\">:</span>\n            <span class=\"n\">article</span><span class=\"p\">[</span>\n
  \               <span class=\"s2\">&quot;cover_image&quot;</span>\n            <span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"sa\">f</span><span
  class=\"s2\">&quot;</span><span class=\"si\">{</span><span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">[</span><span
  class=\"s1\">&#39;images_url&#39;</span><span class=\"p\">]</span><span class=\"si\">}</span><span
  class=\"s2\">/</span><span class=\"si\">{</span><span class=\"n\">post</span><span
  class=\"p\">[</span><span class=\"s1\">&#39;slug&#39;</span><span class=\"p\">]</span><span
  class=\"si\">}</span><span class=\"s2\">.png&quot;</span>\n        <span class=\"n\">post</span><span
  class=\"o\">.</span><span class=\"n\">dev_to</span> <span class=\"o\">=</span> <span
  class=\"n\">article</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"save-function\">save
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>save source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">save</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"p\">:</span> <span
  class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n    <span class=\"n\">output_dir</span>
  <span class=\"o\">=</span> <span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"nb\">str</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;output_dir&quot;</span><span class=\"p\">]))</span>\n    <span
  class=\"n\">output_dir</span><span class=\"o\">.</span><span class=\"n\">mkdir</span><span
  class=\"p\">(</span><span class=\"n\">parents</span><span class=\"o\">=</span><span
  class=\"kc\">True</span><span class=\"p\">,</span> <span class=\"n\">exist_ok</span><span
  class=\"o\">=</span><span class=\"kc\">True</span><span class=\"p\">)</span>\n    <span
  class=\"k\">for</span> <span class=\"n\">post</span> <span class=\"ow\">in</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">iter_articles</span><span
  class=\"p\">(</span><span class=\"n\">description</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;saving source documents&quot;</span><span class=\"p\">):</span>\n\n
  \       <span class=\"k\">with</span> <span class=\"nb\">open</span><span class=\"p\">(</span><span
  class=\"n\">output_dir</span> <span class=\"o\">/</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">post</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;slug&quot;</span><span class=\"p\">])</span> <span class=\"o\">/</span>
  <span class=\"s2\">&quot;dev.md&quot;</span><span class=\"p\">,</span> <span class=\"s2\">&quot;w+&quot;</span><span
  class=\"p\">)</span> <span class=\"k\">as</span> <span class=\"n\">f</span><span
  class=\"p\">:</span>\n            <span class=\"n\">f</span><span class=\"o\">.</span><span
  class=\"n\">write</span><span class=\"p\">(</span><span class=\"n\">frontmatter</span><span
  class=\"o\">.</span><span class=\"n\">dumps</span><span class=\"p\">(</span><span
  class=\"n\">post</span><span class=\"o\">.</span><span class=\"n\">dev_to</span><span
  class=\"p\">))</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for publish_dev_to_source
long_description: ''
now: 2022-02-05 19:38:00.891450
path: publish_dev_to_source.md
slug: markata/plugins/publish_dev_to_source
status: published
title: publish_dev_to_source.py
today: 2022-02-05
---

---

## should_join `function`

None

??? "should_join source"
    ``` python
    def should_join(line):
        if line == "":
            return False
        if line is None:
            return False
        if line[0].isalpha():
            return True
        if line[0].startswith("["):
            return True
        if line[0].startswith("!"):
            return True
        return False
    ```


---

## join_lines `function`

None

??? "join_lines source"
    ``` python
    def join_lines(article):
        lines = article.split("\n")
        line_number = 0
        while line_number + 1 < len(lines):
            line = lines[line_number]
            nextline = lines[line_number + 1]
            if should_join(line) and should_join(nextline):
                lines[line_number] = f"{line} {nextline}"
                lines.pop(line_number + 1)
            else:
                line_number += 1

        return "\n".join(lines)
    ```


---

## post_render `function`

None

??? "post_render source"
    ``` python
    def post_render(markata: "Markata") -> None:
        for post in markata.iter_articles(description="saving source documents"):
            from copy import copy, deepcopy

            article = deepcopy(post)

            before_keys = copy(list(article.keys()))
            for key in before_keys:
                if key not in DEV_TO_FRONTMATTER:
                    del article[key]

            article.content = join_lines(article.content)
            article.content = join_lines(article.content)

            if "canonical_url" not in article:
                article["canonical_url"] = f'{markata.config["url"]}/{post["slug"]}/'

            if "published" not in article:
                article["published"] = True

            if "cover_image" not in article:
                article[
                    "cover_image"
                ] = f"{markata.config['images_url']}/{post['slug']}.png"
            post.dev_to = article
    ```


---

## save `function`

None

??? "save source"
    ``` python
    def save(markata: "Markata") -> None:
        output_dir = Path(str(markata.config["output_dir"]))
        output_dir.mkdir(parents=True, exist_ok=True)
        for post in markata.iter_articles(description="saving source documents"):

            with open(output_dir / Path(post["slug"]) / "dev.md", "w+") as f:
                f.write(frontmatter.dumps(post.dev_to))
    ```