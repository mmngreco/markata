---
article_html: "<hr />\n<h2 id=\"make_project-function\">make_project <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>make_project
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">make_project</span><span class=\"p\">(</span><span class=\"n\">tmp_path_factory</span><span
  class=\"p\">:</span> <span class=\"n\">Any</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">project</span> <span class=\"o\">=</span> <span class=\"n\">tmp_path_factory</span><span
  class=\"o\">.</span><span class=\"n\">mktemp</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;project&quot;</span><span class=\"p\">)</span>\n    <span class=\"n\">module</span>
  <span class=\"o\">=</span> <span class=\"n\">project</span> <span class=\"o\">/</span>
  <span class=\"s2\">&quot;my_module.py&quot;</span>\n    <span class=\"n\">module</span><span
  class=\"o\">.</span><span class=\"n\">write_text</span><span class=\"p\">(</span>\n
  \       <span class=\"n\">textwrap</span><span class=\"o\">.</span><span class=\"n\">dedent</span><span
  class=\"p\">(</span>\n            <span class=\"sd\">&quot;&quot;&quot;</span>\n<span
  class=\"sd\">            &#39;&#39;&#39;</span>\n<span class=\"sd\">            Module
  level docstring</span>\n<span class=\"sd\">            &#39;&#39;&#39;</span>\n\n<span
  class=\"sd\">            def my_func():</span>\n<span class=\"sd\">                &#39;&#39;&#39;</span>\n<span
  class=\"sd\">                docstring for my_func</span>\n<span class=\"sd\">                &#39;&#39;&#39;</span>\n<span
  class=\"sd\">            class MyClass:</span>\n<span class=\"sd\">                &#39;&#39;&#39;</span>\n<span
  class=\"sd\">                docstring for MyClass</span>\n<span class=\"sd\">                &#39;&#39;&#39;</span>\n\n<span
  class=\"sd\">                def my_method(self):</span>\n<span class=\"sd\">                    &#39;&#39;&#39;</span>\n<span
  class=\"sd\">                    docstring for my_method</span>\n<span class=\"sd\">
  \                   &#39;&#39;&#39;</span>\n\n<span class=\"sd\">            &quot;&quot;&quot;</span>\n
  \       <span class=\"p\">)</span>\n    <span class=\"p\">)</span>\n    <span class=\"n\">markta_toml</span>
  <span class=\"o\">=</span> <span class=\"n\">project</span> <span class=\"o\">/</span>
  <span class=\"s2\">&quot;markata.toml&quot;</span>\n    <span class=\"n\">markta_toml</span><span
  class=\"o\">.</span><span class=\"n\">write_text</span><span class=\"p\">(</span>\n
  \       <span class=\"n\">textwrap</span><span class=\"o\">.</span><span class=\"n\">dedent</span><span
  class=\"p\">(</span>\n            <span class=\"sd\">&quot;&quot;&quot;</span>\n<span
  class=\"sd\">            [markata]</span>\n<span class=\"sd\">            hooks
  = [</span>\n<span class=\"sd\">                &quot;markata.plugins.docs&quot;,</span>\n<span
  class=\"sd\">                &quot;default&quot;,</span>\n<span class=\"sd\">                ]</span>\n\n<span
  class=\"sd\">            &quot;&quot;&quot;</span>\n        <span class=\"p\">)</span>\n
  \   <span class=\"p\">)</span>\n\n    <span class=\"k\">return</span> <span class=\"n\">project</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"test_loaded-function\">test_loaded <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>test_loaded
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">test_loaded</span><span class=\"p\">(</span><span class=\"n\">make_project</span><span
  class=\"p\">:</span> <span class=\"n\">Any</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">os</span><span class=\"o\">.</span><span class=\"n\">chdir</span><span
  class=\"p\">(</span><span class=\"n\">make_project</span><span class=\"p\">)</span>\n
  \   <span class=\"n\">m</span> <span class=\"o\">=</span> <span class=\"n\">Markata</span><span
  class=\"p\">()</span>\n    <span class=\"k\">assert</span> <span class=\"nb\">len</span><span
  class=\"p\">(</span><span class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">py_files</span><span
  class=\"p\">)</span> <span class=\"o\">==</span> <span class=\"mi\">1</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"test_run-function\">test_run <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>test_run
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">test_run</span><span class=\"p\">(</span><span class=\"n\">make_project</span><span
  class=\"p\">:</span> <span class=\"n\">Any</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">os</span><span class=\"o\">.</span><span class=\"n\">chdir</span><span
  class=\"p\">(</span><span class=\"n\">make_project</span><span class=\"p\">)</span>\n
  \   <span class=\"n\">m</span> <span class=\"o\">=</span> <span class=\"n\">Markata</span><span
  class=\"p\">()</span>\n    <span class=\"n\">m</span><span class=\"o\">.</span><span
  class=\"n\">run</span><span class=\"p\">()</span>\n    <span class=\"k\">return</span>
  <span class=\"n\">make_project</span>\n</code></pre></div>\n</details>\n<hr />\n<h2
  id=\"test_markout_exists-function\">test_markout_exists <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>test_markout_exists
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">test_markout_exists</span><span class=\"p\">(</span><span class=\"n\">test_run</span><span
  class=\"p\">:</span> <span class=\"n\">Any</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">markout</span> <span class=\"o\">=</span> <span class=\"n\">test_run</span>
  <span class=\"o\">/</span> <span class=\"s2\">&quot;markout&quot;</span>\n    <span
  class=\"k\">assert</span> <span class=\"n\">markout</span><span class=\"o\">.</span><span
  class=\"n\">exists</span><span class=\"p\">()</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"test_index_exists-function\">test_index_exists <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>test_index_exists
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">test_index_exists</span><span class=\"p\">(</span><span class=\"n\">test_run</span><span
  class=\"p\">:</span> <span class=\"n\">Any</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">markout</span> <span class=\"o\">=</span> <span class=\"n\">test_run</span>
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
  \   <span class=\"n\">markout</span> <span class=\"o\">=</span> <span class=\"n\">test_run</span>
  <span class=\"o\">/</span> <span class=\"s2\">&quot;markout&quot;</span>\n    <span
  class=\"n\">rss</span> <span class=\"o\">=</span> <span class=\"n\">markout</span>
  <span class=\"o\">/</span> <span class=\"s2\">&quot;rss.xml&quot;</span>\n    <span
  class=\"k\">assert</span> <span class=\"n\">rss</span><span class=\"o\">.</span><span
  class=\"n\">exists</span><span class=\"p\">()</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for test_doc_page
long_description: ''
now: 2022-02-05 19:38:00.891357
path: test_doc_page.md
slug: tests/test_doc_page
status: published
title: test_doc_page.py
today: 2022-02-05
---

---

## make_project `function`

None

??? "make_project source"
    ``` python
    def make_project(tmp_path_factory: Any) -> Any:
        project = tmp_path_factory.mktemp("project")
        module = project / "my_module.py"
        module.write_text(
            textwrap.dedent(
                """
                '''
                Module level docstring
                '''

                def my_func():
                    '''
                    docstring for my_func
                    '''
                class MyClass:
                    '''
                    docstring for MyClass
                    '''

                    def my_method(self):
                        '''
                        docstring for my_method
                        '''

                """
            )
        )
        markta_toml = project / "markata.toml"
        markta_toml.write_text(
            textwrap.dedent(
                """
                [markata]
                hooks = [
                    "markata.plugins.docs",
                    "default",
                    ]

                """
            )
        )

        return project
    ```


---

## test_loaded `function`

None

??? "test_loaded source"
    ``` python
    def test_loaded(make_project: Any) -> None:
        os.chdir(make_project)
        m = Markata()
        assert len(m.py_files) == 1
    ```


---

## test_run `function`

None

??? "test_run source"
    ``` python
    def test_run(make_project: Any) -> Any:
        os.chdir(make_project)
        m = Markata()
        m.run()
        return make_project
    ```


---

## test_markout_exists `function`

None

??? "test_markout_exists source"
    ``` python
    def test_markout_exists(test_run: Any) -> Any:
        markout = test_run / "markout"
        assert markout.exists()
    ```


---

## test_index_exists `function`

None

??? "test_index_exists source"
    ``` python
    def test_index_exists(test_run: Any) -> Any:
        markout = test_run / "markout"
        index = markout / "index.html"
        assert index.exists()
    ```


---

## test_rss_exists `function`

None

??? "test_rss_exists source"
    ``` python
    def test_rss_exists(test_run: Any) -> Any:
        markout = test_run / "markout"
        rss = markout / "rss.xml"
        assert rss.exists()
    ```