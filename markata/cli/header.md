---
article_html: "<hr />\n<h2 id=\"header-class\">Header <code>class</code></h2>\n<p>Display
  header with clock.</p>\n<details>\n<summary>Header source</summary>\n<div class=\"highlight\"><pre><span></span><code><span
  class=\"k\">class</span> <span class=\"nc\">Header</span><span class=\"p\">:</span>\n
  \   <span class=\"sd\">&quot;&quot;&quot;Display header with clock.&quot;&quot;&quot;</span>\n\n
  \   <span class=\"k\">def</span> <span class=\"nf\">__rich__</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">Panel</span><span class=\"p\">:</span>\n        <span class=\"n\">grid</span>
  <span class=\"o\">=</span> <span class=\"n\">Table</span><span class=\"o\">.</span><span
  class=\"n\">grid</span><span class=\"p\">(</span><span class=\"n\">expand</span><span
  class=\"o\">=</span><span class=\"kc\">True</span><span class=\"p\">)</span>\n        <span
  class=\"n\">grid</span><span class=\"o\">.</span><span class=\"n\">add_column</span><span
  class=\"p\">(</span><span class=\"n\">justify</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;center&quot;</span><span class=\"p\">,</span> <span class=\"n\">ratio</span><span
  class=\"o\">=</span><span class=\"mi\">1</span><span class=\"p\">)</span>\n        <span
  class=\"n\">grid</span><span class=\"o\">.</span><span class=\"n\">add_column</span><span
  class=\"p\">(</span><span class=\"n\">justify</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;right&quot;</span><span class=\"p\">)</span>\n        <span class=\"n\">grid</span><span
  class=\"o\">.</span><span class=\"n\">add_row</span><span class=\"p\">(</span>\n
  \           <span class=\"s2\">&quot;[magenta][b]Markata[/b][/] [bright_black]Live
  Server[/]&quot;</span><span class=\"p\">,</span>\n            <span class=\"n\">datetime</span><span
  class=\"o\">.</span><span class=\"n\">now</span><span class=\"p\">()</span><span
  class=\"o\">.</span><span class=\"n\">ctime</span><span class=\"p\">(),</span>\n
  \       <span class=\"p\">)</span>\n        <span class=\"k\">return</span> <span
  class=\"n\">Panel</span><span class=\"p\">(</span><span class=\"n\">grid</span><span
  class=\"p\">,</span> <span class=\"n\">style</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;yellow&quot;</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"rich-method\"><strong>rich</strong> <code>method</code></h2>\n<p>None</p>\n<details>\n<summary><strong>rich</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">__rich__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Panel</span><span
  class=\"p\">:</span>\n        <span class=\"n\">grid</span> <span class=\"o\">=</span>
  <span class=\"n\">Table</span><span class=\"o\">.</span><span class=\"n\">grid</span><span
  class=\"p\">(</span><span class=\"n\">expand</span><span class=\"o\">=</span><span
  class=\"kc\">True</span><span class=\"p\">)</span>\n        <span class=\"n\">grid</span><span
  class=\"o\">.</span><span class=\"n\">add_column</span><span class=\"p\">(</span><span
  class=\"n\">justify</span><span class=\"o\">=</span><span class=\"s2\">&quot;center&quot;</span><span
  class=\"p\">,</span> <span class=\"n\">ratio</span><span class=\"o\">=</span><span
  class=\"mi\">1</span><span class=\"p\">)</span>\n        <span class=\"n\">grid</span><span
  class=\"o\">.</span><span class=\"n\">add_column</span><span class=\"p\">(</span><span
  class=\"n\">justify</span><span class=\"o\">=</span><span class=\"s2\">&quot;right&quot;</span><span
  class=\"p\">)</span>\n        <span class=\"n\">grid</span><span class=\"o\">.</span><span
  class=\"n\">add_row</span><span class=\"p\">(</span>\n            <span class=\"s2\">&quot;[magenta][b]Markata[/b][/]
  [bright_black]Live Server[/]&quot;</span><span class=\"p\">,</span>\n            <span
  class=\"n\">datetime</span><span class=\"o\">.</span><span class=\"n\">now</span><span
  class=\"p\">()</span><span class=\"o\">.</span><span class=\"n\">ctime</span><span
  class=\"p\">(),</span>\n        <span class=\"p\">)</span>\n        <span class=\"k\">return</span>
  <span class=\"n\">Panel</span><span class=\"p\">(</span><span class=\"n\">grid</span><span
  class=\"p\">,</span> <span class=\"n\">style</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;yellow&quot;</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for header
long_description: ''
now: 2022-02-05 19:38:00.891464
path: header.md
slug: markata/cli/header
status: published
title: header.py
today: 2022-02-05
---

---

## Header `class`

Display header with clock.

??? "Header source"
    ``` python
    class Header:
        """Display header with clock."""

        def __rich__(self) -> Panel:
            grid = Table.grid(expand=True)
            grid.add_column(justify="center", ratio=1)
            grid.add_column(justify="right")
            grid.add_row(
                "[magenta][b]Markata[/b][/] [bright_black]Live Server[/]",
                datetime.now().ctime(),
            )
            return Panel(grid, style="yellow")
    ```


---

## __rich__ `method`

None

??? "__rich__ source"
    ``` python
    def __rich__(self) -> Panel:
            grid = Table.grid(expand=True)
            grid.add_column(justify="center", ratio=1)
            grid.add_column(justify="right")
            grid.add_row(
                "[magenta][b]Markata[/b][/] [bright_black]Live Server[/]",
                datetime.now().ctime(),
            )
            return Panel(grid, style="yellow")
    ```