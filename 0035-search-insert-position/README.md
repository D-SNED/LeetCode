<h2><a href="https://leetcode.com/problems/search-insert-position/">35. Search Insert Position</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">G</span>iven</span> a <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">so</span>rted</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>rray</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">di</span>stinct</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>tegers</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>nd</span> a <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ta</span>rget</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">va</span>lue,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>turn</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">i</span>ndex</span> if <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ta</span>rget</span> is <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">fo</span>und.</span> If <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">n</span>ot,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>turn</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">i</span>ndex</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>here</span> it <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>ould</span> be if it <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>ere</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>serted</span> in <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">or</span>der.</span></span></p>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Y</span>ou</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">m</span>ust</span>&nbsp;<span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>rite</span> an <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">alg</span>orithm</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>ith</span>&nbsp;</span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">O</span>(log</span> n)</span></code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ru</span>ntime</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">com</span>plexity.</span></span></p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>

<pre><strong>Input:</strong> nums = [1,3,5,6], target = 5
<strong>Output:</strong> 2
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>

<pre><strong>Input:</strong> nums = [1,3,5,6], target = 2
<strong>Output:</strong> 1
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 3:</span></strong></p>

<pre><strong>Input:</strong> nums = [1,3,5,6], target = 7
<strong>Output:</strong> 4
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> contains <strong>distinct</strong> values sorted in <strong>ascending</strong> order.</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>
</div>