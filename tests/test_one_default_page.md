---
article_html: "<hr />\n<h2 id=\"make_index-function\">make_index <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>make_index
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">make_index</span><span class=\"p\">(</span><span class=\"n\">tmp_path_factory</span><span
  class=\"p\">:</span> <span class=\"n\">Any</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">fn</span> <span class=\"o\">=</span> <span class=\"n\">tmp_path_factory</span><span
  class=\"o\">.</span><span class=\"n\">mktemp</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;pages&quot;</span><span class=\"p\">)</span> <span class=\"o\">/</span>
  <span class=\"s2\">&quot;index.md&quot;</span>\n    <span class=\"n\">fn</span><span
  class=\"o\">.</span><span class=\"n\">write_text</span><span class=\"p\">(</span>\n
  \       <span class=\"n\">textwrap</span><span class=\"o\">.</span><span class=\"n\">dedent</span><span
  class=\"p\">(</span>\n            <span class=\"sd\">&quot;&quot;&quot;</span>\n<span
  class=\"sd\">            ---</span>\n<span class=\"sd\">            templateKey:
  blog-post</span>\n<span class=\"sd\">            tags: [&#39;python&#39;,]</span>\n<span
  class=\"sd\">            title:  My Awesome Post</span>\n<span class=\"sd\">            date:
  2022-01-21T16:40:34</span>\n<span class=\"sd\">            status: draft</span>\n\n<span
  class=\"sd\">            ---</span>\n\n<span class=\"sd\">            This is my
  awesome post.</span>\n<span class=\"sd\">            &quot;&quot;&quot;</span>\n
  \       <span class=\"p\">)</span>\n    <span class=\"p\">)</span>\n    <span class=\"k\">return</span>
  <span class=\"n\">tmp_path_factory</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"test_loaded-function\">test_loaded <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>test_loaded
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">test_loaded</span><span class=\"p\">(</span><span class=\"n\">make_index</span><span
  class=\"p\">:</span> <span class=\"n\">Any</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">os</span><span class=\"o\">.</span><span class=\"n\">chdir</span><span
  class=\"p\">(</span><span class=\"n\">make_index</span><span class=\"o\">.</span><span
  class=\"n\">getbasetemp</span><span class=\"p\">())</span>\n    <span class=\"n\">m</span>
  <span class=\"o\">=</span> <span class=\"n\">Markata</span><span class=\"p\">()</span>\n
  \   <span class=\"k\">assert</span> <span class=\"nb\">len</span><span class=\"p\">(</span><span
  class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">articles</span><span
  class=\"p\">)</span> <span class=\"o\">==</span> <span class=\"mi\">1</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"test_run-function\">test_run <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>test_run
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">test_run</span><span class=\"p\">(</span><span class=\"n\">make_index</span><span
  class=\"p\">:</span> <span class=\"n\">Any</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">os</span><span class=\"o\">.</span><span class=\"n\">chdir</span><span
  class=\"p\">(</span><span class=\"n\">make_index</span><span class=\"o\">.</span><span
  class=\"n\">getbasetemp</span><span class=\"p\">())</span>\n    <span class=\"n\">m</span>
  <span class=\"o\">=</span> <span class=\"n\">Markata</span><span class=\"p\">()</span>\n
  \   <span class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">run</span><span
  class=\"p\">()</span>\n    <span class=\"k\">return</span> <span class=\"n\">make_index</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"test_markout_exists-function\">test_markout_exists <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>test_markout_exists
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">test_markout_exists</span><span class=\"p\">(</span><span class=\"n\">test_run</span><span
  class=\"p\">:</span> <span class=\"n\">Any</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">markout</span> <span class=\"o\">=</span> <span class=\"n\">test_run</span><span
  class=\"o\">.</span><span class=\"n\">getbasetemp</span><span class=\"p\">()</span>
  <span class=\"o\">/</span> <span class=\"s2\">&quot;markout&quot;</span>\n    <span
  class=\"k\">assert</span> <span class=\"n\">markout</span><span class=\"o\">.</span><span
  class=\"n\">exists</span><span class=\"p\">()</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"test_index_exists-function\">test_index_exists <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>test_index_exists
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">test_index_exists</span><span class=\"p\">(</span><span class=\"n\">test_run</span><span
  class=\"p\">:</span> <span class=\"n\">Any</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">markout</span> <span class=\"o\">=</span> <span class=\"n\">test_run</span><span
  class=\"o\">.</span><span class=\"n\">getbasetemp</span><span class=\"p\">()</span>
  <span class=\"o\">/</span> <span class=\"s2\">&quot;markout&quot;</span>\n    <span
  class=\"n\">index</span> <span class=\"o\">=</span> <span class=\"n\">markout</span>
  <span class=\"o\">/</span> <span class=\"s2\">&quot;index.html&quot;</span>\n    <span
  class=\"k\">assert</span> <span class=\"n\">index</span><span class=\"o\">.</span><span
  class=\"n\">exists</span><span class=\"p\">()</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"test_rss_exists-function\">test_rss_exists <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>test_rss_exists
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">test_rss_exists</span><span class=\"p\">(</span><span class=\"n\">test_run</span><span
  class=\"p\">:</span> <span class=\"n\">Any</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">markout</span> <span class=\"o\">=</span> <span class=\"n\">test_run</span><span
  class=\"o\">.</span><span class=\"n\">getbasetemp</span><span class=\"p\">()</span>
  <span class=\"o\">/</span> <span class=\"s2\">&quot;markout&quot;</span>\n    <span
  class=\"n\">rss</span> <span class=\"o\">=</span> <span class=\"n\">markout</span>
  <span class=\"o\">/</span> <span class=\"s2\">&quot;rss.xml&quot;</span>\n    <span
  class=\"k\">assert</span> <span class=\"n\">rss</span><span class=\"o\">.</span><span
  class=\"n\">exists</span><span class=\"p\">()</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for test_one_default_page
