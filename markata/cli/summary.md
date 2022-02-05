---
article_html: "<hr />\n<h2 id=\"summary-class\">Summary <code>class</code></h2>\n<p>None</p>\n<details>\n<summary>Summary
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span>
  <span class=\"nc\">Summary</span><span class=\"p\">:</span>\n    <span class=\"k\">def</span>
  <span class=\"fm\">__init__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">m</span><span class=\"p\">:</span> <span
  class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">,</span> <span class=\"n\">simple</span><span
  class=\"p\">:</span> <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span
  class=\"kc\">False</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">m</span> <span class=\"o\">=</span> <span
  class=\"n\">m</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">simple</span> <span class=\"o\">=</span> <span class=\"n\">simple</span>\n\n
  \   <span class=\"k\">def</span> <span class=\"nf\">__rich__</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">Union</span><span class=\"p\">[</span><span class=\"n\">Panel</span><span
  class=\"p\">,</span> <span class=\"n\">Table</span><span class=\"p\">]:</span>\n
  \       <span class=\"n\">grid</span> <span class=\"o\">=</span> <span class=\"n\">Table</span><span
  class=\"o\">.</span><span class=\"n\">grid</span><span class=\"p\">(</span><span
  class=\"n\">expand</span><span class=\"o\">=</span><span class=\"kc\">True</span><span
  class=\"p\">)</span>\n        <span class=\"n\">grid</span><span class=\"o\">.</span><span
  class=\"n\">add_row</span><span class=\"p\">(</span><span class=\"sa\">f</span><span
  class=\"s2\">&quot;[bright_blue]</span><span class=\"si\">{</span><span class=\"nb\">len</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">articles</span><span
  class=\"p\">)</span><span class=\"si\">}</span><span class=\"s2\">[/] articles&quot;</span><span
  class=\"p\">)</span>\n        <span class=\"n\">grid</span><span class=\"o\">.</span><span
  class=\"n\">add_row</span><span class=\"p\">(</span>\n            <span class=\"sa\">f</span><span
  class=\"s2\">&quot;[green]</span><span class=\"si\">{</span><span class=\"nb\">len</span><span
  class=\"p\">([</span><span class=\"n\">a</span> <span class=\"k\">for</span> <span
  class=\"n\">a</span> <span class=\"ow\">in</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">articles</span>
  <span class=\"k\">if</span> <span class=\"n\">a</span><span class=\"p\">[</span><span
  class=\"s1\">&#39;status&#39;</span><span class=\"p\">]</span> <span class=\"o\">==</span><span
  class=\"s1\">&#39;published&#39;</span><span class=\"p\">])</span><span class=\"si\">}</span><span
  class=\"s2\">[/] published&quot;</span>\n        <span class=\"p\">)</span>\n        <span
  class=\"n\">grid</span><span class=\"o\">.</span><span class=\"n\">add_row</span><span
  class=\"p\">(</span>\n            <span class=\"sa\">f</span><span class=\"s2\">&quot;[gold1]</span><span
  class=\"si\">{</span><span class=\"nb\">len</span><span class=\"p\">([</span><span
  class=\"n\">a</span> <span class=\"k\">for</span> <span class=\"n\">a</span> <span
  class=\"ow\">in</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">articles</span>
  <span class=\"k\">if</span> <span class=\"n\">a</span><span class=\"p\">[</span><span
  class=\"s1\">&#39;status&#39;</span><span class=\"p\">]</span> <span class=\"o\">==</span><span
  class=\"s1\">&#39;draft&#39;</span><span class=\"p\">])</span><span class=\"si\">}</span><span
  class=\"s2\">[/] drafts&quot;</span>\n        <span class=\"p\">)</span>\n        <span
  class=\"n\">grid</span><span class=\"o\">.</span><span class=\"n\">add_row</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"n\">grid</span><span class=\"o\">.</span><span class=\"n\">add_row</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;[bold gold1]TAGS[/]&quot;</span><span
  class=\"p\">)</span>\n        <span class=\"kn\">from</span> <span class=\"nn\">collections</span>
  <span class=\"kn\">import</span> <span class=\"n\">Counter</span>\n\n        <span
  class=\"kn\">from</span> <span class=\"nn\">more_itertools</span> <span class=\"kn\">import</span>
  <span class=\"n\">flatten</span>\n\n        <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \           <span class=\"k\">for</span> <span class=\"n\">tag</span><span class=\"p\">,</span>
  <span class=\"n\">count</span> <span class=\"ow\">in</span> <span class=\"n\">Counter</span><span
  class=\"p\">(</span>\n                <span class=\"nb\">list</span><span class=\"p\">(</span><span
  class=\"n\">flatten</span><span class=\"p\">([</span><span class=\"n\">a</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;tags&quot;</span><span class=\"p\">]</span>
  <span class=\"k\">for</span> <span class=\"n\">a</span> <span class=\"ow\">in</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">articles</span><span class=\"p\">]))</span>\n
  \           <span class=\"p\">)</span><span class=\"o\">.</span><span class=\"n\">most_common</span><span
  class=\"p\">():</span>\n                <span class=\"n\">grid</span><span class=\"o\">.</span><span
  class=\"n\">add_row</span><span class=\"p\">(</span><span class=\"sa\">f</span><span
  class=\"s1\">&#39;</span><span class=\"si\">{</span><span class=\"n\">count</span><span
  class=\"si\">}</span><span class=\"s1\"> </span><span class=\"si\">{</span><span
  class=\"s2\">&quot; &quot;</span><span class=\"o\">*</span><span class=\"p\">(</span><span
  class=\"mi\">3</span><span class=\"o\">-</span><span class=\"nb\">len</span><span
  class=\"p\">(</span><span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"n\">count</span><span class=\"p\">)))</span><span class=\"si\">}</span><span
  class=\"s1\"> </span><span class=\"si\">{</span><span class=\"n\">tag</span><span
  class=\"si\">}</span><span class=\"s1\">&#39;</span><span class=\"p\">)</span>\n
  \       <span class=\"k\">except</span> <span class=\"ne\">KeyError</span><span
  class=\"p\">:</span>\n            <span class=\"o\">...</span>\n\n        <span
  class=\"k\">try</span><span class=\"p\">:</span>\n            <span class=\"n\">grid</span><span
  class=\"o\">.</span><span class=\"n\">add_row</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;[bold gold1]Series[/]&quot;</span><span class=\"p\">)</span>\n
  \           <span class=\"k\">for</span> <span class=\"n\">series</span><span class=\"p\">,</span>
  <span class=\"n\">count</span> <span class=\"ow\">in</span> <span class=\"n\">Counter</span><span
  class=\"p\">(</span>\n                <span class=\"p\">[</span><span class=\"n\">a</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;templateKey&quot;</span><span class=\"p\">]</span>
  <span class=\"k\">for</span> <span class=\"n\">a</span> <span class=\"ow\">in</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">articles</span><span class=\"p\">]</span>\n
  \           <span class=\"p\">)</span><span class=\"o\">.</span><span class=\"n\">most_common</span><span
  class=\"p\">():</span>\n                <span class=\"n\">grid</span><span class=\"o\">.</span><span
  class=\"n\">add_row</span><span class=\"p\">(</span><span class=\"sa\">f</span><span
  class=\"s1\">&#39;</span><span class=\"si\">{</span><span class=\"n\">count</span><span
  class=\"si\">}</span><span class=\"s1\"> </span><span class=\"si\">{</span><span
  class=\"s2\">&quot; &quot;</span><span class=\"o\">*</span><span class=\"p\">(</span><span
  class=\"mi\">3</span><span class=\"o\">-</span><span class=\"nb\">len</span><span
  class=\"p\">(</span><span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"n\">count</span><span class=\"p\">)))</span><span class=\"si\">}</span><span
  class=\"s1\"> </span><span class=\"si\">{</span><span class=\"n\">series</span><span
  class=\"si\">}</span><span class=\"s1\">&#39;</span><span class=\"p\">)</span>\n
  \       <span class=\"k\">except</span> <span class=\"ne\">KeyError</span><span
  class=\"p\">:</span>\n            <span class=\"o\">...</span>\n        <span class=\"k\">if</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">simple</span><span
  class=\"p\">:</span>\n            <span class=\"k\">return</span> <span class=\"n\">grid</span>\n
  \       <span class=\"k\">else</span><span class=\"p\">:</span>\n            <span
  class=\"k\">return</span> <span class=\"n\">Panel</span><span class=\"p\">(</span><span
  class=\"n\">grid</span><span class=\"p\">,</span> <span class=\"n\">title</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;[gold1]summary[/]&quot;</span><span
  class=\"p\">,</span> <span class=\"n\">border_style</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;magenta&quot;</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"init-method\"><strong>init</strong> <code>method</code></h2>\n<p>None</p>\n<details>\n<summary><strong>init</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"fm\">__init__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">m</span><span class=\"p\">:</span> <span
  class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">,</span> <span class=\"n\">simple</span><span
  class=\"p\">:</span> <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span
  class=\"kc\">False</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">m</span> <span class=\"o\">=</span> <span
  class=\"n\">m</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">simple</span> <span class=\"o\">=</span> <span class=\"n\">simple</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"rich-method\"><strong>rich</strong> <code>method</code></h2>\n<p>None</p>\n<details>\n<summary><strong>rich</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">__rich__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Union</span><span
  class=\"p\">[</span><span class=\"n\">Panel</span><span class=\"p\">,</span> <span
  class=\"n\">Table</span><span class=\"p\">]:</span>\n        <span class=\"n\">grid</span>
  <span class=\"o\">=</span> <span class=\"n\">Table</span><span class=\"o\">.</span><span
  class=\"n\">grid</span><span class=\"p\">(</span><span class=\"n\">expand</span><span
  class=\"o\">=</span><span class=\"kc\">True</span><span class=\"p\">)</span>\n        <span
  class=\"n\">grid</span><span class=\"o\">.</span><span class=\"n\">add_row</span><span
  class=\"p\">(</span><span class=\"sa\">f</span><span class=\"s2\">&quot;[bright_blue]</span><span
  class=\"si\">{</span><span class=\"nb\">len</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">articles</span><span class=\"p\">)</span><span
  class=\"si\">}</span><span class=\"s2\">[/] articles&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"n\">grid</span><span class=\"o\">.</span><span class=\"n\">add_row</span><span
  class=\"p\">(</span>\n            <span class=\"sa\">f</span><span class=\"s2\">&quot;[green]</span><span
  class=\"si\">{</span><span class=\"nb\">len</span><span class=\"p\">([</span><span
  class=\"n\">a</span> <span class=\"k\">for</span> <span class=\"n\">a</span> <span
  class=\"ow\">in</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">articles</span>
  <span class=\"k\">if</span> <span class=\"n\">a</span><span class=\"p\">[</span><span
  class=\"s1\">&#39;status&#39;</span><span class=\"p\">]</span> <span class=\"o\">==</span><span
  class=\"s1\">&#39;published&#39;</span><span class=\"p\">])</span><span class=\"si\">}</span><span
  class=\"s2\">[/] published&quot;</span>\n        <span class=\"p\">)</span>\n        <span
  class=\"n\">grid</span><span class=\"o\">.</span><span class=\"n\">add_row</span><span
  class=\"p\">(</span>\n            <span class=\"sa\">f</span><span class=\"s2\">&quot;[gold1]</span><span
  class=\"si\">{</span><span class=\"nb\">len</span><span class=\"p\">([</span><span
  class=\"n\">a</span> <span class=\"k\">for</span> <span class=\"n\">a</span> <span
  class=\"ow\">in</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">articles</span>
  <span class=\"k\">if</span> <span class=\"n\">a</span><span class=\"p\">[</span><span
  class=\"s1\">&#39;status&#39;</span><span class=\"p\">]</span> <span class=\"o\">==</span><span
  class=\"s1\">&#39;draft&#39;</span><span class=\"p\">])</span><span class=\"si\">}</span><span
  class=\"s2\">[/] drafts&quot;</span>\n        <span class=\"p\">)</span>\n        <span
  class=\"n\">grid</span><span class=\"o\">.</span><span class=\"n\">add_row</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"n\">grid</span><span class=\"o\">.</span><span class=\"n\">add_row</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;[bold gold1]TAGS[/]&quot;</span><span
  class=\"p\">)</span>\n        <span class=\"kn\">from</span> <span class=\"nn\">collections</span>
  <span class=\"kn\">import</span> <span class=\"n\">Counter</span>\n\n        <span
  class=\"kn\">from</span> <span class=\"nn\">more_itertools</span> <span class=\"kn\">import</span>
  <span class=\"n\">flatten</span>\n\n        <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \           <span class=\"k\">for</span> <span class=\"n\">tag</span><span class=\"p\">,</span>
  <span class=\"n\">count</span> <span class=\"ow\">in</span> <span class=\"n\">Counter</span><span
  class=\"p\">(</span>\n                <span class=\"nb\">list</span><span class=\"p\">(</span><span
  class=\"n\">flatten</span><span class=\"p\">([</span><span class=\"n\">a</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;tags&quot;</span><span class=\"p\">]</span>
  <span class=\"k\">for</span> <span class=\"n\">a</span> <span class=\"ow\">in</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">articles</span><span class=\"p\">]))</span>\n
  \           <span class=\"p\">)</span><span class=\"o\">.</span><span class=\"n\">most_common</span><span
  class=\"p\">():</span>\n                <span class=\"n\">grid</span><span class=\"o\">.</span><span
  class=\"n\">add_row</span><span class=\"p\">(</span><span class=\"sa\">f</span><span
  class=\"s1\">&#39;</span><span class=\"si\">{</span><span class=\"n\">count</span><span
  class=\"si\">}</span><span class=\"s1\"> </span><span class=\"si\">{</span><span
  class=\"s2\">&quot; &quot;</span><span class=\"o\">*</span><span class=\"p\">(</span><span
  class=\"mi\">3</span><span class=\"o\">-</span><span class=\"nb\">len</span><span
  class=\"p\">(</span><span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"n\">count</span><span class=\"p\">)))</span><span class=\"si\">}</span><span
  class=\"s1\"> </span><span class=\"si\">{</span><span class=\"n\">tag</span><span
  class=\"si\">}</span><span class=\"s1\">&#39;</span><span class=\"p\">)</span>\n
  \       <span class=\"k\">except</span> <span class=\"ne\">KeyError</span><span
  class=\"p\">:</span>\n            <span class=\"o\">...</span>\n\n        <span
  class=\"k\">try</span><span class=\"p\">:</span>\n            <span class=\"n\">grid</span><span
  class=\"o\">.</span><span class=\"n\">add_row</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;[bold gold1]Series[/]&quot;</span><span class=\"p\">)</span>\n
  \           <span class=\"k\">for</span> <span class=\"n\">series</span><span class=\"p\">,</span>
  <span class=\"n\">count</span> <span class=\"ow\">in</span> <span class=\"n\">Counter</span><span
  class=\"p\">(</span>\n                <span class=\"p\">[</span><span class=\"n\">a</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;templateKey&quot;</span><span class=\"p\">]</span>
  <span class=\"k\">for</span> <span class=\"n\">a</span> <span class=\"ow\">in</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">articles</span><span class=\"p\">]</span>\n
  \           <span class=\"p\">)</span><span class=\"o\">.</span><span class=\"n\">most_common</span><span
  class=\"p\">():</span>\n                <span class=\"n\">grid</span><span class=\"o\">.</span><span
  class=\"n\">add_row</span><span class=\"p\">(</span><span class=\"sa\">f</span><span
  class=\"s1\">&#39;</span><span class=\"si\">{</span><span class=\"n\">count</span><span
  class=\"si\">}</span><span class=\"s1\"> </span><span class=\"si\">{</span><span
  class=\"s2\">&quot; &quot;</span><span class=\"o\">*</span><span class=\"p\">(</span><span
  class=\"mi\">3</span><span class=\"o\">-</span><span class=\"nb\">len</span><span
  class=\"p\">(</span><span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"n\">count</span><span class=\"p\">)))</span><span class=\"si\">}</span><span
  class=\"s1\"> </span><span class=\"si\">{</span><span class=\"n\">series</span><span
  class=\"si\">}</span><span class=\"s1\">&#39;</span><span class=\"p\">)</span>\n
  \       <span class=\"k\">except</span> <span class=\"ne\">KeyError</span><span
  class=\"p\">:</span>\n            <span class=\"o\">...</span>\n        <span class=\"k\">if</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">simple</span><span
  class=\"p\">:</span>\n            <span class=\"k\">return</span> <span class=\"n\">grid</span>\n
  \       <span class=\"k\">else</span><span class=\"p\">:</span>\n            <span
  class=\"k\">return</span> <span class=\"n\">Panel</span><span class=\"p\">(</span><span
  class=\"n\">grid</span><span class=\"p\">,</span> <span class=\"n\">title</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;[gold1]summary[/]&quot;</span><span
  class=\"p\">,</span> <span class=\"n\">border_style</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;magenta&quot;</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for summary
