---
article_html: "<p>Markata's base command line commands.</p>\n<p>This plugin enables\n<a
  href=\"https://markata.dev/markata/plugins/base_cli/#build-function\"><code>build</code></a>\nand\n<a
  href=\"https://markata.dev/markata/plugins/base_cli/#list-function\"><code>list</code></a>\ncommands
  as part of the main markata cli.</p>\n<h2 id=\"building-your-site-with-the-cli\">Building
  Your Site with the Cli</h2>\n<p>Your Markata Site can be build completely from the
  command line.</p>\n<div class=\"highlight\"><pre><span></span><code>markata build\n\n<span
  class=\"c1\"># or if you prefer pipx</span>\npipx run markata build\n</code></pre></div>\n<p>see
  the\n<a href=\"https://markata.dev/markata/plugins/base_cli/#build-function\"><code>build</code></a>\nsection
  for more examples.</p>\n<h2 id=\"listing-your-articles\">Listing your articles</h2>\n<p>Markata
  list is a tool to help list out artile attributes right to your\nterminal.  This
  is very helpful to find articles on larger sites, or\ndebug what is getting picked
  up by markata.</p>\n<div class=\"highlight\"><pre><span></span><code>markata list
  --map <span class=\"s1\">&#39;str(date.year) + &quot;,&quot; + title&#39;</span>\n</code></pre></div>\n<p>see
  the\n<a href=\"https://markata.dev/markata/plugins/base_cli/#list-function\"><code>list</code></a>\nsection
  for more examples.</p>\n<hr />\n<h2 id=\"make_pretty-function\">make_pretty <code>function</code></h2>\n<p>This
  is a helper function that enables suppresses tracebacks from\nframeworks like <code>click</code>
  that can make your traceback long and hard\nto follow.  It also makes evrerything
  more colorful and easier to\nfollow.</p>\n<details>\n<summary>make_pretty source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">make_pretty</span><span
  class=\"p\">()</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n    <span class=\"sd\">&quot;&quot;&quot;</span>\n<span class=\"sd\">
  \   This is a helper function that enables suppresses tracebacks from</span>\n<span
  class=\"sd\">    frameworks like `click` that can make your traceback long and hard</span>\n<span
  class=\"sd\">    to follow.  It also makes evrerything more colorful and easier
  to</span>\n<span class=\"sd\">    follow.</span>\n<span class=\"sd\">    &quot;&quot;&quot;</span>\n
  \   <span class=\"kn\">import</span> <span class=\"nn\">click</span>\n    <span
  class=\"kn\">import</span> <span class=\"nn\">pluggy</span>\n    <span class=\"kn\">import</span>
  <span class=\"nn\">typer</span>\n    <span class=\"kn\">from</span> <span class=\"nn\">rich</span>
  <span class=\"kn\">import</span> <span class=\"n\">pretty</span> <span class=\"k\">as</span>
  <span class=\"n\">_pretty</span>\n    <span class=\"kn\">from</span> <span class=\"nn\">rich</span>
  <span class=\"kn\">import</span> <span class=\"n\">traceback</span>\n\n    <span
  class=\"n\">_pretty</span><span class=\"o\">.</span><span class=\"n\">install</span><span
  class=\"p\">()</span>\n    <span class=\"n\">traceback</span><span class=\"o\">.</span><span
  class=\"n\">install</span><span class=\"p\">(</span>\n        <span class=\"n\">show_locals</span><span
  class=\"o\">=</span><span class=\"kc\">True</span><span class=\"p\">,</span>\n        <span
  class=\"n\">suppress</span><span class=\"o\">=</span><span class=\"p\">[</span>\n
  \           <span class=\"n\">pluggy</span><span class=\"p\">,</span>\n            <span
  class=\"n\">click</span><span class=\"p\">,</span>\n            <span class=\"n\">typer</span><span
  class=\"p\">,</span>\n        <span class=\"p\">],</span>\n    <span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"cli-function\">cli <code>function</code></h2>\n<p>Markata hook to implement
  base cli commands.</p>\n<details>\n<summary>cli source</summary>\n<div class=\"highlight\"><pre><span></span><code><span
  class=\"k\">def</span> <span class=\"nf\">cli</span><span class=\"p\">(</span><span
  class=\"n\">app</span><span class=\"p\">:</span> <span class=\"n\">typer</span><span
  class=\"o\">.</span><span class=\"n\">Typer</span><span class=\"p\">,</span> <span
  class=\"n\">markata</span><span class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n    <span class=\"sd\">&quot;&quot;&quot;</span>\n<span class=\"sd\">
  \   Markata hook to implement base cli commands.</span>\n<span class=\"sd\">    &quot;&quot;&quot;</span>\n\n
  \   <span class=\"nd\">@app</span><span class=\"o\">.</span><span class=\"n\">command</span><span
  class=\"p\">()</span>\n    <span class=\"k\">def</span> <span class=\"nf\">build</span><span
  class=\"p\">(</span>\n        <span class=\"n\">pretty</span><span class=\"p\">:</span>
  <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span class=\"kc\">True</span><span
  class=\"p\">,</span>\n        <span class=\"n\">quiet</span><span class=\"p\">:</span>
  <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span class=\"n\">typer</span><span
  class=\"o\">.</span><span class=\"n\">Option</span><span class=\"p\">(</span>\n
  \           <span class=\"kc\">False</span><span class=\"p\">,</span>\n            <span
  class=\"s2\">&quot;--quiet&quot;</span><span class=\"p\">,</span>\n            <span
  class=\"s2\">&quot;-q&quot;</span><span class=\"p\">,</span>\n        <span class=\"p\">),</span>\n
  \       <span class=\"c1\"># to_dict: bool = False,</span>\n        <span class=\"n\">verbose</span><span
  class=\"p\">:</span> <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span
  class=\"n\">typer</span><span class=\"o\">.</span><span class=\"n\">Option</span><span
  class=\"p\">(</span>\n            <span class=\"kc\">False</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;--verbose&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;-v&quot;</span><span class=\"p\">,</span>\n
  \       <span class=\"p\">),</span>\n        <span class=\"n\">should_pdb</span><span
  class=\"p\">:</span> <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span
  class=\"n\">typer</span><span class=\"o\">.</span><span class=\"n\">Option</span><span
  class=\"p\">(</span>\n            <span class=\"kc\">False</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;--pdb&quot;</span><span class=\"p\">,</span>\n
  \       <span class=\"p\">),</span>\n        <span class=\"n\">profile</span><span
  class=\"p\">:</span> <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span
  class=\"kc\">True</span><span class=\"p\">,</span>\n    <span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \       <span class=\"sd\">&quot;&quot;&quot;</span>\n<span class=\"sd\">        Markata&#39;s
  primary way of building your site for production.</span>\n<span class=\"sd\">        By
  default, running `markta build` will render your markdown to</span>\n<span class=\"sd\">
  \       the `./markout` directory.</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span
  class=\"sd\">        markata build</span>\n<span class=\"sd\">        ```</span>\n\n<span
  class=\"sd\">        If you are having an issue and want to pop immediately into
  a debugger</span>\n<span class=\"sd\">        upon failure you can pass the `--pdb`
  flag to the build command.</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span
  class=\"sd\">        markata build  --pdb</span>\n<span class=\"sd\">        ```</span>\n\n<span
  class=\"sd\">        If you do not like the way rich looks, or its suppressing tracebaks
  you</span>\n<span class=\"sd\">        would like to remain visible you can use
  `--no-pretty`</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span class=\"sd\">
  \       markata build --no-pretty</span>\n<span class=\"sd\">        ```</span>\n\n<span
  class=\"sd\">        If you need to run without any console logging pass in the</span>\n<span
  class=\"sd\">        `--quiet` flag.</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span
  class=\"sd\">        markata build --quiet</span>\n<span class=\"sd\">        ```</span>\n\n<span
  class=\"sd\">        `markta build` will automatically run the pyinstrument profiler</span>\n<span
  class=\"sd\">        while building your site if you have pyinstrument installed.
  \ It</span>\n<span class=\"sd\">        will echo out your profile in the console
  as well as write it to</span>\n<span class=\"sd\">        `/_profile` on your built
  site. If you prefer not to run</span>\n<span class=\"sd\">        pyinstrument profiling,
  even when it is installed you can pass</span>\n<span class=\"sd\">        in `--no-profile`</span>\n\n<span
  class=\"sd\">        ``` bash</span>\n<span class=\"sd\">        markata build --no-profile</span>\n<span
  class=\"sd\">        ```</span>\n<span class=\"sd\">        &quot;&quot;&quot;</span>\n\n
  \       <span class=\"k\">if</span> <span class=\"n\">pretty</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">make_pretty</span><span class=\"p\">()</span>\n\n
  \       <span class=\"k\">if</span> <span class=\"n\">quiet</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">console</span><span
  class=\"o\">.</span><span class=\"n\">quiet</span> <span class=\"o\">=</span> <span
  class=\"kc\">True</span>\n\n        <span class=\"k\">if</span> <span class=\"n\">verbose</span><span
  class=\"p\">:</span>\n            <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">console</span><span class=\"o\">.</span><span class=\"n\">print</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;console options:&quot;</span><span
  class=\"p\">,</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">console</span><span class=\"o\">.</span><span class=\"n\">options</span><span
  class=\"p\">)</span>\n\n        <span class=\"k\">if</span> <span class=\"n\">profile</span><span
  class=\"p\">:</span>\n            <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">should_profile_cli</span> <span class=\"o\">=</span> <span class=\"kc\">True</span>\n
  \           <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">should_profile</span>
  <span class=\"o\">=</span> <span class=\"kc\">True</span>\n            <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">configure</span><span class=\"p\">()</span>\n\n
  \       <span class=\"k\">if</span> <span class=\"n\">should_pdb</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">pdb_run</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">run</span><span class=\"p\">)</span>\n\n        <span
  class=\"k\">else</span><span class=\"p\">:</span>\n            <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">run</span><span class=\"p\">()</span>\n\n
  \   <span class=\"nd\">@app</span><span class=\"o\">.</span><span class=\"n\">command</span><span
  class=\"p\">()</span>\n    <span class=\"k\">def</span> <span class=\"nf\">list</span><span
  class=\"p\">(</span>\n        <span class=\"nb\">map</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;title&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"nb\">filter</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;True&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"n\">sort</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;True&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"n\">head</span><span class=\"p\">:</span>
  <span class=\"n\">Optional</span><span class=\"p\">[</span><span class=\"nb\">int</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"kc\">None</span><span
  class=\"p\">,</span>\n        <span class=\"n\">tail</span><span class=\"p\">:</span>
  <span class=\"n\">Optional</span><span class=\"p\">[</span><span class=\"nb\">int</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"kc\">None</span><span
  class=\"p\">,</span>\n        <span class=\"n\">include_empty</span><span class=\"p\">:</span>
  <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span class=\"kc\">False</span><span
  class=\"p\">,</span>\n        <span class=\"n\">reverse</span><span class=\"p\">:</span>
  <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span class=\"kc\">False</span><span
  class=\"p\">,</span>\n        <span class=\"n\">use_pager</span><span class=\"p\">:</span>
  <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span class=\"n\">typer</span><span
  class=\"o\">.</span><span class=\"n\">Option</span><span class=\"p\">(</span><span
  class=\"kc\">True</span><span class=\"p\">,</span> <span class=\"s2\">&quot;--pager&quot;</span><span
  class=\"p\">,</span> <span class=\"s2\">&quot;--no-pager&quot;</span><span class=\"p\">),</span>\n
  \   <span class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n        <span class=\"sd\">&quot;&quot;&quot;</span>\n<span
  class=\"sd\">        Provides a way run markatas, map, filter, and sort from the</span>\n<span
  class=\"sd\">        command line.  I personally use this more often than the build</span>\n<span
  class=\"sd\">        command while I am writing on a site with a large number of</span>\n<span
  class=\"sd\">        posts on it.  It makes slicing in by `templatekey`, `tag`,
  or</span>\n<span class=\"sd\">        `date` much easier.</span>\n\n<span class=\"sd\">
  \       ### default list</span>\n\n<span class=\"sd\">        By default `markata
  list` will list all titles in a pager, for all posts</span>\n<span class=\"sd\">
  \       being loaded by markata.</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span
  class=\"sd\">        markata list</span>\n<span class=\"sd\">        ```</span>\n\n<span
  class=\"sd\">        ### Skip the pager</span>\n\n<span class=\"sd\">        Markata
  uses rich for its pager, it&#39;s pretty smart about when to</span>\n<span class=\"sd\">
  \       use the pager or pass text to the next thing in the pipeline,</span>\n<span
  class=\"sd\">        but if you don&#39;t want to run a pager you can pass  `--no-pager`</span>\n\n<span
  class=\"sd\">        ``` bash</span>\n<span class=\"sd\">        markata list --no-pager</span>\n<span
  class=\"sd\">        ```</span>\n\n<span class=\"sd\">        ### List other attributes</span>\n\n<span
  class=\"sd\">        You can list any other attribute tied to your posts.  These
  are</span>\n<span class=\"sd\">        added through either your yaml frontmatter
  at the start of your</span>\n<span class=\"sd\">        post, or through the use
  of a plugin.</span>\n\n\n<span class=\"sd\">        ``` bash</span>\n<span class=\"sd\">
  \       # the filepath of the post</span>\n<span class=\"sd\">        markata list
  --map path</span>\n\n<span class=\"sd\">        # the slug of the post (where it
  will show up on the site)</span>\n<span class=\"sd\">        markata list --map
  slug</span>\n\n<span class=\"sd\">        # the date of the post</span>\n<span class=\"sd\">
  \       markata list --map date</span>\n\n<span class=\"sd\">        # the full
  raw content of the post</span>\n<span class=\"sd\">        markata list --map content</span>\n<span
  class=\"sd\">        ```</span>\n\n<span class=\"sd\">        ### List more than
  one attribute</span>\n\n<span class=\"sd\">        You can create new attributes
  as you map to echo out by</span>\n<span class=\"sd\">        combining existing
  attributes.</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span class=\"sd\">
  \       markata list --map &#39;title + &quot; , &quot; + slug&#39;</span>\n<span
  class=\"sd\">        ```</span>\n\n<span class=\"sd\">        ### Using Python objects
  as map</span>\n\n<span class=\"sd\">        You can access attributes of each post
  attribute that you map</span>\n<span class=\"sd\">        over.  For instance on
  my blog, each post has a date that is a</span>\n<span class=\"sd\">        datetime
  object.  I can ask each post for its `date.year`</span>\n\n<span class=\"sd\">        ```
  bash</span>\n<span class=\"sd\">        markata list --map date.year</span>\n\n<span
  class=\"sd\">        # combining this with title</span>\n<span class=\"sd\">        markata
  list --map &#39;str(date.year) + &quot;,&quot; + title&#39;</span>\n<span class=\"sd\">
  \       ```</span>\n\n<span class=\"sd\">        ### Filtering posts</span>\n\n<span
  class=\"sd\">        Posts are filtered with python syntax, you will have all</span>\n<span
  class=\"sd\">        attributes tied to your posts available to filter with.</span>\n\n<span
  class=\"sd\">        ``` bash</span>\n<span class=\"sd\">        markata list --filter
  &quot;&#39;__&#39; not in title&quot;</span>\n<span class=\"sd\">        ```</span>\n\n<span
  class=\"sd\">        ### Filtering by dates</span>\n\n<span class=\"sd\">        If
  your site has dates tied to your posts you can filter by</span>\n<span class=\"sd\">
  \       date.  On my blog this makes a ton of sense and is quite useful.</span>\n<span
  class=\"sd\">        On the Markata docs though it doesn&#39;t really make much
  sense,</span>\n<span class=\"sd\">        since there really isn&#39;t the idea
  of a post date there.</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span
  class=\"sd\">        # listing today&#39;s posts</span>\n<span class=\"sd\">        markata
  list --filter &quot;date==today&quot;</span>\n\n<span class=\"sd\">        # listing
  this year&#39;s posts</span>\n<span class=\"sd\">        markata list --filter &quot;date.year==today.year&quot;</span>\n<span
  class=\"sd\">        ```</span>\n\n<span class=\"sd\">        ### Full Content Search</span>\n\n<span
  class=\"sd\">        You can also search the full content of each post for specific</span>\n<span
  class=\"sd\">        words.</span>\n<span class=\"sd\">        ``` bash</span>\n\n<span
  class=\"sd\">        markata list --filter &quot;&#39;python&#39; in content&quot;</span>\n<span
  class=\"sd\">        ```</span>\n\n<span class=\"sd\">        ### Filtering by frontmatter
  data</span>\n\n<span class=\"sd\">        I use a templateKey on my personal blog
  to determine which</span>\n<span class=\"sd\">        template to render the page
  with.  I can fitler my posts by a</span>\n<span class=\"sd\">        `til` (today
  i learned) key.</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span class=\"sd\">
  \       markata list --filter &quot;templateKey==&#39;til&#39;&quot;</span>\n<span
  class=\"sd\">        ```</span>\n\n<span class=\"sd\">        ### Combining filters</span>\n\n<span
  class=\"sd\">        Filters can be combined together quite like maps can, it&#39;s
  all</span>\n<span class=\"sd\">        just python syntax.</span>\n\n<span class=\"sd\">
  \       ``` bash</span>\n<span class=\"sd\">        markata list --filter &quot;templateKey==&#39;til&#39;
  and date == today&quot;</span>\n<span class=\"sd\">        ```</span>\n\n<span class=\"sd\">
  \       ### Sorting posts</span>\n\n<span class=\"sd\">        Posts can be sorted
  by attributes on your post, and they can</span>\n<span class=\"sd\">        even
  be reversed.</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span class=\"sd\">
  \       markta list --sort date</span>\n<span class=\"sd\">        markta list --sort
  date --reverse</span>\n<span class=\"sd\">        ```</span>\n\n<span class=\"sd\">
  \       ### Putting it all together</span>\n\n<span class=\"sd\">        The real
  power of all this comes when you combine them all into</span>\n<span class=\"sd\">
  \       lists that work for you and your workflow.  This really makes</span>\n<span
  class=\"sd\">        working on larger projects so much easier to find things.</span>\n\n\n<span
  class=\"sd\">        ### Making a fuzzy picker for your posts</span>\n\n<span class=\"sd\">
  \       Here is a bash command to open an fzf picker for todays posts,</span>\n<span
  class=\"sd\">        then open it in your `$EDITOR`</span>\n\n<span class=\"sd\">
  \       ``` bash</span>\n<span class=\"sd\">        markata list --map path --filter
  &#39;date==today&#39; --sort date --reverse | fzf --preview &#39;bat --color always
  {}&#39; | xargs -I {} $EDITOR {}</span>\n<span class=\"sd\">        ```</span>\n\n<span
  class=\"sd\">        ### Combining wtih nvim Telescope</span>\n\n<span class=\"sd\">
  \       Here is the same command setup as a Telescope picker for neovim.</span>\n\n<span
  class=\"sd\">        ``` vim</span>\n<span class=\"sd\">        nnoremap &lt;leader&gt;et
  &lt;cmd&gt;Telescope find_files find_command=markata,list,--map,path,--filter,date==today&lt;cr&gt;</span>\n<span
  class=\"sd\">        ```</span>\n\n<span class=\"sd\">        If you have another
  way to open posts in your editor with</span>\n<span class=\"sd\">        `markata
  list` I would love to accept a PR to add it to the</span>\n<span class=\"sd\">        examples
  here.</span>\n<span class=\"sd\">        &quot;&quot;&quot;</span>\n\n        <span
  class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">console</span><span
  class=\"o\">.</span><span class=\"n\">quiet</span> <span class=\"o\">=</span> <span
  class=\"kc\">True</span>\n\n        <span class=\"n\">tail</span> <span class=\"o\">=</span>
  <span class=\"o\">-</span><span class=\"n\">tail</span> <span class=\"k\">if</span>
  <span class=\"n\">tail</span> <span class=\"k\">else</span> <span class=\"n\">tail</span>\n
  \       <span class=\"n\">filtered</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">map</span><span class=\"p\">(</span><span
  class=\"nb\">map</span><span class=\"p\">,</span> <span class=\"nb\">filter</span><span
  class=\"p\">,</span> <span class=\"n\">sort</span><span class=\"p\">)</span>\n        <span
  class=\"k\">if</span> <span class=\"ow\">not</span> <span class=\"n\">include_empty</span><span
  class=\"p\">:</span>\n            <span class=\"n\">filtered</span> <span class=\"o\">=</span>
  <span class=\"p\">[</span><span class=\"n\">a</span> <span class=\"k\">for</span>
  <span class=\"n\">a</span> <span class=\"ow\">in</span> <span class=\"n\">filtered</span>
  <span class=\"k\">if</span> <span class=\"n\">a</span> <span class=\"o\">!=</span>
  <span class=\"s2\">&quot;&quot;</span><span class=\"p\">]</span>\n        <span
  class=\"n\">filtered</span> <span class=\"o\">=</span> <span class=\"n\">filtered</span><span
  class=\"p\">[</span><span class=\"n\">tail</span><span class=\"p\">:</span><span
  class=\"n\">head</span><span class=\"p\">]</span>\n        <span class=\"k\">if</span>
  <span class=\"n\">reverse</span><span class=\"p\">:</span>\n            <span class=\"n\">filtered</span>
  <span class=\"o\">=</span> <span class=\"nb\">reversed</span><span class=\"p\">(</span><span
  class=\"n\">filtered</span><span class=\"p\">)</span>\n\n        <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">console</span><span class=\"o\">.</span><span
  class=\"n\">quiet</span> <span class=\"o\">=</span> <span class=\"kc\">False</span>\n
  \       <span class=\"k\">if</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">console</span><span class=\"o\">.</span><span class=\"n\">is_terminal</span>
  <span class=\"ow\">and</span> <span class=\"n\">use_pager</span><span class=\"p\">:</span>\n
  \           <span class=\"k\">with</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">console</span><span class=\"o\">.</span><span
  class=\"n\">pager</span><span class=\"p\">():</span>\n                <span class=\"k\">for</span>
  <span class=\"n\">a</span> <span class=\"ow\">in</span> <span class=\"n\">filtered</span><span
  class=\"p\">:</span>\n                    <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">console</span><span class=\"o\">.</span><span
  class=\"n\">print</span><span class=\"p\">(</span><span class=\"n\">a</span><span
  class=\"p\">,</span> <span class=\"n\">style</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;purple&quot;</span><span class=\"p\">)</span>\n        <span
  class=\"k\">else</span><span class=\"p\">:</span>\n            <span class=\"k\">for</span>
  <span class=\"n\">a</span> <span class=\"ow\">in</span> <span class=\"n\">filtered</span><span
  class=\"p\">:</span>\n                <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">console</span><span class=\"o\">.</span><span class=\"n\">print</span><span
  class=\"p\">(</span><span class=\"n\">a</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"pdb_run-function\">pdb_run <code>function</code></h2>\n<p>Wraps a function
  call with a post_mortem pdb debugger.</p>\n<details>\n<summary>pdb_run source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">pdb_run</span><span
  class=\"p\">(</span><span class=\"n\">func</span><span class=\"p\">:</span> <span
  class=\"n\">Callable</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n    <span class=\"sd\">&quot;&quot;&quot;</span>\n<span
  class=\"sd\">    Wraps a function call with a post_mortem pdb debugger.</span>\n<span
  class=\"sd\">    &quot;&quot;&quot;</span>\n    <span class=\"k\">try</span><span
  class=\"p\">:</span>\n        <span class=\"n\">func</span><span class=\"p\">()</span>\n
  \   <span class=\"k\">except</span> <span class=\"ne\">Exception</span><span class=\"p\">:</span>\n
  \       <span class=\"n\">extype</span><span class=\"p\">,</span> <span class=\"n\">value</span><span
  class=\"p\">,</span> <span class=\"n\">tb</span> <span class=\"o\">=</span> <span
  class=\"n\">sys</span><span class=\"o\">.</span><span class=\"n\">exc_info</span><span
  class=\"p\">()</span>\n        <span class=\"n\">traceback</span><span class=\"o\">.</span><span
  class=\"n\">print_exc</span><span class=\"p\">()</span>\n        <span class=\"n\">pdb</span><span
  class=\"o\">.</span><span class=\"n\">post_mortem</span><span class=\"p\">(</span><span
  class=\"n\">tb</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"build-function\">build <code>function</code></h2>\n<p>Markata's primary
  way of building your site for production.\nBy default, running <code>markta build</code>
  will render your markdown to\nthe <code>./markout</code> directory.</p>\n<div class=\"highlight\"><pre><span></span><code>markata
  build\n</code></pre></div>\n<p>If you are having an issue and want to pop immediately
  into a debugger\nupon failure you can pass the <code>--pdb</code> flag to the build
  command.</p>\n<div class=\"highlight\"><pre><span></span><code>markata build  --pdb\n</code></pre></div>\n<p>If
  you do not like the way rich looks, or its suppressing tracebaks you\nwould like
  to remain visible you can use <code>--no-pretty</code></p>\n<div class=\"highlight\"><pre><span></span><code>markata
  build --no-pretty\n</code></pre></div>\n<p>If you need to run without any console
  logging pass in the\n<code>--quiet</code> flag.</p>\n<div class=\"highlight\"><pre><span></span><code>markata
  build --quiet\n</code></pre></div>\n<p><code>markta build</code> will automatically
  run the pyinstrument profiler\nwhile building your site if you have pyinstrument
  installed.  It\nwill echo out your profile in the console as well as write it to\n<code>/_profile</code>
  on your built site. If you prefer not to run\npyinstrument profiling, even when
  it is installed you can pass\nin <code>--no-profile</code></p>\n<div class=\"highlight\"><pre><span></span><code>markata
  build --no-profile\n</code></pre></div>\n<details>\n<summary>build source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">build</span><span
  class=\"p\">(</span>\n        <span class=\"n\">pretty</span><span class=\"p\">:</span>
  <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span class=\"kc\">True</span><span
  class=\"p\">,</span>\n        <span class=\"n\">quiet</span><span class=\"p\">:</span>
  <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span class=\"n\">typer</span><span
  class=\"o\">.</span><span class=\"n\">Option</span><span class=\"p\">(</span>\n
  \           <span class=\"kc\">False</span><span class=\"p\">,</span>\n            <span
  class=\"s2\">&quot;--quiet&quot;</span><span class=\"p\">,</span>\n            <span
  class=\"s2\">&quot;-q&quot;</span><span class=\"p\">,</span>\n        <span class=\"p\">),</span>\n
  \       <span class=\"c1\"># to_dict: bool = False,</span>\n        <span class=\"n\">verbose</span><span
  class=\"p\">:</span> <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span
  class=\"n\">typer</span><span class=\"o\">.</span><span class=\"n\">Option</span><span
  class=\"p\">(</span>\n            <span class=\"kc\">False</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;--verbose&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;-v&quot;</span><span class=\"p\">,</span>\n
  \       <span class=\"p\">),</span>\n        <span class=\"n\">should_pdb</span><span
  class=\"p\">:</span> <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span
  class=\"n\">typer</span><span class=\"o\">.</span><span class=\"n\">Option</span><span
  class=\"p\">(</span>\n            <span class=\"kc\">False</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;--pdb&quot;</span><span class=\"p\">,</span>\n
  \       <span class=\"p\">),</span>\n        <span class=\"n\">profile</span><span
  class=\"p\">:</span> <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span
  class=\"kc\">True</span><span class=\"p\">,</span>\n    <span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \       <span class=\"sd\">&quot;&quot;&quot;</span>\n<span class=\"sd\">        Markata&#39;s
  primary way of building your site for production.</span>\n<span class=\"sd\">        By
  default, running `markta build` will render your markdown to</span>\n<span class=\"sd\">
  \       the `./markout` directory.</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span
  class=\"sd\">        markata build</span>\n<span class=\"sd\">        ```</span>\n\n<span
  class=\"sd\">        If you are having an issue and want to pop immediately into
  a debugger</span>\n<span class=\"sd\">        upon failure you can pass the `--pdb`
  flag to the build command.</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span
  class=\"sd\">        markata build  --pdb</span>\n<span class=\"sd\">        ```</span>\n\n<span
  class=\"sd\">        If you do not like the way rich looks, or its suppressing tracebaks
  you</span>\n<span class=\"sd\">        would like to remain visible you can use
  `--no-pretty`</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span class=\"sd\">
  \       markata build --no-pretty</span>\n<span class=\"sd\">        ```</span>\n\n<span
  class=\"sd\">        If you need to run without any console logging pass in the</span>\n<span
  class=\"sd\">        `--quiet` flag.</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span
  class=\"sd\">        markata build --quiet</span>\n<span class=\"sd\">        ```</span>\n\n<span
  class=\"sd\">        `markta build` will automatically run the pyinstrument profiler</span>\n<span
  class=\"sd\">        while building your site if you have pyinstrument installed.
  \ It</span>\n<span class=\"sd\">        will echo out your profile in the console
  as well as write it to</span>\n<span class=\"sd\">        `/_profile` on your built
  site. If you prefer not to run</span>\n<span class=\"sd\">        pyinstrument profiling,
  even when it is installed you can pass</span>\n<span class=\"sd\">        in `--no-profile`</span>\n\n<span
  class=\"sd\">        ``` bash</span>\n<span class=\"sd\">        markata build --no-profile</span>\n<span
  class=\"sd\">        ```</span>\n<span class=\"sd\">        &quot;&quot;&quot;</span>\n\n
  \       <span class=\"k\">if</span> <span class=\"n\">pretty</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">make_pretty</span><span class=\"p\">()</span>\n\n
  \       <span class=\"k\">if</span> <span class=\"n\">quiet</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">console</span><span
  class=\"o\">.</span><span class=\"n\">quiet</span> <span class=\"o\">=</span> <span
  class=\"kc\">True</span>\n\n        <span class=\"k\">if</span> <span class=\"n\">verbose</span><span
  class=\"p\">:</span>\n            <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">console</span><span class=\"o\">.</span><span class=\"n\">print</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;console options:&quot;</span><span
  class=\"p\">,</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">console</span><span class=\"o\">.</span><span class=\"n\">options</span><span
  class=\"p\">)</span>\n\n        <span class=\"k\">if</span> <span class=\"n\">profile</span><span
  class=\"p\">:</span>\n            <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">should_profile_cli</span> <span class=\"o\">=</span> <span class=\"kc\">True</span>\n
  \           <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">should_profile</span>
  <span class=\"o\">=</span> <span class=\"kc\">True</span>\n            <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">configure</span><span class=\"p\">()</span>\n\n
  \       <span class=\"k\">if</span> <span class=\"n\">should_pdb</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">pdb_run</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">run</span><span class=\"p\">)</span>\n\n        <span
  class=\"k\">else</span><span class=\"p\">:</span>\n            <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">run</span><span class=\"p\">()</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"list-function\">list <code>function</code></h2>\n<p>Provides a way
  run markatas, map, filter, and sort from the\ncommand line.  I personally use this
  more often than the build\ncommand while I am writing on a site with a large number
  of\nposts on it.  It makes slicing in by <code>templatekey</code>, <code>tag</code>,
  or\n<code>date</code> much easier.</p>\n<h3 id=\"default-list\">default list</h3>\n<p>By
  default <code>markata list</code> will list all titles in a pager, for all posts\nbeing
  loaded by markata.</p>\n<div class=\"highlight\"><pre><span></span><code>markata
  list\n</code></pre></div>\n<h3 id=\"skip-the-pager\">Skip the pager</h3>\n<p>Markata
  uses rich for its pager, it's pretty smart about when to\nuse the pager or pass
  text to the next thing in the pipeline,\nbut if you don't want to run a pager you
  can pass  <code>--no-pager</code></p>\n<div class=\"highlight\"><pre><span></span><code>markata
  list --no-pager\n</code></pre></div>\n<h3 id=\"list-other-attributes\">List other
  attributes</h3>\n<p>You can list any other attribute tied to your posts.  These
  are\nadded through either your yaml frontmatter at the start of your\npost, or through
  the use of a plugin.</p>\n<div class=\"highlight\"><pre><span></span><code><span
  class=\"c1\"># the filepath of the post</span>\nmarkata list --map path\n\n<span
  class=\"c1\"># the slug of the post (where it will show up on the site)</span>\nmarkata
  list --map slug\n\n<span class=\"c1\"># the date of the post</span>\nmarkata list
  --map date\n\n<span class=\"c1\"># the full raw content of the post</span>\nmarkata
  list --map content\n</code></pre></div>\n<h3 id=\"list-more-than-one-attribute\">List
  more than one attribute</h3>\n<p>You can create new attributes as you map to echo
  out by\ncombining existing attributes.</p>\n<div class=\"highlight\"><pre><span></span><code>markata
  list --map <span class=\"s1\">&#39;title + &quot; , &quot; + slug&#39;</span>\n</code></pre></div>\n<h3
  id=\"using-python-objects-as-map\">Using Python objects as map</h3>\n<p>You can
  access attributes of each post attribute that you map\nover.  For instance on my
  blog, each post has a date that is a\ndatetime object.  I can ask each post for
  its <code>date.year</code></p>\n<div class=\"highlight\"><pre><span></span><code>markata
  list --map date.year\n\n<span class=\"c1\"># combining this with title</span>\nmarkata
  list --map <span class=\"s1\">&#39;str(date.year) + &quot;,&quot; + title&#39;</span>\n</code></pre></div>\n<h3
  id=\"filtering-posts\">Filtering posts</h3>\n<p>Posts are filtered with python syntax,
  you will have all\nattributes tied to your posts available to filter with.</p>\n<div
  class=\"highlight\"><pre><span></span><code>markata list --filter <span class=\"s2\">&quot;&#39;__&#39;
  not in title&quot;</span>\n</code></pre></div>\n<h3 id=\"filtering-by-dates\">Filtering
  by dates</h3>\n<p>If your site has dates tied to your posts you can filter by\ndate.
  \ On my blog this makes a ton of sense and is quite useful.\nOn the Markata docs
  though it doesn't really make much sense,\nsince there really isn't the idea of
  a post date there.</p>\n<div class=\"highlight\"><pre><span></span><code><span class=\"c1\">#
  listing today&#39;s posts</span>\nmarkata list --filter <span class=\"s2\">&quot;date==today&quot;</span>\n\n<span
  class=\"c1\"># listing this year&#39;s posts</span>\nmarkata list --filter <span
  class=\"s2\">&quot;date.year==today.year&quot;</span>\n</code></pre></div>\n<h3
  id=\"full-content-search\">Full Content Search</h3>\n<p>You can also search the
  full content of each post for specific\nwords.\n<div class=\"highlight\"><pre><span></span><code>markata
  list --filter <span class=\"s2\">&quot;&#39;python&#39; in content&quot;</span>\n</code></pre></div></p>\n<h3
  id=\"filtering-by-frontmatter-data\">Filtering by frontmatter data</h3>\n<p>I use
  a templateKey on my personal blog to determine which\ntemplate to render the page
  with.  I can fitler my posts by a\n<code>til</code> (today i learned) key.</p>\n<div
  class=\"highlight\"><pre><span></span><code>markata list --filter <span class=\"s2\">&quot;templateKey==&#39;til&#39;&quot;</span>\n</code></pre></div>\n<h3
  id=\"combining-filters\">Combining filters</h3>\n<p>Filters can be combined together
  quite like maps can, it's all\njust python syntax.</p>\n<div class=\"highlight\"><pre><span></span><code>markata
  list --filter <span class=\"s2\">&quot;templateKey==&#39;til&#39; and date == today&quot;</span>\n</code></pre></div>\n<h3
  id=\"sorting-posts\">Sorting posts</h3>\n<p>Posts can be sorted by attributes on
  your post, and they can\neven be reversed.</p>\n<div class=\"highlight\"><pre><span></span><code>markta
  list --sort date\nmarkta list --sort date --reverse\n</code></pre></div>\n<h3 id=\"putting-it-all-together\">Putting
  it all together</h3>\n<p>The real power of all this comes when you combine them
  all into\nlists that work for you and your workflow.  This really makes\nworking
  on larger projects so much easier to find things.</p>\n<h3 id=\"making-a-fuzzy-picker-for-your-posts\">Making
  a fuzzy picker for your posts</h3>\n<p>Here is a bash command to open an fzf picker
  for todays posts,\nthen open it in your <code>$EDITOR</code></p>\n<div class=\"highlight\"><pre><span></span><code>markata
  list --map path --filter <span class=\"s1\">&#39;date==today&#39;</span> --sort
  date --reverse <span class=\"p\">|</span> fzf --preview <span class=\"s1\">&#39;bat
  --color always {}&#39;</span> <span class=\"p\">|</span> xargs -I <span class=\"o\">{}</span>
  <span class=\"nv\">$EDITOR</span> <span class=\"o\">{}</span>\n</code></pre></div>\n<h3
  id=\"combining-wtih-nvim-telescope\">Combining wtih nvim Telescope</h3>\n<p>Here
  is the same command setup as a Telescope picker for neovim.</p>\n<div class=\"highlight\"><pre><span></span><code><span
  class=\"nb\">nnoremap</span> <span class=\"p\">&lt;</span>leader<span class=\"p\">&gt;</span><span
  class=\"nb\">et</span> <span class=\"p\">&lt;</span>cmd<span class=\"p\">&gt;</span>Telescope
  find_files find_command<span class=\"p\">=</span>markata<span class=\"p\">,</span><span
  class=\"nb\">list</span><span class=\"p\">,--</span>map<span class=\"p\">,</span><span
  class=\"nb\">path</span><span class=\"p\">,--</span>filter<span class=\"p\">,</span>date<span
  class=\"p\">==</span>today<span class=\"p\">&lt;</span><span class=\"k\">cr</span><span
  class=\"p\">&gt;</span>\n</code></pre></div>\n<p>If you have another way to open
  posts in your editor with\n<code>markata list</code> I would love to accept a PR
  to add it to the\nexamples here.</p>\n<details>\n<summary>list source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">list</span><span
  class=\"p\">(</span>\n        <span class=\"nb\">map</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;title&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"nb\">filter</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;True&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"n\">sort</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;True&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"n\">head</span><span class=\"p\">:</span>
  <span class=\"n\">Optional</span><span class=\"p\">[</span><span class=\"nb\">int</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"kc\">None</span><span
  class=\"p\">,</span>\n        <span class=\"n\">tail</span><span class=\"p\">:</span>
  <span class=\"n\">Optional</span><span class=\"p\">[</span><span class=\"nb\">int</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"kc\">None</span><span
  class=\"p\">,</span>\n        <span class=\"n\">include_empty</span><span class=\"p\">:</span>
  <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span class=\"kc\">False</span><span
  class=\"p\">,</span>\n        <span class=\"n\">reverse</span><span class=\"p\">:</span>
  <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span class=\"kc\">False</span><span
  class=\"p\">,</span>\n        <span class=\"n\">use_pager</span><span class=\"p\">:</span>
  <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span class=\"n\">typer</span><span
  class=\"o\">.</span><span class=\"n\">Option</span><span class=\"p\">(</span><span
  class=\"kc\">True</span><span class=\"p\">,</span> <span class=\"s2\">&quot;--pager&quot;</span><span
  class=\"p\">,</span> <span class=\"s2\">&quot;--no-pager&quot;</span><span class=\"p\">),</span>\n
  \   <span class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n        <span class=\"sd\">&quot;&quot;&quot;</span>\n<span
  class=\"sd\">        Provides a way run markatas, map, filter, and sort from the</span>\n<span
  class=\"sd\">        command line.  I personally use this more often than the build</span>\n<span
  class=\"sd\">        command while I am writing on a site with a large number of</span>\n<span
  class=\"sd\">        posts on it.  It makes slicing in by `templatekey`, `tag`,
  or</span>\n<span class=\"sd\">        `date` much easier.</span>\n\n<span class=\"sd\">
  \       ### default list</span>\n\n<span class=\"sd\">        By default `markata
  list` will list all titles in a pager, for all posts</span>\n<span class=\"sd\">
  \       being loaded by markata.</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span
  class=\"sd\">        markata list</span>\n<span class=\"sd\">        ```</span>\n\n<span
  class=\"sd\">        ### Skip the pager</span>\n\n<span class=\"sd\">        Markata
  uses rich for its pager, it&#39;s pretty smart about when to</span>\n<span class=\"sd\">
  \       use the pager or pass text to the next thing in the pipeline,</span>\n<span
  class=\"sd\">        but if you don&#39;t want to run a pager you can pass  `--no-pager`</span>\n\n<span
  class=\"sd\">        ``` bash</span>\n<span class=\"sd\">        markata list --no-pager</span>\n<span
  class=\"sd\">        ```</span>\n\n<span class=\"sd\">        ### List other attributes</span>\n\n<span
  class=\"sd\">        You can list any other attribute tied to your posts.  These
  are</span>\n<span class=\"sd\">        added through either your yaml frontmatter
  at the start of your</span>\n<span class=\"sd\">        post, or through the use
  of a plugin.</span>\n\n\n<span class=\"sd\">        ``` bash</span>\n<span class=\"sd\">
  \       # the filepath of the post</span>\n<span class=\"sd\">        markata list
  --map path</span>\n\n<span class=\"sd\">        # the slug of the post (where it
  will show up on the site)</span>\n<span class=\"sd\">        markata list --map
  slug</span>\n\n<span class=\"sd\">        # the date of the post</span>\n<span class=\"sd\">
  \       markata list --map date</span>\n\n<span class=\"sd\">        # the full
  raw content of the post</span>\n<span class=\"sd\">        markata list --map content</span>\n<span
  class=\"sd\">        ```</span>\n\n<span class=\"sd\">        ### List more than
  one attribute</span>\n\n<span class=\"sd\">        You can create new attributes
  as you map to echo out by</span>\n<span class=\"sd\">        combining existing
  attributes.</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span class=\"sd\">
  \       markata list --map &#39;title + &quot; , &quot; + slug&#39;</span>\n<span
  class=\"sd\">        ```</span>\n\n<span class=\"sd\">        ### Using Python objects
  as map</span>\n\n<span class=\"sd\">        You can access attributes of each post
  attribute that you map</span>\n<span class=\"sd\">        over.  For instance on
  my blog, each post has a date that is a</span>\n<span class=\"sd\">        datetime
  object.  I can ask each post for its `date.year`</span>\n\n<span class=\"sd\">        ```
  bash</span>\n<span class=\"sd\">        markata list --map date.year</span>\n\n<span
  class=\"sd\">        # combining this with title</span>\n<span class=\"sd\">        markata
  list --map &#39;str(date.year) + &quot;,&quot; + title&#39;</span>\n<span class=\"sd\">
  \       ```</span>\n\n<span class=\"sd\">        ### Filtering posts</span>\n\n<span
  class=\"sd\">        Posts are filtered with python syntax, you will have all</span>\n<span
  class=\"sd\">        attributes tied to your posts available to filter with.</span>\n\n<span
  class=\"sd\">        ``` bash</span>\n<span class=\"sd\">        markata list --filter
  &quot;&#39;__&#39; not in title&quot;</span>\n<span class=\"sd\">        ```</span>\n\n<span
  class=\"sd\">        ### Filtering by dates</span>\n\n<span class=\"sd\">        If
  your site has dates tied to your posts you can filter by</span>\n<span class=\"sd\">
  \       date.  On my blog this makes a ton of sense and is quite useful.</span>\n<span
  class=\"sd\">        On the Markata docs though it doesn&#39;t really make much
  sense,</span>\n<span class=\"sd\">        since there really isn&#39;t the idea
  of a post date there.</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span
  class=\"sd\">        # listing today&#39;s posts</span>\n<span class=\"sd\">        markata
  list --filter &quot;date==today&quot;</span>\n\n<span class=\"sd\">        # listing
  this year&#39;s posts</span>\n<span class=\"sd\">        markata list --filter &quot;date.year==today.year&quot;</span>\n<span
  class=\"sd\">        ```</span>\n\n<span class=\"sd\">        ### Full Content Search</span>\n\n<span
  class=\"sd\">        You can also search the full content of each post for specific</span>\n<span
  class=\"sd\">        words.</span>\n<span class=\"sd\">        ``` bash</span>\n\n<span
  class=\"sd\">        markata list --filter &quot;&#39;python&#39; in content&quot;</span>\n<span
  class=\"sd\">        ```</span>\n\n<span class=\"sd\">        ### Filtering by frontmatter
  data</span>\n\n<span class=\"sd\">        I use a templateKey on my personal blog
  to determine which</span>\n<span class=\"sd\">        template to render the page
  with.  I can fitler my posts by a</span>\n<span class=\"sd\">        `til` (today
  i learned) key.</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span class=\"sd\">
  \       markata list --filter &quot;templateKey==&#39;til&#39;&quot;</span>\n<span
  class=\"sd\">        ```</span>\n\n<span class=\"sd\">        ### Combining filters</span>\n\n<span
  class=\"sd\">        Filters can be combined together quite like maps can, it&#39;s
  all</span>\n<span class=\"sd\">        just python syntax.</span>\n\n<span class=\"sd\">
  \       ``` bash</span>\n<span class=\"sd\">        markata list --filter &quot;templateKey==&#39;til&#39;
  and date == today&quot;</span>\n<span class=\"sd\">        ```</span>\n\n<span class=\"sd\">
  \       ### Sorting posts</span>\n\n<span class=\"sd\">        Posts can be sorted
  by attributes on your post, and they can</span>\n<span class=\"sd\">        even
  be reversed.</span>\n\n<span class=\"sd\">        ``` bash</span>\n<span class=\"sd\">
  \       markta list --sort date</span>\n<span class=\"sd\">        markta list --sort
  date --reverse</span>\n<span class=\"sd\">        ```</span>\n\n<span class=\"sd\">
  \       ### Putting it all together</span>\n\n<span class=\"sd\">        The real
  power of all this comes when you combine them all into</span>\n<span class=\"sd\">
  \       lists that work for you and your workflow.  This really makes</span>\n<span
  class=\"sd\">        working on larger projects so much easier to find things.</span>\n\n\n<span
  class=\"sd\">        ### Making a fuzzy picker for your posts</span>\n\n<span class=\"sd\">
  \       Here is a bash command to open an fzf picker for todays posts,</span>\n<span
  class=\"sd\">        then open it in your `$EDITOR`</span>\n\n<span class=\"sd\">
  \       ``` bash</span>\n<span class=\"sd\">        markata list --map path --filter
  &#39;date==today&#39; --sort date --reverse | fzf --preview &#39;bat --color always
  {}&#39; | xargs -I {} $EDITOR {}</span>\n<span class=\"sd\">        ```</span>\n\n<span
  class=\"sd\">        ### Combining wtih nvim Telescope</span>\n\n<span class=\"sd\">
  \       Here is the same command setup as a Telescope picker for neovim.</span>\n\n<span
  class=\"sd\">        ``` vim</span>\n<span class=\"sd\">        nnoremap &lt;leader&gt;et
  &lt;cmd&gt;Telescope find_files find_command=markata,list,--map,path,--filter,date==today&lt;cr&gt;</span>\n<span
  class=\"sd\">        ```</span>\n\n<span class=\"sd\">        If you have another
  way to open posts in your editor with</span>\n<span class=\"sd\">        `markata
  list` I would love to accept a PR to add it to the</span>\n<span class=\"sd\">        examples
  here.</span>\n<span class=\"sd\">        &quot;&quot;&quot;</span>\n\n        <span
  class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">console</span><span
  class=\"o\">.</span><span class=\"n\">quiet</span> <span class=\"o\">=</span> <span
  class=\"kc\">True</span>\n\n        <span class=\"n\">tail</span> <span class=\"o\">=</span>
  <span class=\"o\">-</span><span class=\"n\">tail</span> <span class=\"k\">if</span>
  <span class=\"n\">tail</span> <span class=\"k\">else</span> <span class=\"n\">tail</span>\n
  \       <span class=\"n\">filtered</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">map</span><span class=\"p\">(</span><span
  class=\"nb\">map</span><span class=\"p\">,</span> <span class=\"nb\">filter</span><span
  class=\"p\">,</span> <span class=\"n\">sort</span><span class=\"p\">)</span>\n        <span
  class=\"k\">if</span> <span class=\"ow\">not</span> <span class=\"n\">include_empty</span><span
  class=\"p\">:</span>\n            <span class=\"n\">filtered</span> <span class=\"o\">=</span>
  <span class=\"p\">[</span><span class=\"n\">a</span> <span class=\"k\">for</span>
  <span class=\"n\">a</span> <span class=\"ow\">in</span> <span class=\"n\">filtered</span>
  <span class=\"k\">if</span> <span class=\"n\">a</span> <span class=\"o\">!=</span>
  <span class=\"s2\">&quot;&quot;</span><span class=\"p\">]</span>\n        <span
  class=\"n\">filtered</span> <span class=\"o\">=</span> <span class=\"n\">filtered</span><span
  class=\"p\">[</span><span class=\"n\">tail</span><span class=\"p\">:</span><span
  class=\"n\">head</span><span class=\"p\">]</span>\n        <span class=\"k\">if</span>
  <span class=\"n\">reverse</span><span class=\"p\">:</span>\n            <span class=\"n\">filtered</span>
  <span class=\"o\">=</span> <span class=\"nb\">reversed</span><span class=\"p\">(</span><span
  class=\"n\">filtered</span><span class=\"p\">)</span>\n\n        <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">console</span><span class=\"o\">.</span><span
  class=\"n\">quiet</span> <span class=\"o\">=</span> <span class=\"kc\">False</span>\n
  \       <span class=\"k\">if</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">console</span><span class=\"o\">.</span><span class=\"n\">is_terminal</span>
  <span class=\"ow\">and</span> <span class=\"n\">use_pager</span><span class=\"p\">:</span>\n
  \           <span class=\"k\">with</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">console</span><span class=\"o\">.</span><span
  class=\"n\">pager</span><span class=\"p\">():</span>\n                <span class=\"k\">for</span>
  <span class=\"n\">a</span> <span class=\"ow\">in</span> <span class=\"n\">filtered</span><span
  class=\"p\">:</span>\n                    <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">console</span><span class=\"o\">.</span><span
  class=\"n\">print</span><span class=\"p\">(</span><span class=\"n\">a</span><span
  class=\"p\">,</span> <span class=\"n\">style</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;purple&quot;</span><span class=\"p\">)</span>\n        <span
  class=\"k\">else</span><span class=\"p\">:</span>\n            <span class=\"k\">for</span>
  <span class=\"n\">a</span> <span class=\"ow\">in</span> <span class=\"n\">filtered</span><span
  class=\"p\">:</span>\n                <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">console</span><span class=\"o\">.</span><span class=\"n\">print</span><span
  class=\"p\">(</span><span class=\"n\">a</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for base_cli
long_description: ''
now: 2022-02-05 19:38:00.891399
path: base_cli.md
slug: markata/plugins/base_cli
status: published
title: base_cli.py
today: 2022-02-05
---

Markata's base command line commands.

This plugin enables
[`build`](https://markata.dev/markata/plugins/base_cli/#build-function)
and
[`list`](https://markata.dev/markata/plugins/base_cli/#list-function)
commands as part of the main markata cli.

## Building Your Site with the Cli

Your Markata Site can be build completely from the command line.

``` bash
markata build

