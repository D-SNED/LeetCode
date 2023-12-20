<h2><a href="https://leetcode.com/problems/merge-strings-alternately/">1768. Merge Strings Alternately</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Y</span>ou</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>re</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">g</span>iven</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>wo</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">st</span>rings</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>ord1</span></span></code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>nd</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>ord2</span></span></code><span class="extension-adhd-reader-wrapper">. <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">M</span>erge</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">st</span>rings</span> by <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ad</span>ding</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">le</span>tters</span> in <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">alt</span>ernating</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">or</span>der,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">st</span>arting</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>ith</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>ord1</span></span></code><span class="extension-adhd-reader-wrapper">. If a <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">st</span>ring</span> is <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">lo</span>nger</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>han</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ot</span>her,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ap</span>pend</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">add</span>itional</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">le</span>tters</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">o</span>nto</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">e</span>nd</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">me</span>rged</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">st</span>ring.</span></span></p>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Re</span>turn</span> </span><em><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">me</span>rged</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">st</span>ring.</span></span></em></p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>

<pre><strong>Input:</strong> word1 = "abc", word2 = "pqr"
<strong>Output:</strong> "apbqcr"
<strong>Explanation:</strong>&nbsp;The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>

<pre><strong>Input:</strong> word1 = "ab", word2 = "pqrs"
<strong>Output:</strong> "apbqrs"
<strong>Explanation:</strong>&nbsp;Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 3:</span></strong></p>

<pre><strong>Input:</strong> word1 = "abcd", word2 = "pq"
<strong>Output:</strong> "apbqcd"
<strong>Explanation:</strong>&nbsp;Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li><code>1 &lt;= word1.length, word2.length &lt;= 100</code></li>
	<li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>
</ul></div>