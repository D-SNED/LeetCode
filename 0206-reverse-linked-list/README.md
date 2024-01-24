<h2><a href="https://leetcode.com/problems/reverse-linked-list/">206. Reverse Linked List</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">G</span>iven</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">h</span>ead</span></span></code><span class="extension-adhd-reader-wrapper"> of a <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">si</span>ngly</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">li</span>nked</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">l</span>ist,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>verse</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">l</span>ist,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>nd</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>turn</span> </span><em><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>versed</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">l</span>ist</span></span></em>.</p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg" style="width: 542px; height: 222px;">
<pre><strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [5,4,3,2,1]
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg" style="width: 182px; height: 222px;">
<pre><strong>Input:</strong> head = [1,2]
<strong>Output:</strong> [2,1]
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 3:</span></strong></p>

<pre><strong>Input:</strong> head = []
<strong>Output:</strong> []
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li>The number of nodes in the list is the range <code>[0, 5000]</code>.</li>
	<li><code>-5000 &lt;= Node.val &lt;= 5000</code></li>
</ul>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Fo</span>llow</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">u</span>p:</span></span></strong><span class="extension-adhd-reader-wrapper"> A <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">li</span>nked</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">l</span>ist</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">c</span>an</span> be <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>versed</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ei</span>ther</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ite</span>ratively</span> or <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">recu</span>rsively.</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">C</span>ould</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">y</span>ou</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">imp</span>lement</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">b</span>oth?</span></span></p>
</div>