---
article_html: "<p>Default glob plugin</p>\n<hr />\n<h2 id=\"glob-function\">glob <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>glob
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">glob</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n\n
  \   <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">files</span>
  <span class=\"o\">=</span> <span class=\"nb\">list</span><span class=\"p\">(</span>\n
  \       <span class=\"n\">flatten</span><span class=\"p\">([</span><span class=\"n\">Path</span><span
  class=\"p\">()</span><span class=\"o\">.</span><span class=\"n\">glob</span><span
  class=\"p\">(</span><span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"n\">pattern</span><span class=\"p\">))</span> <span class=\"k\">for</span>
  <span class=\"n\">pattern</span> <span class=\"ow\">in</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">glob_patterns</span><span class=\"p\">])</span>\n
  \   <span class=\"p\">)</span>\n    <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">content_directories</span> <span class=\"o\">=</span> <span class=\"nb\">list</span><span
  class=\"p\">(</span><span class=\"nb\">set</span><span class=\"p\">([</span><span
  class=\"n\">f</span><span class=\"o\">.</span><span class=\"n\">parent</span> <span
  class=\"k\">for</span> <span class=\"n\">f</span> <span class=\"ow\">in</span> <span
  class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">files</span><span
  class=\"p\">]))</span>\n\n    <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \       <span class=\"n\">ignore</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;glob&quot;</span><span class=\"p\">][</span><span class=\"s2\">&quot;use_gitignore&quot;</span><span
  class=\"p\">]</span> <span class=\"ow\">or</span> <span class=\"kc\">True</span>\n
  \   <span class=\"k\">except</span> <span class=\"ne\">KeyError</span><span class=\"p\">:</span>\n
  \       <span class=\"n\">ignore</span> <span class=\"o\">=</span> <span class=\"kc\">True</span>\n\n
  \   <span class=\"k\">if</span> <span class=\"n\">ignore</span> <span class=\"ow\">and</span>
  <span class=\"p\">(</span><span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;.gitignore&quot;</span><span class=\"p\">)</span><span class=\"o\">.</span><span
  class=\"n\">exists</span><span class=\"p\">()</span> <span class=\"ow\">or</span>
  <span class=\"n\">Path</span><span class=\"p\">(</span><span class=\"s2\">&quot;.markataignore&quot;</span><span
  class=\"p\">)</span><span class=\"o\">.</span><span class=\"n\">exists</span><span
  class=\"p\">()):</span>\n        <span class=\"kn\">import</span> <span class=\"nn\">pathspec</span>\n\n
  \       <span class=\"n\">lines</span> <span class=\"o\">=</span> <span class=\"p\">[]</span>\n\n
  \       <span class=\"k\">if</span> <span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;.gitignore&quot;</span><span class=\"p\">)</span><span class=\"o\">.</span><span
  class=\"n\">exists</span><span class=\"p\">():</span>\n            <span class=\"n\">lines</span><span
  class=\"o\">.</span><span class=\"n\">extend</span><span class=\"p\">(</span><span
  class=\"n\">Path</span><span class=\"p\">(</span><span class=\"s2\">&quot;.gitignore&quot;</span><span
  class=\"p\">)</span><span class=\"o\">.</span><span class=\"n\">read_text</span><span
  class=\"p\">()</span><span class=\"o\">.</span><span class=\"n\">splitlines</span><span
  class=\"p\">())</span>\n\n        <span class=\"k\">if</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;.markataignore&quot;</span><span class=\"p\">)</span><span
  class=\"o\">.</span><span class=\"n\">exists</span><span class=\"p\">():</span>\n
  \           <span class=\"n\">lines</span><span class=\"o\">.</span><span class=\"n\">extend</span><span
  class=\"p\">(</span><span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;.markataignore&quot;</span><span class=\"p\">)</span><span class=\"o\">.</span><span
  class=\"n\">read_text</span><span class=\"p\">()</span><span class=\"o\">.</span><span
  class=\"n\">splitlines</span><span class=\"p\">())</span>\n\n        <span class=\"n\">spec</span>
  <span class=\"o\">=</span> <span class=\"n\">pathspec</span><span class=\"o\">.</span><span
  class=\"n\">PathSpec</span><span class=\"o\">.</span><span class=\"n\">from_lines</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;gitwildmatch&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">lines</span><span class=\"p\">)</span>\n\n        <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">files</span> <span class=\"o\">=</span> <span
  class=\"p\">[</span>\n            <span class=\"n\">file</span> <span class=\"k\">for</span>
  <span class=\"n\">file</span> <span class=\"ow\">in</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">files</span> <span class=\"k\">if</span> <span
  class=\"ow\">not</span> <span class=\"n\">spec</span><span class=\"o\">.</span><span
  class=\"n\">match_file</span><span class=\"p\">(</span><span class=\"nb\">str</span><span
  class=\"p\">(</span><span class=\"n\">file</span><span class=\"p\">))</span>\n        <span
  class=\"p\">]</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for glob
long_description: ''
now: 2022-02-05 19:38:00.891448
path: glob.md
slug: markata/plugins/glob
status: published
title: glob.py
today: 2022-02-05
---

Default glob plugin


---

## glob `function`

None

??? "glob source"
    ``` python
    def glob(markata: "Markata") -> None:

        markata.files = list(
            flatten([Path().glob(str(pattern)) for pattern in markata.glob_patterns])
        )
        markata.content_directories = list(set([f.parent for f in markata.files]))

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

            markata.files = [
                file for file in markata.files if not spec.match_file(str(file))
            ]
    ```