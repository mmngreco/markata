---
article_html: "<p>leading docstring</p>\n<hr />\n<h2 id=\"add_parents-function\">add_parents
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>add_parents source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">add_parents</span><span
  class=\"p\">(</span><span class=\"n\">tree</span><span class=\"p\">:</span> <span
  class=\"n\">ast</span><span class=\"o\">.</span><span class=\"n\">AST</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n    <span class=\"k\">for</span> <span class=\"n\">node</span>
  <span class=\"ow\">in</span> <span class=\"n\">ast</span><span class=\"o\">.</span><span
  class=\"n\">walk</span><span class=\"p\">(</span><span class=\"n\">tree</span><span
  class=\"p\">):</span>\n        <span class=\"k\">for</span> <span class=\"n\">child</span>
  <span class=\"ow\">in</span> <span class=\"n\">ast</span><span class=\"o\">.</span><span
  class=\"n\">iter_child_nodes</span><span class=\"p\">(</span><span class=\"n\">node</span><span
  class=\"p\">):</span>\n            <span class=\"n\">child</span><span class=\"o\">.</span><span
  class=\"n\">parent</span> <span class=\"o\">=</span> <span class=\"n\">node</span>\n
  \           <span class=\"k\">if</span> <span class=\"ow\">not</span> <span class=\"nb\">hasattr</span><span
  class=\"p\">(</span><span class=\"n\">child</span><span class=\"p\">,</span> <span
  class=\"s2\">&quot;parents&quot;</span><span class=\"p\">):</span>\n                <span
  class=\"n\">child</span><span class=\"o\">.</span><span class=\"n\">parents</span>
  <span class=\"o\">=</span> <span class=\"p\">[</span><span class=\"n\">node</span><span
  class=\"p\">]</span>\n            <span class=\"n\">child</span><span class=\"o\">.</span><span
  class=\"n\">parents</span><span class=\"o\">.</span><span class=\"n\">append</span><span
  class=\"p\">(</span><span class=\"n\">node</span><span class=\"p\">)</span>\n            <span
  class=\"k\">if</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"n\">node</span><span class=\"p\">,</span> <span class=\"n\">ast</span><span
  class=\"o\">.</span><span class=\"n\">ClassDef</span><span class=\"p\">)</span>
  <span class=\"ow\">and</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"n\">child</span><span class=\"p\">,</span> <span class=\"n\">ast</span><span
  class=\"o\">.</span><span class=\"n\">FunctionDef</span><span class=\"p\">):</span>\n
  \               <span class=\"n\">child</span><span class=\"o\">.</span><span class=\"n\">type</span>
  <span class=\"o\">=</span> <span class=\"s2\">&quot;method&quot;</span>\n            <span
  class=\"k\">elif</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"n\">child</span><span class=\"p\">,</span> <span class=\"n\">ast</span><span
  class=\"o\">.</span><span class=\"n\">FunctionDef</span><span class=\"p\">):</span>\n
  \               <span class=\"n\">child</span><span class=\"o\">.</span><span class=\"n\">type</span>
  <span class=\"o\">=</span> <span class=\"s2\">&quot;function&quot;</span>\n            <span
  class=\"k\">elif</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"n\">child</span><span class=\"p\">,</span> <span class=\"n\">ast</span><span
  class=\"o\">.</span><span class=\"n\">ClassDef</span><span class=\"p\">):</span>\n
  \               <span class=\"n\">child</span><span class=\"o\">.</span><span class=\"n\">type</span>
  <span class=\"o\">=</span> <span class=\"s2\">&quot;class&quot;</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"glob-function\">glob <code>function</code></h2>\n<p>finds k</p>\n<h2
  id=\"parameters\">Parameters</h2>\n<p><code>markata</code> the markata object</p>\n<details>\n<summary>glob
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">glob</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;MarkataDocs&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"sd\">&quot;&quot;&quot;</span>\n<span class=\"sd\">    finds k</span>\n\n<span
  class=\"sd\">    ## Parameters</span>\n\n<span class=\"sd\">    `markata` the markata
  object</span>\n\n<span class=\"sd\">    &quot;&quot;&quot;</span>\n\n    <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">py_files</span> <span class=\"o\">=</span>
  <span class=\"nb\">list</span><span class=\"p\">(</span><span class=\"n\">Path</span><span
  class=\"p\">()</span><span class=\"o\">.</span><span class=\"n\">glob</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;**/*.py&quot;</span><span class=\"p\">))</span>\n\n
  \   <span class=\"n\">content_directories</span> <span class=\"o\">=</span> <span
  class=\"nb\">list</span><span class=\"p\">(</span><span class=\"nb\">set</span><span
  class=\"p\">([</span><span class=\"n\">f</span><span class=\"o\">.</span><span class=\"n\">parent</span>
  <span class=\"k\">for</span> <span class=\"n\">f</span> <span class=\"ow\">in</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">py_files</span><span
  class=\"p\">]))</span>\n    <span class=\"k\">if</span> <span class=\"s2\">&quot;content_directories&quot;</span>
  <span class=\"ow\">in</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"vm\">__dict__</span><span class=\"o\">.</span><span class=\"n\">keys</span><span
  class=\"p\">():</span>\n        <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">content_directories</span><span class=\"o\">.</span><span class=\"n\">extend</span><span
  class=\"p\">(</span><span class=\"n\">content_directories</span><span class=\"p\">)</span>\n
  \   <span class=\"k\">else</span><span class=\"p\">:</span>\n        <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">content_directories</span> <span class=\"o\">=</span>
  <span class=\"n\">content_directories</span>\n\n    <span class=\"k\">try</span><span
  class=\"p\">:</span>\n        <span class=\"n\">ignore</span> <span class=\"o\">=</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;glob&quot;</span><span class=\"p\">][</span><span
  class=\"s2\">&quot;use_gitignore&quot;</span><span class=\"p\">]</span> <span class=\"ow\">or</span>
  <span class=\"kc\">True</span>\n    <span class=\"k\">except</span> <span class=\"ne\">KeyError</span><span
  class=\"p\">:</span>\n        <span class=\"n\">ignore</span> <span class=\"o\">=</span>
  <span class=\"kc\">True</span>\n\n    <span class=\"k\">if</span> <span class=\"n\">ignore</span>
  <span class=\"ow\">and</span> <span class=\"p\">(</span><span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;.gitignore&quot;</span><span class=\"p\">)</span><span
  class=\"o\">.</span><span class=\"n\">exists</span><span class=\"p\">()</span> <span
  class=\"ow\">or</span> <span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;.markataignore&quot;</span><span class=\"p\">)</span><span class=\"o\">.</span><span
  class=\"n\">exists</span><span class=\"p\">()):</span>\n        <span class=\"kn\">import</span>
  <span class=\"nn\">pathspec</span>\n\n        <span class=\"n\">lines</span> <span
  class=\"o\">=</span> <span class=\"p\">[]</span>\n\n        <span class=\"k\">if</span>
  <span class=\"n\">Path</span><span class=\"p\">(</span><span class=\"s2\">&quot;.gitignore&quot;</span><span
  class=\"p\">)</span><span class=\"o\">.</span><span class=\"n\">exists</span><span
  class=\"p\">():</span>\n            <span class=\"n\">lines</span><span class=\"o\">.</span><span
  class=\"n\">extend</span><span class=\"p\">(</span><span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;.gitignore&quot;</span><span class=\"p\">)</span><span
  class=\"o\">.</span><span class=\"n\">read_text</span><span class=\"p\">()</span><span
  class=\"o\">.</span><span class=\"n\">splitlines</span><span class=\"p\">())</span>\n\n
  \       <span class=\"k\">if</span> <span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;.markataignore&quot;</span><span class=\"p\">)</span><span class=\"o\">.</span><span
  class=\"n\">exists</span><span class=\"p\">():</span>\n            <span class=\"n\">lines</span><span
  class=\"o\">.</span><span class=\"n\">extend</span><span class=\"p\">(</span><span
  class=\"n\">Path</span><span class=\"p\">(</span><span class=\"s2\">&quot;.markataignore&quot;</span><span
  class=\"p\">)</span><span class=\"o\">.</span><span class=\"n\">read_text</span><span
  class=\"p\">()</span><span class=\"o\">.</span><span class=\"n\">splitlines</span><span
  class=\"p\">())</span>\n\n        <span class=\"n\">spec</span> <span class=\"o\">=</span>
  <span class=\"n\">pathspec</span><span class=\"o\">.</span><span class=\"n\">PathSpec</span><span
  class=\"o\">.</span><span class=\"n\">from_lines</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;gitwildmatch&quot;</span><span class=\"p\">,</span> <span class=\"n\">lines</span><span
  class=\"p\">)</span>\n\n        <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">py_files</span> <span class=\"o\">=</span> <span class=\"p\">[</span>\n
  \           <span class=\"n\">file</span> <span class=\"k\">for</span> <span class=\"n\">file</span>
  <span class=\"ow\">in</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">py_files</span> <span class=\"k\">if</span> <span class=\"ow\">not</span>
  <span class=\"n\">spec</span><span class=\"o\">.</span><span class=\"n\">match_file</span><span
  class=\"p\">(</span><span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"n\">file</span><span class=\"p\">))</span>\n        <span class=\"p\">]</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"make_article-function\">make_article <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>make_article
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">make_article</span><span class=\"p\">(</span><span class=\"n\">file</span><span
  class=\"p\">:</span> <span class=\"n\">Path</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"n\">frontmatter</span><span class=\"o\">.</span><span
  class=\"n\">Post</span><span class=\"p\">:</span>\n    <span class=\"n\">raw_source</span>
  <span class=\"o\">=</span> <span class=\"n\">file</span><span class=\"o\">.</span><span
  class=\"n\">read_text</span><span class=\"p\">()</span>\n    <span class=\"n\">tree</span>
  <span class=\"o\">=</span> <span class=\"n\">ast</span><span class=\"o\">.</span><span
  class=\"n\">parse</span><span class=\"p\">(</span><span class=\"n\">raw_source</span><span
  class=\"p\">)</span>\n    <span class=\"n\">add_parents</span><span class=\"p\">(</span><span
  class=\"n\">tree</span><span class=\"p\">)</span>\n    <span class=\"n\">nodes</span>
  <span class=\"o\">=</span> <span class=\"p\">[</span>\n        <span class=\"n\">n</span>\n
  \       <span class=\"k\">for</span> <span class=\"n\">n</span> <span class=\"ow\">in</span>
  <span class=\"n\">ast</span><span class=\"o\">.</span><span class=\"n\">walk</span><span
  class=\"p\">(</span><span class=\"n\">tree</span><span class=\"p\">)</span>\n        <span
  class=\"k\">if</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"n\">n</span><span class=\"p\">,</span> <span class=\"n\">ast</span><span
  class=\"o\">.</span><span class=\"n\">FunctionDef</span><span class=\"p\">)</span>
  <span class=\"ow\">or</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"n\">n</span><span class=\"p\">,</span> <span class=\"n\">ast</span><span
  class=\"o\">.</span><span class=\"n\">ClassDef</span><span class=\"p\">)</span>\n
  \   <span class=\"p\">]</span>\n    <span class=\"n\">article</span> <span class=\"o\">=</span>
  <span class=\"n\">textwrap</span><span class=\"o\">.</span><span class=\"n\">dedent</span><span
  class=\"p\">(</span>\n        <span class=\"sa\">f</span><span class=\"s2\">&quot;&quot;&quot;</span>\n<span
  class=\"s2\">    ---</span>\n<span class=\"s2\">    title: </span><span class=\"si\">{</span><span
  class=\"n\">file</span><span class=\"o\">.</span><span class=\"n\">name</span><span
  class=\"si\">}</span><span class=\"s2\"></span>\n<span class=\"s2\">    status:
  published</span>\n<span class=\"s2\">    slug: </span><span class=\"si\">{</span><span
  class=\"n\">file</span><span class=\"o\">.</span><span class=\"n\">parent</span><span
  class=\"si\">}</span><span class=\"s2\">/</span><span class=\"si\">{</span><span
  class=\"n\">file</span><span class=\"o\">.</span><span class=\"n\">stem</span><span
  class=\"si\">}</span><span class=\"s2\"></span>\n<span class=\"s2\">    path: </span><span
  class=\"si\">{</span><span class=\"n\">file</span><span class=\"o\">.</span><span
  class=\"n\">stem</span><span class=\"si\">}</span><span class=\"s2\">.md</span>\n<span
  class=\"s2\">    today: </span><span class=\"si\">{</span><span class=\"n\">datetime</span><span
  class=\"o\">.</span><span class=\"n\">datetime</span><span class=\"o\">.</span><span
  class=\"n\">today</span><span class=\"p\">()</span><span class=\"si\">}</span><span
  class=\"s2\"></span>\n<span class=\"s2\">    description: Docs for </span><span
  class=\"si\">{</span><span class=\"n\">file</span><span class=\"o\">.</span><span
  class=\"n\">stem</span><span class=\"si\">}</span><span class=\"s2\"></span>\n\n<span
  class=\"s2\">    ---</span>\n\n<span class=\"s2\">    &quot;&quot;&quot;</span>\n
  \   <span class=\"p\">)</span>\n    <span class=\"n\">article</span> <span class=\"o\">+=</span>
  <span class=\"n\">textwrap</span><span class=\"o\">.</span><span class=\"n\">dedent</span><span
  class=\"p\">(</span>\n        <span class=\"sa\">f</span><span class=\"s2\">&quot;&quot;&quot;</span>\n<span
  class=\"s2\">            </span><span class=\"si\">{</span><span class=\"n\">ast</span><span
  class=\"o\">.</span><span class=\"n\">get_docstring</span><span class=\"p\">(</span><span
  class=\"n\">tree</span><span class=\"p\">)</span> <span class=\"ow\">or</span> <span
  class=\"s2\">&quot;&quot;</span><span class=\"si\">}</span><span class=\"s2\"></span>\n<span
  class=\"s2\">            &quot;&quot;&quot;</span>\n    <span class=\"p\">)</span>\n
  \   <span class=\"k\">for</span> <span class=\"n\">node</span> <span class=\"ow\">in</span>
  <span class=\"n\">nodes</span><span class=\"p\">:</span>\n        <span class=\"n\">article</span>
  <span class=\"o\">+=</span> <span class=\"n\">textwrap</span><span class=\"o\">.</span><span
  class=\"n\">dedent</span><span class=\"p\">(</span>\n            <span class=\"sa\">f</span><span
  class=\"s2\">&quot;&quot;&quot;</span>\n\n<span class=\"s2\">---</span>\n\n<span
  class=\"s2\">## </span><span class=\"si\">{</span><span class=\"n\">node</span><span
  class=\"o\">.</span><span class=\"n\">name</span><span class=\"si\">}</span><span
  class=\"s2\"> `</span><span class=\"si\">{</span><span class=\"n\">node</span><span
  class=\"o\">.</span><span class=\"n\">type</span><span class=\"si\">}</span><span
  class=\"s2\">`</span>\n\n<span class=\"si\">{</span><span class=\"n\">ast</span><span
  class=\"o\">.</span><span class=\"n\">get_docstring</span><span class=\"p\">(</span><span
  class=\"n\">node</span><span class=\"p\">)</span><span class=\"si\">}</span><span
  class=\"s2\"></span>\n\n<span class=\"s2\">??? &quot;</span><span class=\"si\">{</span><span
  class=\"n\">node</span><span class=\"o\">.</span><span class=\"n\">name</span><span
  class=\"si\">}</span><span class=\"s2\"> source&quot;</span>\n<span class=\"s2\">
  \   ``` python</span>\n<span class=\"si\">{</span><span class=\"n\">textwrap</span><span
  class=\"o\">.</span><span class=\"n\">indent</span><span class=\"p\">(</span><span
  class=\"n\">ast</span><span class=\"o\">.</span><span class=\"n\">get_source_segment</span><span
  class=\"p\">(</span><span class=\"n\">raw_source</span><span class=\"p\">,</span>
  <span class=\"n\">node</span><span class=\"p\">),</span> <span class=\"s1\">&#39;
  \   &#39;</span><span class=\"p\">)</span><span class=\"si\">}</span><span class=\"s2\"></span>\n<span
  class=\"s2\">    ```</span>\n<span class=\"s2\">        &quot;&quot;&quot;</span>\n
  \       <span class=\"p\">)</span>\n\n    <span class=\"k\">return</span> <span
  class=\"n\">frontmatter</span><span class=\"o\">.</span><span class=\"n\">loads</span><span
  class=\"p\">(</span><span class=\"n\">article</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"load-function\">load <code>function</code></h2>\n<p>similar to <a href=\"../glob\">glob</a></p>\n<details>\n<summary>load
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">load</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;MarkataDocs&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"sd\">&quot;&quot;&quot;</span>\n<span class=\"sd\">    similar
  to [glob](../glob)</span>\n<span class=\"sd\">    &quot;&quot;&quot;</span>\n    <span
  class=\"k\">if</span> <span class=\"s2\">&quot;articles&quot;</span> <span class=\"ow\">not</span>
  <span class=\"ow\">in</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"vm\">__dict__</span><span class=\"p\">:</span>\n        <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">articles</span> <span class=\"o\">=</span>
  <span class=\"p\">[]</span>\n    <span class=\"k\">for</span> <span class=\"n\">py_file</span>
  <span class=\"ow\">in</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">py_files</span><span class=\"p\">:</span>\n        <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">articles</span><span class=\"o\">.</span><span
  class=\"n\">append</span><span class=\"p\">(</span><span class=\"n\">make_article</span><span
  class=\"p\">(</span><span class=\"n\">py_file</span><span class=\"p\">))</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"markatadocs-class\">MarkataDocs <code>class</code></h2>\n<p>None</p>\n<details>\n<summary>MarkataDocs
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span>
  <span class=\"nc\">MarkataDocs</span><span class=\"p\">(</span><span class=\"n\">Markata</span><span
  class=\"p\">):</span>\n        <span class=\"n\">py_files</span><span class=\"p\">:</span>
  <span class=\"n\">List</span> <span class=\"o\">=</span> <span class=\"p\">[]</span>\n
  \       <span class=\"n\">content_directories</span><span class=\"p\">:</span> <span
  class=\"n\">List</span> <span class=\"o\">=</span> <span class=\"p\">[]</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for docs