# or if you prefer pipx
pipx run markata build
```

see the
[`build`](https://markata.dev/markata/plugins/base_cli/#build-function)
section for more examples.

## Listing your articles

Markata list is a tool to help list out artile attributes right to your
terminal.  This is very helpful to find articles on larger sites, or
debug what is getting picked up by markata.

``` bash
markata list --map 'str(date.year) + "," + title'
```

see the
[`list`](https://markata.dev/markata/plugins/base_cli/#list-function)
section for more examples.


---

## make_pretty `function`

This is a helper function that enables suppresses tracebacks from
frameworks like `click` that can make your traceback long and hard
to follow.  It also makes evrerything more colorful and easier to
follow.

??? "make_pretty source"
    ``` python
    def make_pretty() -> None:
        """
        This is a helper function that enables suppresses tracebacks from
        frameworks like `click` that can make your traceback long and hard
        to follow.  It also makes evrerything more colorful and easier to
        follow.
        """
        import click
        import pluggy
        import typer
        from rich import pretty as _pretty
        from rich import traceback

        _pretty.install()
        traceback.install(
            show_locals=True,
            suppress=[
                pluggy,
                click,
                typer,
            ],
        )
    ```


---

## cli `function`

Markata hook to implement base cli commands.

??? "cli source"
    ``` python
    def cli(app: typer.Typer, markata: "Markata") -> None:
        """
        Markata hook to implement base cli commands.
        """

        @app.command()
        def build(
            pretty: bool = True,
            quiet: bool = typer.Option(
                False,
                "--quiet",
                "-q",
            ),
            # to_dict: bool = False,
            verbose: bool = typer.Option(
                False,
                "--verbose",
                "-v",
            ),
            should_pdb: bool = typer.Option(
                False,
                "--pdb",
            ),
            profile: bool = True,
        ) -> None:
            """
            Markata's primary way of building your site for production.
            By default, running `markta build` will render your markdown to
            the `./markout` directory.

            ``` bash
            markata build
            ```

            If you are having an issue and want to pop immediately into a debugger
            upon failure you can pass the `--pdb` flag to the build command.

            ``` bash
            markata build  --pdb
            ```

            If you do not like the way rich looks, or its suppressing tracebaks you
            would like to remain visible you can use `--no-pretty`

            ``` bash
            markata build --no-pretty
            ```

            If you need to run without any console logging pass in the
            `--quiet` flag.

            ``` bash
            markata build --quiet
            ```

            `markta build` will automatically run the pyinstrument profiler
            while building your site if you have pyinstrument installed.  It
            will echo out your profile in the console as well as write it to
            `/_profile` on your built site. If you prefer not to run
            pyinstrument profiling, even when it is installed you can pass
            in `--no-profile`

            ``` bash
            markata build --no-profile
            ```
            """

            if pretty:
                make_pretty()

            if quiet:
                markata.console.quiet = True

            if verbose:
                markata.console.print("console options:", markata.console.options)

            if profile:
                markata.should_profile_cli = True
                markata.should_profile = True
                markata.configure()

            if should_pdb:
                pdb_run(markata.run)

            else:
                markata.run()

        @app.command()
        def list(
            map: str = "title",
            filter: str = "True",
            sort: str = "True",
            head: Optional[int] = None,
            tail: Optional[int] = None,
            include_empty: bool = False,
            reverse: bool = False,
            use_pager: bool = typer.Option(True, "--pager", "--no-pager"),
        ) -> None:
            """
            Provides a way run markatas, map, filter, and sort from the
            command line.  I personally use this more often than the build
            command while I am writing on a site with a large number of
            posts on it.  It makes slicing in by `templatekey`, `tag`, or
            `date` much easier.

            ### default list

            By default `markata list` will list all titles in a pager, for all posts
            being loaded by markata.

            ``` bash
            markata list
            ```

            ### Skip the pager

            Markata uses rich for its pager, it's pretty smart about when to
            use the pager or pass text to the next thing in the pipeline,
            but if you don't want to run a pager you can pass  `--no-pager`

            ``` bash
            markata list --no-pager
            ```

            ### List other attributes

            You can list any other attribute tied to your posts.  These are
            added through either your yaml frontmatter at the start of your
            post, or through the use of a plugin.


            ``` bash
            # the filepath of the post
            markata list --map path

            # the slug of the post (where it will show up on the site)
            markata list --map slug

            # the date of the post
            markata list --map date

            # the full raw content of the post
            markata list --map content
            ```

            ### List more than one attribute

            You can create new attributes as you map to echo out by
            combining existing attributes.

            ``` bash
            markata list --map 'title + " , " + slug'
            ```

            ### Using Python objects as map

            You can access attributes of each post attribute that you map
            over.  For instance on my blog, each post has a date that is a
            datetime object.  I can ask each post for its `date.year`

            ``` bash
            markata list --map date.year

            # combining this with title
            markata list --map 'str(date.year) + "," + title'
            ```

            ### Filtering posts

            Posts are filtered with python syntax, you will have all
            attributes tied to your posts available to filter with.

            ``` bash
            markata list --filter "'__' not in title"
            ```

            ### Filtering by dates

            If your site has dates tied to your posts you can filter by
            date.  On my blog this makes a ton of sense and is quite useful.
            On the Markata docs though it doesn't really make much sense,
            since there really isn't the idea of a post date there.

            ``` bash
            # listing today's posts
            markata list --filter "date==today"

            # listing this year's posts
            markata list --filter "date.year==today.year"
            ```

            ### Full Content Search

            You can also search the full content of each post for specific
            words.
            ``` bash

            markata list --filter "'python' in content"
            ```

            ### Filtering by frontmatter data

            I use a templateKey on my personal blog to determine which
            template to render the page with.  I can fitler my posts by a
            `til` (today i learned) key.

            ``` bash
            markata list --filter "templateKey=='til'"
            ```

            ### Combining filters

            Filters can be combined together quite like maps can, it's all
            just python syntax.

            ``` bash
            markata list --filter "templateKey=='til' and date == today"
            ```

            ### Sorting posts

            Posts can be sorted by attributes on your post, and they can
            even be reversed.

            ``` bash
            markta list --sort date
            markta list --sort date --reverse
            ```

            ### Putting it all together

            The real power of all this comes when you combine them all into
            lists that work for you and your workflow.  This really makes
            working on larger projects so much easier to find things.


            ### Making a fuzzy picker for your posts

            Here is a bash command to open an fzf picker for todays posts,
            then open it in your `$EDITOR`

            ``` bash
            markata list --map path --filter 'date==today' --sort date --reverse | fzf --preview 'bat --color always {}' | xargs -I {} $EDITOR {}
            ```

            ### Combining wtih nvim Telescope

            Here is the same command setup as a Telescope picker for neovim.

            ``` vim
            nnoremap <leader>et <cmd>Telescope find_files find_command=markata,list,--map,path,--filter,date==today<cr>
            ```

            If you have another way to open posts in your editor with
            `markata list` I would love to accept a PR to add it to the
            examples here.
            """

            markata.console.quiet = True

            tail = -tail if tail else tail
            filtered = markata.map(map, filter, sort)
            if not include_empty:
                filtered = [a for a in filtered if a != ""]
            filtered = filtered[tail:head]
            if reverse:
                filtered = reversed(filtered)

            markata.console.quiet = False
            if markata.console.is_terminal and use_pager:
                with markata.console.pager():
                    for a in filtered:
                        markata.console.print(a, style="purple")
            else:
                for a in filtered:
                    markata.console.print(a)
    ```


---

## pdb_run `function`

Wraps a function call with a post_mortem pdb debugger.

??? "pdb_run source"
    ``` python
    def pdb_run(func: Callable) -> None:
        """
        Wraps a function call with a post_mortem pdb debugger.
        """
        try:
            func()
        except Exception:
            extype, value, tb = sys.exc_info()
            traceback.print_exc()
            pdb.post_mortem(tb)
    ```


---

## build `function`

Markata's primary way of building your site for production.
By default, running `markta build` will render your markdown to
the `./markout` directory.

``` bash
markata build
```

If you are having an issue and want to pop immediately into a debugger
upon failure you can pass the `--pdb` flag to the build command.

``` bash
markata build  --pdb
```

If you do not like the way rich looks, or its suppressing tracebaks you
would like to remain visible you can use `--no-pretty`

``` bash
markata build --no-pretty
```

If you need to run without any console logging pass in the
`--quiet` flag.

``` bash
markata build --quiet
```

`markta build` will automatically run the pyinstrument profiler
while building your site if you have pyinstrument installed.  It
will echo out your profile in the console as well as write it to
`/_profile` on your built site. If you prefer not to run
pyinstrument profiling, even when it is installed you can pass
in `--no-profile`

``` bash
markata build --no-profile
```

??? "build source"
    ``` python
    def build(
            pretty: bool = True,
            quiet: bool = typer.Option(
                False,
                "--quiet",
                "-q",
            ),
            # to_dict: bool = False,
            verbose: bool = typer.Option(
                False,
                "--verbose",
                "-v",
            ),
            should_pdb: bool = typer.Option(
                False,
                "--pdb",
            ),
            profile: bool = True,
        ) -> None:
            """
            Markata's primary way of building your site for production.
            By default, running `markta build` will render your markdown to
            the `./markout` directory.

            ``` bash
            markata build
            ```

            If you are having an issue and want to pop immediately into a debugger
            upon failure you can pass the `--pdb` flag to the build command.

            ``` bash
            markata build  --pdb
            ```

            If you do not like the way rich looks, or its suppressing tracebaks you
            would like to remain visible you can use `--no-pretty`

            ``` bash
            markata build --no-pretty
            ```

            If you need to run without any console logging pass in the
            `--quiet` flag.

            ``` bash
            markata build --quiet
            ```

            `markta build` will automatically run the pyinstrument profiler
            while building your site if you have pyinstrument installed.  It
            will echo out your profile in the console as well as write it to
            `/_profile` on your built site. If you prefer not to run
            pyinstrument profiling, even when it is installed you can pass
            in `--no-profile`

            ``` bash
            markata build --no-profile
            ```
            """

            if pretty:
                make_pretty()

            if quiet:
                markata.console.quiet = True

            if verbose:
                markata.console.print("console options:", markata.console.options)

            if profile:
                markata.should_profile_cli = True
                markata.should_profile = True
                markata.configure()

            if should_pdb:
                pdb_run(markata.run)

            else:
                markata.run()
    ```


---

## list `function`

Provides a way run markatas, map, filter, and sort from the
command line.  I personally use this more often than the build
command while I am writing on a site with a large number of
posts on it.  It makes slicing in by `templatekey`, `tag`, or
`date` much easier.

### default list

By default `markata list` will list all titles in a pager, for all posts
being loaded by markata.

``` bash
markata list
```

### Skip the pager

Markata uses rich for its pager, it's pretty smart about when to
use the pager or pass text to the next thing in the pipeline,
but if you don't want to run a pager you can pass  `--no-pager`

``` bash
markata list --no-pager
```

### List other attributes

You can list any other attribute tied to your posts.  These are
added through either your yaml frontmatter at the start of your
post, or through the use of a plugin.


``` bash
# the filepath of the post
markata list --map path

