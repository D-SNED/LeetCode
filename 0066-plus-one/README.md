<h2><a href="https://leetcode.com/problems/plus-one/">66. Plus One</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Y</span>ou</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>re</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">g</span>iven</span> a </span><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">l</span>arge</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>teger</span></span></strong><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">rep</span>resented</span> as an <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>teger</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>rray</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">di</span>gits</span></span></code><span class="extension-adhd-reader-wrapper">, <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>here</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">e</span>ach</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">dig</span>its[i]</span></span></code><span class="extension-adhd-reader-wrapper"> is <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> </span><code>i<sup>th</sup></code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">d</span>igit</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>teger.</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">T</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">di</span>gits</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>re</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">or</span>dered</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">f</span>rom</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">m</span>ost</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">sig</span>nificant</span> to <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">l</span>east</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">sig</span>nificant</span> in <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">left</span>-to-right</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">or</span>der.</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">T</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">l</span>arge</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>teger</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">d</span>oes</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">n</span>ot</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">co</span>ntain</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>ny</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">le</span>ading</span> </span><code>0</code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">'</span>s.</span></span></p>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Inc</span>rement</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">l</span>arge</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>teger</span> by <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">o</span>ne</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>nd</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>turn</span> </span><em><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">res</span>ulting</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>rray</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">di</span>gits</span></span></em>.</p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>

<pre><strong>Input:</strong> digits = [1,2,3]
<strong>Output:</strong> [1,2,4]
<strong>Explanation:</strong> The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>

<pre><strong>Input:</strong> digits = [4,3,2,1]
<strong>Output:</strong> [4,3,2,2]
<strong>Explanation:</strong> The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 3:</span></strong></p>

<pre><strong>Input:</strong> digits = [9]
<strong>Output:</strong> [1,0]
<strong>Explanation:</strong> The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li><code>1 &lt;= digits.length &lt;= 100</code></li>
	<li><code>0 &lt;= digits[i] &lt;= 9</code></li>
	<li><code>digits</code> does not contain any leading <code>0</code>'s.</li>
</ul>
</div>