<h2><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list/">83. Remove Duplicates from Sorted List</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">G</span>iven</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">h</span>ead</span></span></code><span class="extension-adhd-reader-wrapper"> of a <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">so</span>rted</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">li</span>nked</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">l</span>ist,</span> </span><em><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">de</span>lete</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>ll</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">dup</span>licates</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">s</span>uch</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>hat</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">e</span>ach</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">el</span>ement</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ap</span>pears</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">o</span>nly</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">o</span>nce</span></span></em><span class="extension-adhd-reader-wrapper">. <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Re</span>turn</span> </span><em><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">li</span>nked</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">l</span>ist</span> </span><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">so</span>rted</span></span></strong><span class="extension-adhd-reader-wrapper"> as <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>ell</span></span></em>.</p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/list1.jpg" style="width: 302px; height: 242px;">
<pre><strong>Input:</strong> head = [1,1,2]
<strong>Output:</strong> [1,2]
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/list2.jpg" style="width: 542px; height: 222px;">
<pre><strong>Input:</strong> head = [1,1,2,3,3]
<strong>Output:</strong> [1,2,3]
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 300]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li>The list is guaranteed to be <strong>sorted</strong> in ascending order.</li>
</ul>
</div>