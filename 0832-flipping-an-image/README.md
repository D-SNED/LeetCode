<h2><a href="https://leetcode.com/problems/flipping-an-image/">832. Flipping an Image</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">G</span>iven</span> an </span><code><span class="extension-adhd-reader-wrapper">n x n</span></code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">bi</span>nary</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ma</span>trix</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">i</span>mage</span></span></code><span class="extension-adhd-reader-wrapper">, <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">f</span>lip</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">i</span>mage</span> </span><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">hori</span>zontally</span></span></strong><span class="extension-adhd-reader-wrapper">, <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>hen</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>vert</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">i</span>t,</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>nd</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>turn</span> </span><em><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">res</span>ulting</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">i</span>mage</span></span></em>.</p>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper">To <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">f</span>lip</span> an <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">i</span>mage</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">hori</span>zontally</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">m</span>eans</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>hat</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">e</span>ach</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">r</span>ow</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">i</span>mage</span> is <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">rev</span>ersed.</span></span></p>

<ul>
	<li>For example, flipping <code>[1,1,0]</code> horizontally results in <code>[0,1,1]</code>.</li>
</ul>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper">To <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>vert</span> an <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">i</span>mage</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">m</span>eans</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>hat</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">e</span>ach</span> </span><code>0</code><span class="extension-adhd-reader-wrapper"> is <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>placed</span> by </span><code>1</code><span class="extension-adhd-reader-wrapper">, <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>nd</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">e</span>ach</span> </span><code>1</code><span class="extension-adhd-reader-wrapper"> is <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">re</span>placed</span> by </span><code>0</code>.</p>

<ul>
	<li>For example, inverting <code>[0,1,1]</code> results in <code>[1,0,0]</code>.</li>
</ul>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>

<pre><strong>Input:</strong> image = [[1,1,0],[1,0,1],[0,0,0]]
<strong>Output:</strong> [[1,0,0],[0,1,0],[1,1,1]]
<strong>Explanation:</strong> First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>

<pre><strong>Input:</strong> image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
<strong>Output:</strong> [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
<strong>Explanation:</strong> First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li><code>n == image.length</code></li>
	<li><code>n == image[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>images[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>
</div>