---
article_html: "<hr />\n<h2 id=\"runner-class\">Runner <code>class</code></h2>\n<p>Display
  Footer</p>\n<details>\n<summary>Runner source</summary>\n<div class=\"highlight\"><pre><span></span><code><span
  class=\"k\">class</span> <span class=\"nc\">Runner</span><span class=\"p\">:</span>\n
  \   <span class=\"sd\">&quot;&quot;&quot;Display Footer&quot;&quot;&quot;</span>\n\n
  \   <span class=\"n\">_status</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;waiting&quot;</span>\n\n
  \   <span class=\"n\">_dirhash</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;&quot;</span>\n
  \   <span class=\"n\">time</span> <span class=\"o\">=</span> <span class=\"n\">time</span><span
  class=\"o\">.</span><span class=\"n\">time</span><span class=\"p\">()</span>\n\n
  \   <span class=\"k\">def</span> <span class=\"fm\">__init__</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">,</span> <span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">m</span>
  <span class=\"o\">=</span> <span class=\"n\">markata</span>\n\n    <span class=\"k\">def</span>
  <span class=\"nf\">run</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">status</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;running&quot;</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">run</span><span class=\"p\">()</span>\n        <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">time</span>
  <span class=\"o\">=</span> <span class=\"n\">time</span><span class=\"o\">.</span><span
  class=\"n\">time</span><span class=\"p\">()</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">status</span> <span class=\"o\">=</span> <span
  class=\"s2\">&quot;waiting&quot;</span>\n\n    <span class=\"k\">def</span> <span
  class=\"nf\">__rich__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Panel</span><span
  class=\"p\">:</span>\n\n        <span class=\"k\">if</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_dirhash</span> <span class=\"o\">!=</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">content_dir_hash</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">run</span><span
  class=\"p\">()</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_dirhash</span> <span class=\"o\">=</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">content_dir_hash</span>\n\n
  \       <span class=\"n\">s</span> <span class=\"o\">=</span> <span class=\"sa\">f</span><span
  class=\"s2\">&quot;runner is waiting </span><span class=\"si\">{</span><span class=\"nb\">round</span><span
  class=\"p\">(</span><span class=\"n\">time</span><span class=\"o\">.</span><span
  class=\"n\">time</span><span class=\"p\">()</span> <span class=\"o\">-</span> <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">time</span><span
  class=\"p\">)</span><span class=\"si\">}</span><span class=\"s2\">&quot;</span>\n\n
  \       <span class=\"k\">return</span> <span class=\"n\">Panel</span><span class=\"p\">(</span><span
  class=\"n\">Text</span><span class=\"p\">(</span><span class=\"n\">s</span><span
  class=\"p\">),</span> <span class=\"n\">border_style</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;green&quot;</span><span class=\"p\">,</span> <span class=\"n\">title</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;runner&quot;</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"init-method\"><strong>init</strong> <code>method</code></h2>\n<p>None</p>\n<details>\n<summary><strong>init</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"fm\">__init__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">markata</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">m</span> <span class=\"o\">=</span> <span
  class=\"n\">markata</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"run-method\">run
  <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>run source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">run</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">status</span>
  <span class=\"o\">=</span> <span class=\"s2\">&quot;running&quot;</span>\n        <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">run</span><span class=\"p\">()</span>\n        <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">time</span>
  <span class=\"o\">=</span> <span class=\"n\">time</span><span class=\"o\">.</span><span
  class=\"n\">time</span><span class=\"p\">()</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">status</span> <span class=\"o\">=</span> <span
  class=\"s2\">&quot;waiting&quot;</span>\n</code></pre></div>\n</details>\n<hr />\n<h2
  id=\"rich-method\"><strong>rich</strong> <code>method</code></h2>\n<p>None</p>\n<details>\n<summary><strong>rich</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">__rich__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Panel</span><span
  class=\"p\">:</span>\n\n        <span class=\"k\">if</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_dirhash</span> <span class=\"o\">!=</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">content_dir_hash</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">run</span><span
  class=\"p\">()</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_dirhash</span> <span class=\"o\">=</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">content_dir_hash</span>\n\n
  \       <span class=\"n\">s</span> <span class=\"o\">=</span> <span class=\"sa\">f</span><span
  class=\"s2\">&quot;runner is waiting </span><span class=\"si\">{</span><span class=\"nb\">round</span><span
  class=\"p\">(</span><span class=\"n\">time</span><span class=\"o\">.</span><span
  class=\"n\">time</span><span class=\"p\">()</span> <span class=\"o\">-</span> <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">time</span><span
  class=\"p\">)</span><span class=\"si\">}</span><span class=\"s2\">&quot;</span>\n\n
  \       <span class=\"k\">return</span> <span class=\"n\">Panel</span><span class=\"p\">(</span><span
  class=\"n\">Text</span><span class=\"p\">(</span><span class=\"n\">s</span><span
  class=\"p\">),</span> <span class=\"n\">border_style</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;green&quot;</span><span class=\"p\">,</span> <span class=\"n\">title</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;runner&quot;</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for runner
long_description: ''
now: 2022-02-05 19:38:00.891456
path: runner.md
slug: markata/cli/runner
status: published
title: runner.py
today: 2022-02-05
---

---

## Runner `class`

Display Footer

??? "Runner source"
    ``` python
    class Runner:
        """Display Footer"""

        _status = "waiting"

        _dirhash = ""
        time = time.time()

        def __init__(self, markata: "Markata") -> None:
            self.m = markata

        def run(self) -> None:
            self.status = "running"
            self.m.run()
            self.time = time.time()
            self.status = "waiting"

        def __rich__(self) -> Panel:

            if self._dirhash != self.m.content_dir_hash:
                self.run()
                self._dirhash = self.m.content_dir_hash

            s = f"runner is waiting {round(time.time() - self.time)}"

            return Panel(Text(s), border_style="green", title="runner")
    ```


---

## __init__ `method`

None

??? "__init__ source"
    ``` python
    def __init__(self, markata: "Markata") -> None:
            self.m = markata
    ```


---

## run `method`

None

??? "run source"
    ``` python
    def run(self) -> None:
            self.status = "running"
            self.m.run()
            self.time = time.time()
            self.status = "waiting"
    ```


---

## __rich__ `method`

None

??? "__rich__ source"
    ``` python
    def __rich__(self) -> Panel:

            if self._dirhash != self.m.content_dir_hash:
                self.run()
                self._dirhash = self.m.content_dir_hash

            s = f"runner is waiting {round(time.time() - self.time)}"

            return Panel(Text(s), border_style="green", title="runner")
    ```