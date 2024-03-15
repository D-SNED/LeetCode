<h2><a href="https://leetcode.com/problems/maximum-number-of-balloons/">1189. Maximum Number of Balloons</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">G</span>iven</span> a <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">st</span>ring</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>ext</span></span></code><span class="extension-adhd-reader-wrapper">, <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">y</span>ou</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>ant</span> to <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">u</span>se</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">cha</span>racters</span> of </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>ext</span></span></code><span class="extension-adhd-reader-wrapper"> to <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">f</span>orm</span> as <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">m</span>any</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ins</span>tances</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>ord</span> </span><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">"ba</span>lloon"</span></span></strong><span class="extension-adhd-reader-wrapper"> as <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">pos</span>sible.</span></span></p>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Y</span>ou</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">c</span>an</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">u</span>se</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">e</span>ach</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">cha</span>racter</span> in </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>ext</span></span></code> <strong><span class="extension-adhd-reader-wrapper">at <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">m</span>ost</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">o</span>nce</span></span></strong><span class="extension-adhd-reader-wrapper">. <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Re</span>turn</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ma</span>ximum</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">nu</span>mber</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ins</span>tances</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>hat</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">c</span>an</span> be <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">fo</span>rmed.</span></span></p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>

<p class="extension-adhd-reader-p"><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG" style="width: 132px; height: 35px;"></strong></p>

<pre><strong>Input:</strong> text = "nlaebolko"
<strong>Output:</strong> 1
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>

<p class="extension-adhd-reader-p"><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG" style="width: 267px; height: 35px;"></strong></p>

<pre><strong>Input:</strong> text = "loonbalxballpoon"
<strong>Output:</strong> 2
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 3:</span></strong></p>

<pre><strong>Input:</strong> text = "leetcode"
<strong>Output:</strong> 0
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 10<sup>4</sup></code></li>
	<li><code>text</code> consists of lower case English letters only.</li>
</ul>
</div>