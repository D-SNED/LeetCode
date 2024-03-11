<h2><a href="https://leetcode.com/problems/longest-common-prefix/">14. Longest Common Prefix</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">W</span>rite</span> a <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">fu</span>nction</span> to <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">f</span>ind</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">lo</span>ngest</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">co</span>mmon</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">pr</span>efix</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">st</span>ring</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">am</span>ongst</span> an <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>rray</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">st</span>rings.</span></span></p>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper">If <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>here</span> is no <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">co</span>mmon</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">pr</span>efix,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>turn</span> an <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">e</span>mpty</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">st</span>ring</span> </span><code>""</code>.</p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>

<pre><strong>Input:</strong> strs = ["flower","flow","flight"]
<strong>Output:</strong> "fl"
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>

<pre><strong>Input:</strong> strs = ["dog","racecar","car"]
<strong>Output:</strong> ""
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> consists of only lowercase English letters.</li>
</ul>
</div>