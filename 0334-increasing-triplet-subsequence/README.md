<h2><a href="https://leetcode.com/problems/increasing-triplet-subsequence/">334. Increasing Triplet Subsequence</a></h2><h3>Medium</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">G</span>iven</span> an <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>teger</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>rray</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">n</span>ums</span></span></code><span class="extension-adhd-reader-wrapper">, <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>turn</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>rue</span></span></code><em><span class="extension-adhd-reader-wrapper"> if <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>here</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ex</span>ists</span> a <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">tr</span>iple</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>dices</span> </span></em><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">(</span>i,</span> j, k)</span></code><em><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">s</span>uch</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>hat</span> </span></em><code><span class="extension-adhd-reader-wrapper">i &lt; j &lt; k</span></code><em><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>nd</span> </span></em><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">nu</span>ms[i]</span> &lt; <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">nu</span>ms[j]</span> &lt; <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">nu</span>ms[k]</span></span></code><span class="extension-adhd-reader-wrapper">. If no <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">s</span>uch</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>dices</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ex</span>ists,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>turn</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">f</span>alse</span></span></code>.</p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> Any triplet where i &lt; j &lt; k is valid.
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>

<pre><strong>Input:</strong> nums = [5,4,3,2,1]
<strong>Output:</strong> false
<strong>Explanation:</strong> No triplet exists.
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 3:</span></strong></p>

<pre><strong>Input:</strong> nums = [2,1,5,0,4,6]
<strong>Output:</strong> true
<strong>Explanation:</strong> The triplet (3, 4, 5) is valid because nums[3] == 0 &lt; nums[4] == 4 &lt; nums[5] == 6.
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p class="extension-adhd-reader-p">&nbsp;</p>
<strong>Follow up:</strong> Could you implement a solution that runs in <code>O(n)</code> time complexity and <code>O(1)</code> space complexity?</div>