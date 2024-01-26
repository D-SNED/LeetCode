<h2><a href="https://leetcode.com/problems/delete-greatest-value-in-each-row/">2500. Delete Greatest Value in Each Row</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Y</span>ou</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>re</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">g</span>iven</span> an </span><code><span class="extension-adhd-reader-wrapper">m x n</span></code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ma</span>trix</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">g</span>rid</span></span></code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">con</span>sisting</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">po</span>sitive</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">int</span>egers.</span></span></p>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Pe</span>rform</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">fol</span>lowing</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ope</span>ration</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">u</span>ntil</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">g</span>rid</span></span></code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">be</span>comes</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">em</span>pty:</span></span></p>

<ul>
	<li>Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.</li>
	<li>Add the maximum of deleted elements to the answer.</li>
</ul>

<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">N</span>ote</span></span></strong><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>hat</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">nu</span>mber</span> of <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">co</span>lumns</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">dec</span>reases</span> by <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">o</span>ne</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>fter</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">e</span>ach</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ope</span>ration.</span></span></p>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Re</span>turn</span> </span><em><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">an</span>swer</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>fter</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">per</span>forming</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">ope</span>rations</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">des</span>cribed</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>bove</span></span></em>.</p>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/10/19/q1ex1.jpg" style="width: 600px; height: 135px;">
<pre><strong>Input:</strong> grid = [[1,2,4],[3,3,1]]
<strong>Output:</strong> 8
<strong>Explanation:</strong> The diagram above shows the removed values in each step.
- In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
- In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
- In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
The final answer = 4 + 3 + 1 = 8.
</pre>

<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 2:</span></strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/10/19/q1ex2.jpg" style="width: 83px; height: 83px;">
<pre><strong>Input:</strong> grid = [[10]]
<strong>Output:</strong> 10
<strong>Explanation:</strong> The diagram above shows the removed values in each step.
- In the first operation, we remove 10 from the first row. We add 10 to the answer.
The final answer = 10.
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>
</div>