long_description: ''
now: 2022-02-05 19:38:00.891423
path: docs.md
slug: markata/plugins/docs
status: published
title: docs.py
today: 2022-02-05
---

leading docstring


---

## add_parents `function`

None

??? "add_parents source"
    ``` python
    def add_parents(tree: ast.AST) -> None:
        for node in ast.walk(tree):
            for child in ast.iter_child_nodes(node):
                child.parent = node
                if not hasattr(child, "parents"):
                    child.parents = [node]
                child.parents.append(node)
                if isinstance(node, ast.ClassDef) and isinstance(child, ast.FunctionDef):
                    child.type = "method"
                elif isinstance(child, ast.FunctionDef):
                    child.type = "function"
                elif isinstance(child, ast.ClassDef):
                    child.type = "class"
    ```


---

## glob `function`

finds k

## Parameters

`markata` the markata object

??? "glob source"
    ``` python
    def glob(markata: "MarkataDocs") -> None:
        """
        finds k

        ## Parameters

        `markata` the markata object

        """

        markata.py_files = list(Path().glob("**/*.py"))

        content_directories = list(set([f.parent for f in markata.py_files]))
        if "content_directories" in markata.__dict__.keys():
            markata.content_directories.extend(content_directories)
        else:
            markata.content_directories = content_directories

        try:
            ignore = markata.config["glob"]["use_gitignore"] or True
        except KeyError:
            ignore = True

        if ignore and (Path(".gitignore").exists() or Path(".markataignore").exists()):
            import pathspec

            lines = []

            if Path(".gitignore").exists():
                lines.extend(Path(".gitignore").read_text().splitlines())

            if Path(".markataignore").exists():
                lines.extend(Path(".markataignore").read_text().splitlines())

            spec = pathspec.PathSpec.from_lines("gitwildmatch", lines)

            markata.py_files = [
                file for file in markata.py_files if not spec.match_file(str(file))
            ]
    ```