long_description: ''
now: 2022-02-05 19:38:00.891354
path: test_one_default_page.md
slug: tests/test_one_default_page
status: published
title: test_one_default_page.py
today: 2022-02-05
---

---

## make_index `function`

None

??? "make_index source"
    ``` python
    def make_index(tmp_path_factory: Any) -> Any:
        fn = tmp_path_factory.mktemp("pages") / "index.md"
        fn.write_text(
            textwrap.dedent(
                """
                ---
                templateKey: blog-post
                tags: ['python',]
                title:  My Awesome Post
                date: 2022-01-21T16:40:34
                status: draft

                ---

                This is my awesome post.
                """
            )
        )
        return tmp_path_factory
    ```


---

## test_loaded `function`

None

??? "test_loaded source"
    ``` python
    def test_loaded(make_index: Any) -> None:
        os.chdir(make_index.getbasetemp())
        m = Markata()
        assert len(m.articles) == 1
    ```


---

## test_run `function`

None

??? "test_run source"
    ``` python
    def test_run(make_index: Any) -> Any:
        os.chdir(make_index.getbasetemp())
        m = Markata()
        m.run()
        return make_index
    ```


---

## test_markout_exists `function`

None

??? "test_markout_exists source"
    ``` python
    def test_markout_exists(test_run: Any) -> Any:
        markout = test_run.getbasetemp() / "markout"
        assert markout.exists()
    ```


---

## test_index_exists `function`

None

??? "test_index_exists source"
    ``` python
    def test_index_exists(test_run: Any) -> Any:
        markout = test_run.getbasetemp() / "markout"
        index = markout / "index.html"
        assert index.exists()
    ```


---

## test_rss_exists `function`

None

??? "test_rss_exists source"
    ``` python
    def test_rss_exists(test_run: Any) -> Any:
        markout = test_run.getbasetemp() / "markout"
        rss = markout / "rss.xml"
        assert rss.exists()
    ```