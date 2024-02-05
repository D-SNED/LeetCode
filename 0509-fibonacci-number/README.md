<h2><a href="https://leetcode.com/problems/fibonacci-number/">509. Fibonacci Number</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">T</span>he</span> </span><b><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Fib</span>onacci</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">nu</span>mbers</span></span></b><span class="extension-adhd-reader-wrapper">, <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">co</span>mmonly</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">de</span>noted</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">F</span>(n)</span></span></code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">f</span>orm</span> a <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">seq</span>uence,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ca</span>lled</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> </span><b><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Fib</span>onacci</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">se</span>quence</span></span></b><span class="extension-adhd-reader-wrapper">, <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">s</span>uch</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>hat</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">e</span>ach</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">nu</span>mber</span> is <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">s</span>um</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>wo</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">pre</span>ceding</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">o</span>nes,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">st</span>arting</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">f</span>rom</span> </span><code>0</code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>nd</span> </span><code>1</code><span class="extension-adhd-reader-wrapper">. <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">T</span>hat</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">i</span>s,</span></span></p>

<pre>F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n &gt; 1.
</pre>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">G</span>iven</span> </span><code>n</code><span class="extension-adhd-reader-wrapper">, <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">cal</span>culate</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">F</span>(n)</span></span></code>.</p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>

<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> F(2) = F(1) + F(0) = 1 + 0 = 1.
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>

<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> F(3) = F(2) + F(1) = 1 + 1 = 2.
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 3:</span></strong></p>

<pre><strong>Input:</strong> n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> F(4) = F(3) + F(2) = 2 + 1 = 3.
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 30</code></li>
</ul>
</div>