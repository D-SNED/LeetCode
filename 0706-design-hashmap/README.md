<h2><a href="https://leetcode.com/problems/design-hashmap/">706. Design HashMap</a></h2><h3>Easy</h3><hr><div><p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">De</span>sign</span> a <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ha</span>shMap</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">wi</span>thout</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">u</span>sing</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">a</span>ny</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">bu</span>ilt-in</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">h</span>ash</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>able</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">lib</span>raries.</span></span></p>

<p class="extension-adhd-reader-p"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Imp</span>lement</span> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">t</span>he</span> </span><code><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">MyH</span>ashMap</span></span></code><span class="extension-adhd-reader-wrapper"> <span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">cl</span>ass:</span></span></p>

<ul>
	<li><code>MyHashMap()</code> initializes the object with an empty map.</li>
	<li><code>void put(int key, int value)</code> inserts a <code>(key, value)</code> pair into the HashMap. If the <code>key</code> already exists in the map, update the corresponding <code>value</code>.</li>
	<li><code>int get(int key)</code> returns the <code>value</code> to which the specified <code>key</code> is mapped, or <code>-1</code> if this map contains no mapping for the <code>key</code>.</li>
	<li><code>void remove(key)</code> removes the <code>key</code> and its corresponding <code>value</code> if the map contains the mapping for the <code>key</code>.</li>
</ul>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong class="example"><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Ex</span>ample</span> 1:</span></strong></p>

<pre><strong>Input</strong>
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
<strong>Output</strong>
[null, null, null, 1, -1, null, 1, null, -1]

<strong>Explanation</strong>
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
</pre>

<p class="extension-adhd-reader-p">&nbsp;</p>
<p class="extension-adhd-reader-p"><strong><span class="extension-adhd-reader-wrapper"><span class="extension-adhd-reader-container"><span class="extension-adhd-reader-boldify">Cons</span>traints:</span></span></strong></p>

<ul>
	<li><code>0 &lt;= key, value &lt;= 10<sup>6</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>put</code>, <code>get</code>, and <code>remove</code>.</li>
</ul>
</div>