<h2><a href="https://leetcode.com/problems/length-of-last-word/">58. Length of Last Word</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">G</span>iven</span> a <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">st</span>ring</span> </span><code>s</code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">con</span>sisting</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>ords</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>nd</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">sp</span>aces,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>turn</span> </span><em><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">le</span>ngth</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> </span><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">l</span>ast</span></span></strong><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>ord</span> in <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">st</span>ring.</span></span></em></p>

<p class="extension-adhd-reader-p">A <strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>ord</span></span></strong><span class="extension-adhd-reader-wrapper"> is a <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ma</span>ximal</span> </span><span data-keyword="substring-nonempty"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">sub</span>string</span></span></span><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">con</span>sisting</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">non</span>-space</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">cha</span>racters</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">o</span>nly.</span></span></p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>

<pre><strong>Input:</strong> s = "Hello World"
<strong>Output:</strong> 5
<strong>Explanation:</strong> The last word is "World" with length 5.
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>

<pre><strong>Input:</strong> s = "   fly me   to   the moon  "
<strong>Output:</strong> 4
<strong>Explanation:</strong> The last word is "moon" with length 4.
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 3:</span></strong></p>

<pre><strong>Input:</strong> s = "luffy is still joyboy"
<strong>Output:</strong> 6
<strong>Explanation:</strong> The last word is "joyboy" with length 6.
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of only English letters and spaces <code>' '</code>.</li>
	<li>There will be at least one word in <code>s</code>.</li>
</ul>
</div>