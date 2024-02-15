<h2><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/">153. Find Minimum in Rotated Sorted Array</a></h2><h3>Medium</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Su</span>ppose</span> an <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>rray</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">le</span>ngth</span> </span><code>n</code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">so</span>rted</span> in <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">asc</span>ending</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">o</span>rder</span> is </span><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ro</span>tated</span></span></strong><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">be</span>tween</span> </span><code>1</code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>nd</span> </span><code>n</code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ti</span>mes.</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">F</span>or</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ex</span>ample,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>rray</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">n</span>ums</span> = <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">[0,1,</span>2,4,5,6,7]</span></span></code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">m</span>ight</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">be</span>come:</span></span></p>

<ul>
	<li><code>[4,5,6,7,0,1,2]</code> if it was rotated <code>4</code> times.</li>
	<li><code>[0,1,2,4,5,6,7]</code> if it was rotated <code>7</code> times.</li>
</ul>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">No</span>tice</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>hat</span> </span><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ro</span>tating</span></span></strong><span class="extension-adhd-reader-wrapper"> an <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>rray</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">[a</span>[0],</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>[1],</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>[2],</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">.</span>..,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a[</span>n-1]]</span></span></code><span class="extension-adhd-reader-wrapper"> 1 <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>ime</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>sults</span> in <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>rray</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">[a</span>[n-1],</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>[0],</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>[1],</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>[2],</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">.</span>..,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a[</span>n-2]]</span></span></code>.</p>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">G</span>iven</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">so</span>rted</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ro</span>tated</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>rray</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">n</span>ums</span></span></code> of <strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">un</span>ique</span></span></strong><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ele</span>ments,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>turn</span> </span><em><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">mi</span>nimum</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">el</span>ement</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>his</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>rray</span></span></em>.</p>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Y</span>ou</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">m</span>ust</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>rite</span> an <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">alg</span>orithm</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>hat</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">r</span>uns</span> in&nbsp;</span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">O</span>(log</span> n) <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>ime.</span></span></code></p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>

<pre><strong>Input:</strong> nums = [3,4,5,1,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The original array was [1,2,3,4,5] rotated 3 times.
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>

<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 3:</span></strong></p>

<pre><strong>Input:</strong> nums = [11,13,15,17]
<strong>Output:</strong> 11
<strong>Explanation:</strong> The original array was [11,13,15,17] and it was rotated 4 times. 
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>-5000 &lt;= nums[i] &lt;= 5000</code></li>
	<li>All the integers of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is sorted and rotated between <code>1</code> and <code>n</code> times.</li>
</ul>
</div>