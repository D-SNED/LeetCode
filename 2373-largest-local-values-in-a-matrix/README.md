<h2><a href="https://leetcode.com/problems/largest-local-values-in-a-matrix/">2373. Largest Local Values in a Matrix</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Y</span>ou</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>re</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">g</span>iven</span> an </span><code><span class="extension-adhd-reader-wrapper">n x n</span></code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>teger</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ma</span>trix</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">g</span>rid</span></span></code>.</p>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ge</span>nerate</span> an <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">in</span>teger</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ma</span>trix</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ma</span>xLocal</span></span></code><span class="extension-adhd-reader-wrapper"> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">s</span>ize</span> </span><code><span class="extension-adhd-reader-wrapper">(n - 2) x (n - 2)</span></code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">s</span>uch</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>hat:</span></span></p>

<ul>
	<li><code>maxLocal[i][j]</code> is equal to the <strong>largest</strong> value of the <code>3 x 3</code> matrix in <code>grid</code> centered around row <code>i + 1</code> and column <code>j + 1</code>.</li>
</ul>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper">In <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">o</span>ther</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">wo</span>rds,</span> we <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">w</span>ant</span> to <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">f</span>ind</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">la</span>rgest</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">v</span>alue</span> in <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">e</span>very</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">con</span>tiguous</span> </span><code><span class="extension-adhd-reader-wrapper">3 x 3</span></code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ma</span>trix</span> in </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">g</span>rid</span></span></code>.</p>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Re</span>turn</span> </span><em><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">gen</span>erated</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ma</span>trix</span></span></em>.</p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/06/21/ex1.png" style="width: 371px; height: 210px;">
<pre><strong>Input:</strong> grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
<strong>Output:</strong> [[9,9],[8,6]]
<strong>Explanation:</strong> The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/07/02/ex2new2.png" style="width: 436px; height: 240px;">
<pre><strong>Input:</strong> grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
<strong>Output:</strong> [[2,2,2],[2,2,2],[2,2,2]]
<strong>Explanation:</strong> Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li><code>n == grid.length == grid[i].length</code></li>
	<li><code>3 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>
</div>