---
article_html: "<hr />\n<h2 id=\"save-function\">save <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>save
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">save</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">output_file</span> <span class=\"o\">=</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;output_dir&quot;</span><span
  class=\"p\">])</span> <span class=\"o\">/</span> <span class=\"s2\">&quot;markata.json&quot;</span>\n
  \   <span class=\"n\">output_file</span><span class=\"o\">.</span><span class=\"n\">parent</span><span
  class=\"o\">.</span><span class=\"n\">mkdir</span><span class=\"p\">(</span><span
  class=\"n\">parents</span><span class=\"o\">=</span><span class=\"kc\">True</span><span
  class=\"p\">,</span> <span class=\"n\">exist_ok</span><span class=\"o\">=</span><span
  class=\"kc\">True</span><span class=\"p\">)</span>\n    <span class=\"n\">output_file</span><span
  class=\"o\">.</span><span class=\"n\">write_text</span><span class=\"p\">(</span><span
  class=\"n\">json</span><span class=\"o\">.</span><span class=\"n\">dumps</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">to_dict</span><span class=\"p\">(),</span> <span class=\"n\">default</span><span
  class=\"o\">=</span><span class=\"nb\">str</span><span class=\"p\">))</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for to_json
long_description: ''
now: 2022-02-05 19:38:00.891388
path: to_json.md
slug: markata/plugins/to_json
status: published
title: to_json.py
today: 2022-02-05
---

---

## save `function`

None

??? "save source"
    ``` python
    def save(markata: "Markata") -> None:
        output_file = Path(markata.config["output_dir"]) / "markata.json"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(json.dumps(markata.to_dict(), default=str))
    ```