# the slug of the post (where it will show up on the site)
markata list --map slug

# the date of the post
markata list --map date

# the full raw content of the post
markata list --map content
```

### List more than one attribute

You can create new attributes as you map to echo out by
combining existing attributes.

``` bash
markata list --map 'title + " , " + slug'
```

### Using Python objects as map

You can access attributes of each post attribute that you map
over.  For instance on my blog, each post has a date that is a
datetime object.  I can ask each post for its `date.year`

``` bash
markata list --map date.year

# combining this with title
markata list --map 'str(date.year) + "," + title'
```

### Filtering posts

Posts are filtered with python syntax, you will have all
attributes tied to your posts available to filter with.

``` bash
markata list --filter "'__' not in title"
```

### Filtering by dates

If your site has dates tied to your posts you can filter by
date.  On my blog this makes a ton of sense and is quite useful.
On the Markata docs though it doesn't really make much sense,
since there really isn't the idea of a post date there.

``` bash
# listing today's posts
markata list --filter "date==today"

# listing this year's posts
markata list --filter "date.year==today.year"
```

### Full Content Search

You can also search the full content of each post for specific
words.
``` bash

markata list --filter "'python' in content"
```

### Filtering by frontmatter data

I use a templateKey on my personal blog to determine which
template to render the page with.  I can fitler my posts by a
`til` (today i learned) key.

``` bash
markata list --filter "templateKey=='til'"
```

### Combining filters

Filters can be combined together quite like maps can, it's all
just python syntax.

``` bash
markata list --filter "templateKey=='til' and date == today"
```

### Sorting posts

Posts can be sorted by attributes on your post, and they can
even be reversed.

``` bash
markta list --sort date
markta list --sort date --reverse
```

### Putting it all together

The real power of all this comes when you combine them all into
lists that work for you and your workflow.  This really makes
working on larger projects so much easier to find things.


### Making a fuzzy picker for your posts

Here is a bash command to open an fzf picker for todays posts,
then open it in your `$EDITOR`

``` bash
markata list --map path --filter 'date==today' --sort date --reverse | fzf --preview 'bat --color always {}' | xargs -I {} $EDITOR {}
```

### Combining wtih nvim Telescope

Here is the same command setup as a Telescope picker for neovim.

``` vim
nnoremap <leader>et <cmd>Telescope find_files find_command=markata,list,--map,path,--filter,date==today<cr>
```

If you have another way to open posts in your editor with
`markata list` I would love to accept a PR to add it to the
examples here.

??? "list source"
    ``` python
    def list(
            map: str = "title",
            filter: str = "True",
            sort: str = "True",
            head: Optional[int] = None,
            tail: Optional[int] = None,
            include_empty: bool = False,
            reverse: bool = False,
            use_pager: bool = typer.Option(True, "--pager", "--no-pager"),
        ) -> None:
            """
            Provides a way run markatas, map, filter, and sort from the
            command line.  I personally use this more often than the build
            command while I am writing on a site with a large number of
            posts on it.  It makes slicing in by `templatekey`, `tag`, or
            `date` much easier.

            ### default list

            By default `markata list` will list all titles in a pager, for all posts
            being loaded by markata.

            ``` bash
            markata list
            ```

            ### Skip the pager

            Markata uses rich for its pager, it's pretty smart about when to
            use the pager or pass text to the next thing in the pipeline,
            but if you don't want to run a pager you can pass  `--no-pager`

            ``` bash
            markata list --no-pager
            ```

            ### List other attributes

            You can list any other attribute tied to your posts.  These are
            added through either your yaml frontmatter at the start of your
            post, or through the use of a plugin.


            ``` bash
            # the filepath of the post
            markata list --map path

            # the slug of the post (where it will show up on the site)
            markata list --map slug

            # the date of the post
            markata list --map date

            # the full raw content of the post
            markata list --map content
            ```

            ### List more than one attribute

            You can create new attributes as you map to echo out by
            combining existing attributes.

            ``` bash
            markata list --map 'title + " , " + slug'
            ```

            ### Using Python objects as map

            You can access attributes of each post attribute that you map
            over.  For instance on my blog, each post has a date that is a
            datetime object.  I can ask each post for its `date.year`

            ``` bash
            markata list --map date.year

            # combining this with title
            markata list --map 'str(date.year) + "," + title'
            ```

            ### Filtering posts

            Posts are filtered with python syntax, you will have all
            attributes tied to your posts available to filter with.

            ``` bash
            markata list --filter "'__' not in title"
            ```

            ### Filtering by dates

            If your site has dates tied to your posts you can filter by
            date.  On my blog this makes a ton of sense and is quite useful.
            On the Markata docs though it doesn't really make much sense,
            since there really isn't the idea of a post date there.

            ``` bash
            # listing today's posts
            markata list --filter "date==today"

            # listing this year's posts
            markata list --filter "date.year==today.year"
            ```

            ### Full Content Search

            You can also search the full content of each post for specific
            words.
            ``` bash

            markata list --filter "'python' in content"
            ```

            ### Filtering by frontmatter data

            I use a templateKey on my personal blog to determine which
            template to render the page with.  I can fitler my posts by a
            `til` (today i learned) key.

            ``` bash
            markata list --filter "templateKey=='til'"
            ```

            ### Combining filters

            Filters can be combined together quite like maps can, it's all
            just python syntax.

            ``` bash
            markata list --filter "templateKey=='til' and date == today"
            ```

            ### Sorting posts

            Posts can be sorted by attributes on your post, and they can
            even be reversed.

            ``` bash
            markta list --sort date
            markta list --sort date --reverse
            ```

            ### Putting it all together

            The real power of all this comes when you combine them all into
            lists that work for you and your workflow.  This really makes
            working on larger projects so much easier to find things.


            ### Making a fuzzy picker for your posts

            Here is a bash command to open an fzf picker for todays posts,
            then open it in your `$EDITOR`

            ``` bash
            markata list --map path --filter 'date==today' --sort date --reverse | fzf --preview 'bat --color always {}' | xargs -I {} $EDITOR {}
            ```

            ### Combining wtih nvim Telescope

            Here is the same command setup as a Telescope picker for neovim.

            ``` vim
            nnoremap <leader>et <cmd>Telescope find_files find_command=markata,list,--map,path,--filter,date==today<cr>
            ```

            If you have another way to open posts in your editor with
            `markata list` I would love to accept a PR to add it to the
            examples here.
            """

            markata.console.quiet = True

            tail = -tail if tail else tail
            filtered = markata.map(map, filter, sort)
            if not include_empty:
                filtered = [a for a in filtered if a != ""]
            filtered = filtered[tail:head]
            if reverse:
                filtered = reversed(filtered)

            markata.console.quiet = False
            if markata.console.is_terminal and use_pager:
                with markata.console.pager():
                    for a in filtered:
                        markata.console.print(a, style="purple")
            else:
                for a in filtered:
                    markata.console.print(a)
    ```