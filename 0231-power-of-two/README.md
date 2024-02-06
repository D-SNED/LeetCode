<h2><a href="https://leetcode.com/problems/power-of-two/">231. Power of Two</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">G</span>iven</span> an <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>teger</span> </span><code>n</code><span class="extension-adhd-reader-wrapper">, <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>turn</span> </span><em><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>rue</span></span></code><span class="extension-adhd-reader-wrapper"> if it is a <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">p</span>ower</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>wo.</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Oth</span>erwise,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>turn</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">f</span>alse</span></span></code></em>.</p>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper">An <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>teger</span> </span><code>n</code><span class="extension-adhd-reader-wrapper"> is a <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">p</span>ower</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>wo,</span> if <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>here</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ex</span>ists</span> an <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>teger</span> </span><code>x</code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">s</span>uch</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>hat</span> </span><code><span class="extension-adhd-reader-wrapper">n == 2</span><sup>x</sup></code>.</p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>

<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>0</sup> = 1
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>

<pre><strong>Input:</strong> n = 16
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>4</sup> = 16
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 3:</span></strong></p>

<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> false
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p class="extension-adhd-reader-p">&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without loops/recursion?</div>