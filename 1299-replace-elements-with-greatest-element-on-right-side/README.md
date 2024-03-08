<h2><a href="https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/">1299. Replace Elements with Greatest Element on Right Side</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">G</span>iven</span> an <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>rray</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>rr</span></span></code><span class="extension-adhd-reader-wrapper">,&nbsp;<span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>place</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">e</span>very</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">el</span>ement</span> in <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>hat</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>rray</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>ith</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">gr</span>eatest</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">el</span>ement</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>mong</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">el</span>ements</span> to <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">i</span>ts</span>&nbsp;<span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ri</span>ght,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>nd</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>place</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">l</span>ast</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">el</span>ement</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>ith</span> </span><code>-1</code>.</p>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">A</span>fter</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">d</span>oing</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">s</span>o,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>turn</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ar</span>ray.</span></span></p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>

<pre><strong>Input:</strong> arr = [17,18,5,4,6,1]
<strong>Output:</strong> [18,6,6,6,1,-1]
<strong>Explanation:</strong> 
- index 0 --&gt; the greatest element to the right of index 0 is index 1 (18).
- index 1 --&gt; the greatest element to the right of index 1 is index 4 (6).
- index 2 --&gt; the greatest element to the right of index 2 is index 4 (6).
- index 3 --&gt; the greatest element to the right of index 3 is index 4 (6).
- index 4 --&gt; the greatest element to the right of index 4 is index 5 (1).
- index 5 --&gt; there are no elements to the right of index 5, so we put -1.
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>

<pre><strong>Input:</strong> arr = [400]
<strong>Output:</strong> [-1]
<strong>Explanation:</strong> There are no elements to the right of index 0.
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
</ul>
</div>