---

## make_article `function`

None

??? "make_article source"
    ``` python
    def make_article(file: Path) -> frontmatter.Post:
        raw_source = file.read_text()
        tree = ast.parse(raw_source)
        add_parents(tree)
        nodes = [
            n
            for n in ast.walk(tree)
            if isinstance(n, ast.FunctionDef) or isinstance(n, ast.ClassDef)
        ]
        article = textwrap.dedent(
            f"""
        ---
        title: {file.name}
        status: published
        slug: {file.parent}/{file.stem}
        path: {file.stem}.md
        today: {datetime.datetime.today()}
        description: Docs for {file.stem}

        ---

        """
        )
        article += textwrap.dedent(
            f"""
                {ast.get_docstring(tree) or ""}
                """
        )
        for node in nodes:
            article += textwrap.dedent(
                f"""

    ---

    ## {node.name} `{node.type}`

    {ast.get_docstring(node)}

    ??? "{node.name} source"
        ``` python
    {textwrap.indent(ast.get_source_segment(raw_source, node), '    ')}
        ```
            """
            )

        return frontmatter.loads(article)
    ```


---

## load `function`

similar to [glob](../glob)

??? "load source"
    ``` python
    def load(markata: "MarkataDocs") -> None:
        """
        similar to [glob](../glob)
        """
        if "articles" not in markata.__dict__:
            markata.articles = []
        for py_file in markata.py_files:
            markata.articles.append(make_article(py_file))
    ```


---

## MarkataDocs `class`

None

??? "MarkataDocs source"
    ``` python
    class MarkataDocs(Markata):
            py_files: List = []
            content_directories: List = []
    ```