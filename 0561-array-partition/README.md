<h2><a href="https://leetcode.com/problems/array-partition/">561. Array Partition</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">G</span>iven</span> an <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>teger</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>rray</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">n</span>ums</span></span></code> of <code>2n</code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">int</span>egers,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">g</span>roup</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>hese</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>tegers</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">i</span>nto</span> </span><code>n</code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">p</span>airs</span> </span><code>(a<sub>1</sub><span class="extension-adhd-reader-wrapper">, b</span><sub>1</sub><span class="extension-adhd-reader-wrapper">), (a</span><sub>2</sub><span class="extension-adhd-reader-wrapper">, b</span><sub>2</sub><span class="extension-adhd-reader-wrapper">), <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">.</span>..,</span> (a</span><sub>n</sub><span class="extension-adhd-reader-wrapper">, b</span><sub>n</sub>)</code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">s</span>uch</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>hat</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">s</span>um</span> of </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">m</span>in(a</span></span><sub>i</sub><span class="extension-adhd-reader-wrapper">, b</span><sub>i</sub>)</code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">f</span>or</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>ll</span> </span><code>i</code> is <strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">max</span>imized</span></span></strong><span class="extension-adhd-reader-wrapper">. <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Re</span>turn</span></span><em><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">max</span>imized</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">s</span>um</span></span></em>.</p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>

<pre><strong>Input:</strong> nums = [1,4,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -&gt; min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -&gt; min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -&gt; min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>

<pre><strong>Input:</strong> nums = [6,2,6,5,1,2]
<strong>Output:</strong> 9
<strong>Explanation:</strong> The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>nums.length == 2 * n</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>
</div>