long_description: ''
now: 2022-02-05 19:38:00.891466
path: summary.md
slug: markata/cli/summary
status: published
title: summary.py
today: 2022-02-05
---

---

## Summary `class`

None

??? "Summary source"
    ``` python
    class Summary:
        def __init__(self, m: "Markata", simple: bool = False) -> None:
            self.m = m
            self.simple = simple

        def __rich__(self) -> Union[Panel, Table]:
            grid = Table.grid(expand=True)
            grid.add_row(f"[bright_blue]{len(self.m.articles)}[/] articles")
            grid.add_row(
                f"[green]{len([a for a in self.m.articles if a['status'] =='published'])}[/] published"
            )
            grid.add_row(
                f"[gold1]{len([a for a in self.m.articles if a['status'] =='draft'])}[/] drafts"
            )
            grid.add_row("")
            grid.add_row("[bold gold1]TAGS[/]")
            from collections import Counter

            from more_itertools import flatten

            try:
                for tag, count in Counter(
                    list(flatten([a["tags"] for a in self.m.articles]))
                ).most_common():
                    grid.add_row(f'{count} {" "*(3-len(str(count)))} {tag}')
            except KeyError:
                ...

            try:
                grid.add_row("[bold gold1]Series[/]")
                for series, count in Counter(
                    [a["templateKey"] for a in self.m.articles]
                ).most_common():
                    grid.add_row(f'{count} {" "*(3-len(str(count)))} {series}')
            except KeyError:
                ...
            if self.simple:
                return grid
            else:
                return Panel(grid, title="[gold1]summary[/]", border_style="magenta")
    ```


