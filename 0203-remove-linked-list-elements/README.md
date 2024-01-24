<h2><a href="https://leetcode.com/problems/remove-linked-list-elements/">203. Remove Linked List Elements</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">G</span>iven</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">h</span>ead</span></span></code><span class="extension-adhd-reader-wrapper"> of a <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">li</span>nked</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">l</span>ist</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>nd</span> an <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>teger</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">v</span>al</span></span></code><span class="extension-adhd-reader-wrapper">, <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>move</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>ll</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">n</span>odes</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">li</span>nked</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">l</span>ist</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>hat</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">h</span>as</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">No</span>de.val</span> == <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">v</span>al</span></span></code><span class="extension-adhd-reader-wrapper">, <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>nd</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>turn</span> </span><em><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">n</span>ew</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">h</span>ead</span></span></em>.</p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg" style="width: 500px; height: 142px;">
<pre><strong>Input:</strong> head = [1,2,6,3,4,5,6], val = 6
<strong>Output:</strong> [1,2,3,4,5]
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>

<pre><strong>Input:</strong> head = [], val = 1
<strong>Output:</strong> []
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 3:</span></strong></p>

<pre><strong>Input:</strong> head = [7,7,7,7], val = 7
<strong>Output:</strong> []
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 50</code></li>
	<li><code>0 &lt;= val &lt;= 50</code></li>
</ul>
</div>