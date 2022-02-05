---
article_html: "<p>manifest plugin</p>\n<hr />\n<h2 id=\"_create_seo-function\">_create_seo
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>_create_seo source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">_create_seo</span><span
  class=\"p\">(</span>\n    <span class=\"n\">markata</span><span class=\"p\">:</span>
  <span class=\"n\">Markata</span><span class=\"p\">,</span>\n    <span class=\"n\">soup</span><span
  class=\"p\">:</span> <span class=\"n\">BeautifulSoup</span><span class=\"p\">,</span>\n
  \   <span class=\"n\">article</span><span class=\"p\">:</span> <span class=\"s2\">&quot;frontmatter.Post&quot;</span><span
  class=\"p\">,</span>\n    <span class=\"n\">site_name</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span><span class=\"p\">,</span>\n    <span class=\"n\">author_name</span><span
  class=\"p\">:</span> <span class=\"nb\">str</span><span class=\"p\">,</span>\n    <span
  class=\"n\">author_email</span><span class=\"p\">:</span> <span class=\"nb\">str</span><span
  class=\"p\">,</span>\n    <span class=\"n\">twitter_card</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span><span class=\"p\">,</span>\n    <span class=\"n\">twitter_creator</span><span
  class=\"p\">:</span> <span class=\"nb\">str</span><span class=\"p\">,</span>\n    <span
  class=\"n\">config_seo</span><span class=\"p\">:</span> <span class=\"n\">Dict</span><span
  class=\"p\">,</span>\n    <span class=\"n\">images_url</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span><span class=\"p\">,</span>\n<span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"n\">List</span><span class=\"p\">:</span>\n
  \   <span class=\"k\">if</span> <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">[</span><span class=\"s2\">&quot;description&quot;</span><span
  class=\"p\">]</span> <span class=\"o\">==</span> <span class=\"s2\">&quot;&quot;</span>
  <span class=\"ow\">or</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">try</span><span class=\"p\">:</span>\n            <span
  class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">metadata</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;description&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"s2\">&quot; &quot;</span><span class=\"o\">.</span><span
  class=\"n\">join</span><span class=\"p\">(</span>\n                <span class=\"p\">[</span><span
  class=\"n\">p</span><span class=\"o\">.</span><span class=\"n\">text</span> <span
  class=\"k\">for</span> <span class=\"n\">p</span> <span class=\"ow\">in</span> <span
  class=\"n\">soup</span><span class=\"o\">.</span><span class=\"n\">find</span><span
  class=\"p\">(</span><span class=\"nb\">id</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;post-body&quot;</span><span class=\"p\">)</span><span class=\"o\">.</span><span
  class=\"n\">find_all</span><span class=\"p\">(</span><span class=\"s2\">&quot;p&quot;</span><span
  class=\"p\">)]</span>\n            <span class=\"p\">)</span><span class=\"o\">.</span><span
  class=\"n\">strip</span><span class=\"p\">()[:</span><span class=\"mi\">120</span><span
  class=\"p\">]</span>\n        <span class=\"k\">except</span> <span class=\"ne\">AttributeError</span><span
  class=\"p\">:</span>\n            <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">[</span><span class=\"s2\">&quot;description&quot;</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;&quot;</span>\n\n
  \   <span class=\"n\">seo</span> <span class=\"o\">=</span> <span class=\"p\">[</span>\n
  \       <span class=\"o\">*</span><span class=\"n\">config_seo</span><span class=\"p\">,</span>\n
  \       <span class=\"p\">{</span>\n            <span class=\"s2\">&quot;name&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;og:author&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;property&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;og:author&quot;</span><span class=\"p\">,</span>\n            <span
  class=\"s2\">&quot;content&quot;</span><span class=\"p\">:</span> <span class=\"n\">author_name</span><span
  class=\"p\">,</span>\n        <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n
  \           <span class=\"s2\">&quot;name&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;og:author_email&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;property&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;og:author_email&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;content&quot;</span><span class=\"p\">:</span>
  <span class=\"n\">author_email</span><span class=\"p\">,</span>\n        <span class=\"p\">},</span>\n
  \       <span class=\"p\">{</span>\n            <span class=\"s2\">&quot;name&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;og:type&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;property&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;og:type&quot;</span><span class=\"p\">,</span>\n            <span
  class=\"s2\">&quot;content&quot;</span><span class=\"p\">:</span> <span class=\"s2\">&quot;website&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n
  \           <span class=\"s2\">&quot;name&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;description&quot;</span><span class=\"p\">,</span>\n            <span
  class=\"s2\">&quot;property&quot;</span><span class=\"p\">:</span> <span class=\"s2\">&quot;description&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;content&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">[</span><span class=\"s2\">&quot;description&quot;</span><span
  class=\"p\">],</span>\n        <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n
  \           <span class=\"s2\">&quot;name&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;og:description&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;property&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;og:description&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;content&quot;</span><span class=\"p\">:</span>
  <span class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">metadata</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;description&quot;</span><span class=\"p\">],</span>\n
  \       <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n            <span
  class=\"s2\">&quot;name&quot;</span><span class=\"p\">:</span> <span class=\"s2\">&quot;twitter:description&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;property&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;twitter:description&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;content&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">[</span><span class=\"s2\">&quot;description&quot;</span><span
  class=\"p\">],</span>\n        <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n
  \           <span class=\"s2\">&quot;name&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;og:title&quot;</span><span class=\"p\">,</span>\n            <span
  class=\"s2\">&quot;property&quot;</span><span class=\"p\">:</span> <span class=\"s2\">&quot;og:title&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;content&quot;</span><span
  class=\"p\">:</span> <span class=\"sa\">f</span><span class=\"s1\">&#39;</span><span
  class=\"si\">{</span><span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">[</span><span class=\"s2\">&quot;title&quot;</span><span
  class=\"p\">]</span><span class=\"si\">}</span><span class=\"s1\"> | </span><span
  class=\"si\">{</span><span class=\"n\">site_name</span><span class=\"si\">}</span><span
  class=\"s1\">&#39;</span><span class=\"p\">[:</span><span class=\"mi\">60</span><span
  class=\"p\">],</span>\n        <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n
  \           <span class=\"s2\">&quot;name&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;twitter:title&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;property&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;twitter:title&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;content&quot;</span><span class=\"p\">:</span>
  <span class=\"sa\">f</span><span class=\"s1\">&#39;</span><span class=\"si\">{</span><span
  class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">metadata</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;title&quot;</span><span class=\"p\">]</span><span
  class=\"si\">}</span><span class=\"s1\"> | </span><span class=\"si\">{</span><span
  class=\"n\">site_name</span><span class=\"si\">}</span><span class=\"s1\">&#39;</span><span
  class=\"p\">[:</span><span class=\"mi\">60</span><span class=\"p\">],</span>\n        <span
  class=\"p\">},</span>\n        <span class=\"p\">{</span>\n            <span class=\"s2\">&quot;name&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;og:image&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;property&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;og:image&quot;</span><span class=\"p\">,</span>\n            <span
  class=\"s2\">&quot;content&quot;</span><span class=\"p\">:</span> <span class=\"sa\">f</span><span
  class=\"s1\">&#39;</span><span class=\"si\">{</span><span class=\"n\">images_url</span><span
  class=\"si\">}</span><span class=\"s1\">/</span><span class=\"si\">{</span><span
  class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">metadata</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;slug&quot;</span><span class=\"p\">]</span><span
  class=\"si\">}</span><span class=\"s1\">-og.png&#39;</span><span class=\"p\">,</span>\n
  \       <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n            <span
  class=\"s2\">&quot;name&quot;</span><span class=\"p\">:</span> <span class=\"s2\">&quot;twitter:image&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;property&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;twitter:image&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;content&quot;</span><span class=\"p\">:</span>
  <span class=\"sa\">f</span><span class=\"s1\">&#39;</span><span class=\"si\">{</span><span
  class=\"n\">images_url</span><span class=\"si\">}</span><span class=\"s1\">/</span><span
  class=\"si\">{</span><span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">[</span><span class=\"s2\">&quot;slug&quot;</span><span
  class=\"p\">]</span><span class=\"si\">}</span><span class=\"s1\">-og.png&#39;</span><span
  class=\"p\">,</span>\n        <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n
  \           <span class=\"s2\">&quot;name&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;og:image:width&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;property&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;og:image:width&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;content&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;1600&quot;</span><span class=\"p\">,</span>\n        <span
  class=\"p\">},</span>\n        <span class=\"p\">{</span>\n            <span class=\"s2\">&quot;name&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;og:image:width&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;property&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;og:image:width&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;content&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;900&quot;</span><span class=\"p\">,</span>\n        <span
  class=\"p\">},</span>\n        <span class=\"p\">{</span>\n            <span class=\"s2\">&quot;name&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;twitter:card&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;property&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;twitter:card&quot;</span><span class=\"p\">,</span>\n            <span
  class=\"s2\">&quot;content&quot;</span><span class=\"p\">:</span> <span class=\"n\">twitter_card</span><span
  class=\"p\">,</span>\n        <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n
  \           <span class=\"s2\">&quot;name&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;og:site_name&quot;</span><span class=\"p\">,</span>\n            <span
  class=\"s2\">&quot;property&quot;</span><span class=\"p\">:</span> <span class=\"s2\">&quot;og:site_name&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;content&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">site_name</span><span class=\"p\">,</span>\n
  \       <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n            <span
  class=\"s2\">&quot;name&quot;</span><span class=\"p\">:</span> <span class=\"s2\">&quot;twitter:creator&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;property&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;twitter:creator&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;content&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">twitter_creator</span><span class=\"p\">,</span>\n
  \       <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n            <span
  class=\"s2\">&quot;name&quot;</span><span class=\"p\">:</span> <span class=\"s2\">&quot;title&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;property&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;title&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;content&quot;</span><span class=\"p\">:</span>
  <span class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">metadata</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;title&quot;</span><span class=\"p\">],</span>\n
  \       <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n            <span
  class=\"s2\">&quot;name&quot;</span><span class=\"p\">:</span> <span class=\"s2\">&quot;generator&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;property&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;generator&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;content&quot;</span><span class=\"p\">:</span>
  <span class=\"sa\">f</span><span class=\"s2\">&quot;markata </span><span class=\"si\">{</span><span
  class=\"n\">__version__</span><span class=\"si\">}</span><span class=\"s2\">&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"p\">},</span>\n    <span class=\"p\">]</span>\n
  \   <span class=\"k\">return</span> <span class=\"n\">seo</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"_add_seo_tags-function\">_add_seo_tags <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>_add_seo_tags
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">_add_seo_tags</span><span class=\"p\">(</span><span class=\"n\">seo</span><span
  class=\"p\">:</span> <span class=\"n\">List</span><span class=\"p\">,</span> <span
  class=\"n\">article</span><span class=\"p\">:</span> <span class=\"s2\">&quot;frontmatter.Post&quot;</span><span
  class=\"p\">,</span> <span class=\"n\">soup</span><span class=\"p\">:</span> <span
  class=\"n\">BeautifulSoup</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n    <span class=\"k\">for</span>
  <span class=\"n\">meta</span> <span class=\"ow\">in</span> <span class=\"n\">seo</span><span
  class=\"p\">:</span>\n        <span class=\"n\">soup</span><span class=\"o\">.</span><span
  class=\"n\">head</span><span class=\"o\">.</span><span class=\"n\">append</span><span
  class=\"p\">(</span><span class=\"n\">_create_seo_tag</span><span class=\"p\">(</span><span
  class=\"n\">meta</span><span class=\"p\">,</span> <span class=\"n\">soup</span><span
  class=\"p\">))</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"_create_seo_tag-function\">_create_seo_tag
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>_create_seo_tag source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">_create_seo_tag</span><span
  class=\"p\">(</span><span class=\"n\">meta</span><span class=\"p\">:</span> <span
  class=\"nb\">dict</span><span class=\"p\">,</span> <span class=\"n\">soup</span><span
  class=\"p\">:</span> <span class=\"n\">BeautifulSoup</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"s2\">&quot;Tag&quot;</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">tag</span> <span class=\"o\">=</span> <span class=\"n\">soup</span><span
  class=\"o\">.</span><span class=\"n\">new_tag</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;meta&quot;</span><span class=\"p\">)</span>\n    <span class=\"k\">for</span>
  <span class=\"n\">k</span> <span class=\"ow\">in</span> <span class=\"n\">meta</span><span
  class=\"p\">:</span>\n        <span class=\"n\">tag</span><span class=\"o\">.</span><span
  class=\"n\">attrs</span><span class=\"p\">[</span><span class=\"n\">k</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"n\">meta</span><span
  class=\"p\">[</span><span class=\"n\">k</span><span class=\"p\">]</span>\n    <span
  class=\"k\">return</span> <span class=\"n\">tag</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"render-function\">render <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>render
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">render</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"n\">Markata</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n\n
  \   <span class=\"n\">url</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">get_config</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;url&quot;</span><span class=\"p\">)</span> <span class=\"ow\">or</span>
  <span class=\"s2\">&quot;&quot;</span>\n    <span class=\"n\">images_url</span>
  <span class=\"o\">=</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">get_config</span><span class=\"p\">(</span><span class=\"s2\">&quot;images_url&quot;</span><span
  class=\"p\">)</span> <span class=\"ow\">or</span> <span class=\"n\">url</span> <span
  class=\"ow\">or</span> <span class=\"s2\">&quot;&quot;</span>\n    <span class=\"n\">site_name</span>
  <span class=\"o\">=</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">get_config</span><span class=\"p\">(</span><span class=\"s2\">&quot;site_name&quot;</span><span
  class=\"p\">)</span> <span class=\"ow\">or</span> <span class=\"s2\">&quot;&quot;</span>\n
  \   <span class=\"n\">author_name</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">get_config</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;author_name&quot;</span><span class=\"p\">)</span> <span class=\"ow\">or</span>
  <span class=\"s2\">&quot;&quot;</span>\n    <span class=\"n\">author_email</span>
  <span class=\"o\">=</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">get_config</span><span class=\"p\">(</span><span class=\"s2\">&quot;author_email&quot;</span><span
  class=\"p\">)</span> <span class=\"ow\">or</span> <span class=\"s2\">&quot;&quot;</span>\n
  \   <span class=\"n\">twitter_creator</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">get_config</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;twitter_creator&quot;</span><span class=\"p\">)</span> <span
  class=\"ow\">or</span> <span class=\"s2\">&quot;&quot;</span>\n    <span class=\"n\">twitter_card</span>
  <span class=\"o\">=</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">get_config</span><span class=\"p\">(</span><span class=\"s2\">&quot;twitter_card&quot;</span><span
  class=\"p\">)</span> <span class=\"ow\">or</span> <span class=\"s2\">&quot;summary_large_image&quot;</span>\n
  \   <span class=\"n\">config_seo</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">get_config</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;seo&quot;</span><span class=\"p\">,</span> <span class=\"n\">warn</span><span
  class=\"o\">=</span><span class=\"kc\">False</span><span class=\"p\">)</span> <span
  class=\"ow\">or</span> <span class=\"nb\">dict</span><span class=\"p\">()</span>\n\n
  \   <span class=\"k\">with</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">cache</span> <span class=\"k\">as</span> <span class=\"n\">cache</span><span
  class=\"p\">:</span>\n        <span class=\"k\">for</span> <span class=\"n\">article</span>
  <span class=\"ow\">in</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">iter_articles</span><span class=\"p\">(</span><span class=\"s2\">&quot;add
  seo tags from seo.py&quot;</span><span class=\"p\">):</span>\n            <span
  class=\"n\">key</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">make_hash</span><span class=\"p\">(</span>\n
  \               <span class=\"s2\">&quot;seo&quot;</span><span class=\"p\">,</span>\n
  \               <span class=\"s2\">&quot;render&quot;</span><span class=\"p\">,</span>\n
  \               <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">html</span><span class=\"p\">,</span>\n                <span class=\"n\">site_name</span><span
  class=\"p\">,</span>\n                <span class=\"n\">url</span><span class=\"p\">,</span>\n
  \               <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">[</span><span class=\"s2\">&quot;slug&quot;</span><span
  class=\"p\">],</span>\n                <span class=\"n\">twitter_card</span><span
  class=\"p\">,</span>\n                <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">[</span><span class=\"s2\">&quot;title&quot;</span><span
  class=\"p\">],</span>\n                <span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"n\">config_seo</span><span class=\"p\">),</span>\n            <span class=\"p\">)</span>\n\n
  \           <span class=\"n\">html_from_cache</span> <span class=\"o\">=</span>
  <span class=\"n\">cache</span><span class=\"o\">.</span><span class=\"n\">get</span><span
  class=\"p\">(</span><span class=\"n\">key</span><span class=\"p\">)</span>\n\n            <span
  class=\"k\">if</span> <span class=\"n\">html_from_cache</span> <span class=\"ow\">is</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n                <span
  class=\"n\">soup</span> <span class=\"o\">=</span> <span class=\"n\">BeautifulSoup</span><span
  class=\"p\">(</span><span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">html</span><span class=\"p\">,</span> <span class=\"n\">features</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;lxml&quot;</span><span class=\"p\">)</span>\n
  \               <span class=\"n\">seo</span> <span class=\"o\">=</span> <span class=\"n\">_create_seo</span><span
  class=\"p\">(</span>\n                    <span class=\"n\">markata</span><span
  class=\"o\">=</span><span class=\"n\">markata</span><span class=\"p\">,</span>\n
  \                   <span class=\"n\">soup</span><span class=\"o\">=</span><span
  class=\"n\">soup</span><span class=\"p\">,</span>\n                    <span class=\"n\">article</span><span
  class=\"o\">=</span><span class=\"n\">article</span><span class=\"p\">,</span>\n
  \                   <span class=\"n\">site_name</span><span class=\"o\">=</span><span
  class=\"n\">site_name</span><span class=\"p\">,</span>\n                    <span
  class=\"n\">author_name</span><span class=\"o\">=</span><span class=\"n\">author_name</span><span
  class=\"p\">,</span>\n                    <span class=\"n\">author_email</span><span
  class=\"o\">=</span><span class=\"n\">author_email</span><span class=\"p\">,</span>\n
  \                   <span class=\"n\">twitter_card</span><span class=\"o\">=</span><span
  class=\"n\">twitter_card</span><span class=\"p\">,</span>\n                    <span
  class=\"n\">twitter_creator</span><span class=\"o\">=</span><span class=\"n\">twitter_creator</span><span
  class=\"p\">,</span>\n                    <span class=\"n\">config_seo</span><span
  class=\"o\">=</span><span class=\"n\">config_seo</span><span class=\"p\">,</span>\n
  \                   <span class=\"n\">images_url</span><span class=\"o\">=</span><span
  class=\"n\">images_url</span><span class=\"p\">,</span>\n                <span class=\"p\">)</span>\n
  \               <span class=\"n\">_add_seo_tags</span><span class=\"p\">(</span><span
  class=\"n\">seo</span><span class=\"p\">,</span> <span class=\"n\">article</span><span
  class=\"p\">,</span> <span class=\"n\">soup</span><span class=\"p\">)</span>\n                <span
  class=\"n\">canonical_link</span> <span class=\"o\">=</span> <span class=\"n\">soup</span><span
  class=\"o\">.</span><span class=\"n\">new_tag</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;link&quot;</span><span class=\"p\">)</span>\n                <span
  class=\"n\">canonical_link</span><span class=\"o\">.</span><span class=\"n\">attrs</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;rel&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"s2\">&quot;canonical&quot;</span>\n                <span
  class=\"k\">if</span> <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">[</span><span class=\"s2\">&quot;slug&quot;</span><span
  class=\"p\">]</span> <span class=\"o\">==</span> <span class=\"s2\">&quot;index&quot;</span><span
  class=\"p\">:</span>\n                    <span class=\"n\">canonical_link</span><span
  class=\"o\">.</span><span class=\"n\">attrs</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;href&quot;</span><span class=\"p\">]</span> <span class=\"o\">=</span>
  <span class=\"sa\">f</span><span class=\"s2\">&quot;</span><span class=\"si\">{</span><span
  class=\"n\">url</span><span class=\"si\">}</span><span class=\"s2\">/&quot;</span>\n
  \               <span class=\"k\">else</span><span class=\"p\">:</span>\n                    <span
  class=\"n\">canonical_link</span><span class=\"o\">.</span><span class=\"n\">attrs</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;href&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"sa\">f</span><span class=\"s1\">&#39;</span><span
  class=\"si\">{</span><span class=\"n\">url</span><span class=\"si\">}</span><span
  class=\"s1\">/</span><span class=\"si\">{</span><span class=\"n\">article</span><span
  class=\"o\">.</span><span class=\"n\">metadata</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;slug&quot;</span><span class=\"p\">]</span><span class=\"si\">}</span><span
  class=\"s1\">/&#39;</span>\n                <span class=\"n\">soup</span><span class=\"o\">.</span><span
  class=\"n\">head</span><span class=\"o\">.</span><span class=\"n\">append</span><span
  class=\"p\">(</span><span class=\"n\">canonical_link</span><span class=\"p\">)</span>\n\n
  \               <span class=\"n\">meta_url</span> <span class=\"o\">=</span> <span
  class=\"n\">soup</span><span class=\"o\">.</span><span class=\"n\">new_tag</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;meta&quot;</span><span class=\"p\">)</span>\n
  \               <span class=\"n\">meta_url</span><span class=\"o\">.</span><span
  class=\"n\">attrs</span><span class=\"p\">[</span><span class=\"s2\">&quot;name&quot;</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;og:url&quot;</span>\n
  \               <span class=\"n\">meta_url</span><span class=\"o\">.</span><span
  class=\"n\">attrs</span><span class=\"p\">[</span><span class=\"s2\">&quot;property&quot;</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;og:url&quot;</span>\n
  \               <span class=\"k\">if</span> <span class=\"n\">article</span><span
  class=\"o\">.</span><span class=\"n\">metadata</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;slug&quot;</span><span class=\"p\">]</span> <span class=\"o\">==</span>
  <span class=\"s2\">&quot;index&quot;</span><span class=\"p\">:</span>\n                    <span
  class=\"n\">meta_url</span><span class=\"o\">.</span><span class=\"n\">attrs</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;content&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"sa\">f</span><span class=\"s2\">&quot;</span><span
  class=\"si\">{</span><span class=\"n\">url</span><span class=\"si\">}</span><span
  class=\"s2\">/&quot;</span>\n                <span class=\"k\">else</span><span
  class=\"p\">:</span>\n                    <span class=\"n\">meta_url</span><span
  class=\"o\">.</span><span class=\"n\">attrs</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;content&quot;</span><span class=\"p\">]</span> <span class=\"o\">=</span>
  <span class=\"sa\">f</span><span class=\"s1\">&#39;</span><span class=\"si\">{</span><span
  class=\"n\">url</span><span class=\"si\">}</span><span class=\"s1\">/</span><span
  class=\"si\">{</span><span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">[</span><span class=\"s2\">&quot;slug&quot;</span><span
  class=\"p\">]</span><span class=\"si\">}</span><span class=\"s1\">/&#39;</span>\n
  \               <span class=\"n\">soup</span><span class=\"o\">.</span><span class=\"n\">head</span><span
  class=\"o\">.</span><span class=\"n\">append</span><span class=\"p\">(</span><span
  class=\"n\">meta_url</span><span class=\"p\">)</span>\n\n                <span class=\"n\">html</span>
  <span class=\"o\">=</span> <span class=\"n\">soup</span><span class=\"o\">.</span><span
  class=\"n\">prettify</span><span class=\"p\">()</span>\n                <span class=\"n\">cache</span><span
  class=\"o\">.</span><span class=\"n\">add</span><span class=\"p\">(</span><span
  class=\"n\">key</span><span class=\"p\">,</span> <span class=\"n\">html</span><span
  class=\"p\">,</span> <span class=\"n\">expire</span><span class=\"o\">=</span><span
  class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;default_cache_expire&quot;</span><span
  class=\"p\">])</span>\n\n            <span class=\"k\">else</span><span class=\"p\">:</span>\n
  \               <span class=\"n\">html</span> <span class=\"o\">=</span> <span class=\"n\">html_from_cache</span>\n
  \           <span class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">html</span>
  <span class=\"o\">=</span> <span class=\"n\">html</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for seo
long_description: ''
now: 2022-02-05 19:38:00.891412
path: seo.md
slug: markata/plugins/seo
status: published
title: seo.py
today: 2022-02-05
---

manifest plugin


---

## _create_seo `function`

None

??? "_create_seo source"
    ``` python
    def _create_seo(
        markata: Markata,
        soup: BeautifulSoup,
        article: "frontmatter.Post",
        site_name: str,
        author_name: str,
        author_email: str,
        twitter_card: str,
        twitter_creator: str,
        config_seo: Dict,
        images_url: str,
    ) -> List:
        if article.metadata["description"] == "" or None:
            try:
                article.metadata["description"] = " ".join(
                    [p.text for p in soup.find(id="post-body").find_all("p")]
                ).strip()[:120]
            except AttributeError:
                article.metadata["description"] = ""

        seo = [
            *config_seo,
            {
                "name": "og:author",
                "property": "og:author",
                "content": author_name,
            },
            {
                "name": "og:author_email",
                "property": "og:author_email",
                "content": author_email,
            },
            {
                "name": "og:type",
                "property": "og:type",
                "content": "website",
            },
            {
                "name": "description",
                "property": "description",
                "content": article.metadata["description"],
            },
            {
                "name": "og:description",
                "property": "og:description",
                "content": article.metadata["description"],
            },
            {
                "name": "twitter:description",
                "property": "twitter:description",
                "content": article.metadata["description"],
            },
            {
                "name": "og:title",
                "property": "og:title",
                "content": f'{article.metadata["title"]} | {site_name}'[:60],
            },
            {
                "name": "twitter:title",
                "property": "twitter:title",
                "content": f'{article.metadata["title"]} | {site_name}'[:60],
            },
            {
                "name": "og:image",
                "property": "og:image",
                "content": f'{images_url}/{article.metadata["slug"]}-og.png',
            },
            {
                "name": "twitter:image",
                "property": "twitter:image",
                "content": f'{images_url}/{article.metadata["slug"]}-og.png',
            },
            {
                "name": "og:image:width",
                "property": "og:image:width",
                "content": "1600",
            },
            {
                "name": "og:image:width",
                "property": "og:image:width",
                "content": "900",
            },
            {
                "name": "twitter:card",
                "property": "twitter:card",
                "content": twitter_card,
            },
            {
                "name": "og:site_name",
                "property": "og:site_name",
                "content": site_name,
            },
            {
                "name": "twitter:creator",
                "property": "twitter:creator",
                "content": twitter_creator,
            },
            {
                "name": "title",
                "property": "title",
                "content": article.metadata["title"],
            },
            {
                "name": "generator",
                "property": "generator",
                "content": f"markata {__version__}",
            },
        ]
        return seo
    ```


---

## _add_seo_tags `function`

None

??? "_add_seo_tags source"
    ``` python
    def _add_seo_tags(seo: List, article: "frontmatter.Post", soup: BeautifulSoup) -> None:
        for meta in seo:
            soup.head.append(_create_seo_tag(meta, soup))
    ```


---

## _create_seo_tag `function`

None

??? "_create_seo_tag source"
    ``` python
    def _create_seo_tag(meta: dict, soup: BeautifulSoup) -> "Tag":
        tag = soup.new_tag("meta")
        for k in meta:
            tag.attrs[k] = meta[k]
        return tag
    ```


---

## render `function`

None

??? "render source"
    ``` python
    def render(markata: Markata) -> None:

        url = markata.get_config("url") or ""
        images_url = markata.get_config("images_url") or url or ""
        site_name = markata.get_config("site_name") or ""
        author_name = markata.get_config("author_name") or ""
        author_email = markata.get_config("author_email") or ""
        twitter_creator = markata.get_config("twitter_creator") or ""
        twitter_card = markata.get_config("twitter_card") or "summary_large_image"
        config_seo = markata.get_config("seo", warn=False) or dict()

        with markata.cache as cache:
            for article in markata.iter_articles("add seo tags from seo.py"):
                key = markata.make_hash(
                    "seo",
                    "render",
                    article.html,
                    site_name,
                    url,
                    article.metadata["slug"],
                    twitter_card,
                    article.metadata["title"],
                    str(config_seo),
                )

                html_from_cache = cache.get(key)

                if html_from_cache is None:
                    soup = BeautifulSoup(article.html, features="lxml")
                    seo = _create_seo(
                        markata=markata,
                        soup=soup,
                        article=article,
                        site_name=site_name,
                        author_name=author_name,
                        author_email=author_email,
                        twitter_card=twitter_card,
                        twitter_creator=twitter_creator,
                        config_seo=config_seo,
                        images_url=images_url,
                    )
                    _add_seo_tags(seo, article, soup)
                    canonical_link = soup.new_tag("link")
                    canonical_link.attrs["rel"] = "canonical"
                    if article.metadata["slug"] == "index":
                        canonical_link.attrs["href"] = f"{url}/"
                    else:
                        canonical_link.attrs["href"] = f'{url}/{article.metadata["slug"]}/'
                    soup.head.append(canonical_link)

                    meta_url = soup.new_tag("meta")
                    meta_url.attrs["name"] = "og:url"
                    meta_url.attrs["property"] = "og:url"
                    if article.metadata["slug"] == "index":
                        meta_url.attrs["content"] = f"{url}/"
                    else:
                        meta_url.attrs["content"] = f'{url}/{article.metadata["slug"]}/'
                    soup.head.append(meta_url)

                    html = soup.prettify()
                    cache.add(key, html, expire=markata.config["default_cache_expire"])

                else:
                    html = html_from_cache
                article.html = html
    ```