---

## __init__ `method`

None

??? "__init__ source"
    ``` python
    def __init__(self, m: "Markata", simple: bool = False) -> None:
            self.m = m
            self.simple = simple
    ```


---

## __rich__ `method`

None

??? "__rich__ source"
    ``` python
    def __rich__(self) -> Union[Panel, Table]:
            grid = Table.grid(expand=True)
            grid.add_row(f"[bright_blue]{len(self.m.articles)}[/] articles")
            grid.add_row(
                f"[green]{len([a for a in self.m.articles if a['status'] =='published'])}[/] published"
            )
            grid.add_row(
                f"[gold1]{len([a for a in self.m.articles if a['status'] =='draft'])}[/] drafts"
            )
            grid.add_row("")
            grid.add_row("[bold gold1]TAGS[/]")
            from collections import Counter

            from more_itertools import flatten

            try:
                for tag, count in Counter(
                    list(flatten([a["tags"] for a in self.m.articles]))
                ).most_common():
                    grid.add_row(f'{count} {" "*(3-len(str(count)))} {tag}')
            except KeyError:
                ...

            try:
                grid.add_row("[bold gold1]Series[/]")
                for series, count in Counter(
                    [a["templateKey"] for a in self.m.articles]
                ).most_common():
                    grid.add_row(f'{count} {" "*(3-len(str(count)))} {series}')
            except KeyError:
                ...
            if self.simple:
                return grid
            else:
                return Panel(grid, title="[gold1]summary[/]", border_style="magenta")
    ```