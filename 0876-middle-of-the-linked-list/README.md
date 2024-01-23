<h2><a href="https://leetcode.com/problems/middle-of-the-linked-list/">876. Middle of the Linked List</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">G</span>iven</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">h</span>ead</span></span></code><span class="extension-adhd-reader-wrapper"> of a <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">si</span>ngly</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">li</span>nked</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">l</span>ist,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>turn</span> </span><em><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">mi</span>ddle</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">n</span>ode</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">li</span>nked</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">l</span>ist</span></span></em>.</p>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper">If <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>here</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>re</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>wo</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">mi</span>ddle</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">no</span>des,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>turn</span> </span><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">se</span>cond</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">mi</span>ddle</span></span></strong><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">n</span>ode.</span></span></p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg" style="width: 544px; height: 65px;">
<pre><strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [3,4,5]
<strong>Explanation:</strong> The middle node of the list is node 3.
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg" style="width: 664px; height: 65px;">
<pre><strong>Input:</strong> head = [1,2,3,4,5,6]
<strong>Output:</strong> [4,5,6]
<strong>Explanation:</strong> Since the list has two middle nodes with values 3 and 4, we return the second one.
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 100]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 100</code></li>
</ul>
</div>