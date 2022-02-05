---
article_html: "<p>Default datetime plugin</p>\n<hr />\n<h2 id=\"load-function\">load
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>load source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">load</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"p\">:</span> <span
  class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n    <span class=\"k\">for</span>
  <span class=\"n\">article</span> <span class=\"ow\">in</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">iter_articles</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;datetime&quot;</span><span class=\"p\">):</span>\n\n        <span
  class=\"k\">try</span><span class=\"p\">:</span>\n            <span class=\"n\">date</span>
  <span class=\"o\">=</span> <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">[</span><span class=\"s2\">&quot;date&quot;</span><span
  class=\"p\">]</span>\n        <span class=\"k\">except</span> <span class=\"ne\">KeyError</span><span
  class=\"p\">:</span>\n            <span class=\"n\">date</span> <span class=\"o\">=</span>
  <span class=\"kc\">None</span>\n        <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span
  class=\"p\">(</span><span class=\"n\">date</span><span class=\"p\">,</span> <span
  class=\"nb\">str</span><span class=\"p\">):</span>\n            <span class=\"n\">date</span>
  <span class=\"o\">=</span> <span class=\"n\">dateutil</span><span class=\"o\">.</span><span
  class=\"n\">parser</span><span class=\"o\">.</span><span class=\"n\">parse</span><span
  class=\"p\">(</span><span class=\"n\">date</span><span class=\"p\">)</span>\n        <span
  class=\"k\">if</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"n\">date</span><span class=\"p\">,</span> <span class=\"n\">datetime</span><span
  class=\"o\">.</span><span class=\"n\">date</span><span class=\"p\">):</span>\n            <span
  class=\"n\">date</span> <span class=\"o\">=</span> <span class=\"n\">datetime</span><span
  class=\"o\">.</span><span class=\"n\">datetime</span><span class=\"p\">(</span>\n
  \               <span class=\"n\">year</span><span class=\"o\">=</span><span class=\"n\">date</span><span
  class=\"o\">.</span><span class=\"n\">year</span><span class=\"p\">,</span>\n                <span
  class=\"n\">month</span><span class=\"o\">=</span><span class=\"n\">date</span><span
  class=\"o\">.</span><span class=\"n\">month</span><span class=\"p\">,</span>\n                <span
  class=\"n\">day</span><span class=\"o\">=</span><span class=\"n\">date</span><span
  class=\"o\">.</span><span class=\"n\">day</span><span class=\"p\">,</span>\n                <span
  class=\"n\">tzinfo</span><span class=\"o\">=</span><span class=\"n\">pytz</span><span
  class=\"o\">.</span><span class=\"n\">utc</span><span class=\"p\">,</span>\n            <span
  class=\"p\">)</span>\n\n        <span class=\"n\">article</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;today&quot;</span><span class=\"p\">]</span> <span class=\"o\">=</span>
  <span class=\"n\">datetime</span><span class=\"o\">.</span><span class=\"n\">date</span><span
  class=\"o\">.</span><span class=\"n\">today</span><span class=\"p\">()</span>\n
  \       <span class=\"n\">article</span><span class=\"p\">[</span><span class=\"s2\">&quot;now&quot;</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"n\">datetime</span><span
  class=\"o\">.</span><span class=\"n\">datetime</span><span class=\"o\">.</span><span
  class=\"n\">now</span><span class=\"p\">()</span>\n        <span class=\"n\">article</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;datetime&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"n\">date</span>\n        <span class=\"k\">if</span>
  <span class=\"n\">date</span> <span class=\"ow\">is</span> <span class=\"ow\">not</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n            <span class=\"n\">article</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;date&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"n\">date</span><span class=\"o\">.</span><span
  class=\"n\">date</span><span class=\"p\">()</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for datetime
long_description: ''
now: 2022-02-05 19:38:00.891437
path: datetime.md
slug: markata/plugins/datetime
status: published
title: datetime.py
today: 2022-02-05
---

Default datetime plugin


---

## load `function`

None

??? "load source"
    ``` python
    def load(markata: "Markata") -> None:
        for article in markata.iter_articles("datetime"):

            try:
                date = article.metadata["date"]
            except KeyError:
                date = None
            if isinstance(date, str):
                date = dateutil.parser.parse(date)
            if isinstance(date, datetime.date):
                date = datetime.datetime(
                    year=date.year,
                    month=date.month,
                    day=date.day,
                    tzinfo=pytz.utc,
                )

            article["today"] = datetime.date.today()
            article["now"] = datetime.datetime.now()
            article["datetime"] = date
            if date is not None:
                article["date"] = date.date()
    ```