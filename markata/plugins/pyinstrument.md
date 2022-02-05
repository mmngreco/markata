---
article_html: "<p>Markata plugin to create a pyinstrument profile if pyinstrument
  is installed.</p>\n<p>The profile will be saved to <output_dir>/_profile/index.html</p>\n<hr
  />\n<h2 id=\"markatainstrument-class\">MarkataInstrument <code>class</code></h2>\n<p>None</p>\n<details>\n<summary>MarkataInstrument
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span>
  <span class=\"nc\">MarkataInstrument</span><span class=\"p\">(</span><span class=\"n\">Markata</span><span
  class=\"p\">):</span>\n    <span class=\"n\">should_profile</span> <span class=\"o\">=</span>
  <span class=\"kc\">False</span>\n    <span class=\"n\">profiler</span> <span class=\"o\">=</span>
  <span class=\"kc\">None</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"configure-function\">configure
  <code>function</code></h2>\n<p>set the should_profile variable</p>\n<details>\n<summary>configure
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">configure</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"n\">MarkataInstrument</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"s2\">&quot;set the should_profile variable&quot;</span>\n\n    <span
  class=\"k\">if</span> <span class=\"s2\">&quot;should_profile&quot;</span> <span
  class=\"ow\">not</span> <span class=\"ow\">in</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"vm\">__dict__</span><span class=\"o\">.</span><span
  class=\"n\">keys</span><span class=\"p\">():</span>\n        <span class=\"k\">try</span><span
  class=\"p\">:</span>\n            <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">should_profile</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;pyinstrument&quot;</span><span class=\"p\">][</span><span class=\"s2\">&quot;should_profile&quot;</span><span
  class=\"p\">]</span>\n        <span class=\"k\">except</span> <span class=\"ne\">KeyError</span><span
  class=\"p\">:</span>\n            <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">should_profile</span> <span class=\"o\">=</span> <span class=\"kc\">False</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"glob-function\">glob <code>function</code></h2>\n<p>start the profiler
  as soon as possible</p>\n<details>\n<summary>glob source</summary>\n<div class=\"highlight\"><pre><span></span><code><span
  class=\"k\">def</span> <span class=\"nf\">glob</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"p\">:</span> <span class=\"n\">MarkataInstrument</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n    <span class=\"s2\">&quot;start the profiler as soon as
  possible&quot;</span>\n    <span class=\"k\">if</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">should_profile</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">try</span><span class=\"p\">:</span>\n            <span
  class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">profiler</span>
  <span class=\"o\">=</span> <span class=\"n\">Profiler</span><span class=\"p\">()</span>\n
  \           <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">profiler</span><span
  class=\"o\">.</span><span class=\"n\">start</span><span class=\"p\">()</span>\n
  \       <span class=\"k\">except</span> <span class=\"ne\">NameError</span><span
  class=\"p\">:</span>\n            <span class=\"s2\">&quot;ignore if Profiler does
  not exist&quot;</span>\n            <span class=\"o\">...</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"save-function\">save <code>function</code></h2>\n<p>stop the profiler
  and save as late as possible</p>\n<details>\n<summary>save source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">save</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"p\">:</span> <span
  class=\"n\">MarkataInstrument</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n    <span class=\"s2\">&quot;stop
  the profiler and save as late as possible&quot;</span>\n    <span class=\"k\">if</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">should_profile</span><span
  class=\"p\">:</span>\n        <span class=\"k\">try</span><span class=\"p\">:</span>\n\n
  \           <span class=\"k\">if</span> <span class=\"s2\">&quot;profiler&quot;</span>
  <span class=\"ow\">in</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"vm\">__dict__</span><span class=\"o\">.</span><span class=\"n\">keys</span><span
  class=\"p\">():</span>\n                <span class=\"n\">output_file</span> <span
  class=\"o\">=</span> <span class=\"p\">(</span>\n                    <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;output_dir&quot;</span><span
  class=\"p\">])</span> <span class=\"o\">/</span> <span class=\"s2\">&quot;_profile&quot;</span>
  <span class=\"o\">/</span> <span class=\"s2\">&quot;index.html&quot;</span>\n                <span
  class=\"p\">)</span>\n                <span class=\"n\">output_file</span><span
  class=\"o\">.</span><span class=\"n\">parent</span><span class=\"o\">.</span><span
  class=\"n\">mkdir</span><span class=\"p\">(</span><span class=\"n\">parents</span><span
  class=\"o\">=</span><span class=\"kc\">True</span><span class=\"p\">,</span> <span
  class=\"n\">exist_ok</span><span class=\"o\">=</span><span class=\"kc\">True</span><span
  class=\"p\">)</span>\n                <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">profiler</span><span class=\"o\">.</span><span class=\"n\">stop</span><span
  class=\"p\">()</span>\n                <span class=\"n\">html</span> <span class=\"o\">=</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">profiler</span><span
  class=\"o\">.</span><span class=\"n\">output_html</span><span class=\"p\">()</span>\n
  \               <span class=\"n\">output_file</span><span class=\"o\">.</span><span
  class=\"n\">write_text</span><span class=\"p\">(</span><span class=\"n\">html</span><span
  class=\"p\">)</span>\n                <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">console</span><span class=\"o\">.</span><span class=\"n\">print</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">profiler</span><span class=\"o\">.</span><span class=\"n\">output_text</span><span
  class=\"p\">())</span>\n\n        <span class=\"k\">except</span> <span class=\"ne\">AttributeError</span><span
  class=\"p\">:</span>\n            <span class=\"s2\">&quot;ignore if markata does
  not have a profiler attribute&quot;</span>\n            <span class=\"o\">...</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for pyinstrument
long_description: ''
now: 2022-02-05 19:38:00.891396
path: pyinstrument.md
slug: markata/plugins/pyinstrument
status: published
title: pyinstrument.py
today: 2022-02-05
---

Markata plugin to create a pyinstrument profile if pyinstrument is installed.

The profile will be saved to <output_dir>/_profile/index.html


---

## MarkataInstrument `class`

None

??? "MarkataInstrument source"
    ``` python
    class MarkataInstrument(Markata):
        should_profile = False
        profiler = None
    ```


---

## configure `function`

set the should_profile variable

??? "configure source"
    ``` python
    def configure(markata: MarkataInstrument) -> None:
        "set the should_profile variable"

        if "should_profile" not in markata.__dict__.keys():
            try:
                markata.should_profile = markata.config["pyinstrument"]["should_profile"]
            except KeyError:
                markata.should_profile = False
    ```


---

## glob `function`

start the profiler as soon as possible

??? "glob source"
    ``` python
    def glob(markata: MarkataInstrument) -> None:
        "start the profiler as soon as possible"
        if markata.should_profile:
            try:
                markata.profiler = Profiler()
                markata.profiler.start()
            except NameError:
                "ignore if Profiler does not exist"
                ...
    ```


---

## save `function`

stop the profiler and save as late as possible

??? "save source"
    ``` python
    def save(markata: MarkataInstrument) -> None:
        "stop the profiler and save as late as possible"
        if markata.should_profile:
            try:

                if "profiler" in markata.__dict__.keys():
                    output_file = (
                        Path(markata.config["output_dir"]) / "_profile" / "index.html"
                    )
                    output_file.parent.mkdir(parents=True, exist_ok=True)
                    markata.profiler.stop()
                    html = markata.profiler.output_html()
                    output_file.write_text(html)
                    markata.console.print(markata.profiler.output_text())

            except AttributeError:
                "ignore if markata does not have a profiler attribute"
                ...
    ```