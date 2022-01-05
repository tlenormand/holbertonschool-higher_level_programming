# 0x04. Python - More Data Structures: Set, Dictionary

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/XCPKZqM_ZWGW2un62Rg3qw" title="Data structures" target="_blank">Data structures</a> </li>
<li><a href="/rltoken/z4yFKyKQTfQTZZj9Ji5J3g" title="Lambda, filter, reduce and map" target="_blank">Lambda, filter, reduce and map</a> </li>
<li><a href="/rltoken/AT-UtsGuhgIzQSwSdKvckw" title="Learn to Program 12 Lambda Map Filter Reduce" target="_blank">Learn to Program 12 Lambda Map Filter Reduce</a> </li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>python3</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/DVEd729oRoWJl-ektHvuNg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>What are sets and how to use them</li>
<li>What are the most common methods of set and how to use them</li>
<li>When to use sets versus lists</li>
<li>How to iterate into a set</li>
<li>What are dictionaries and how to use them</li>
<li>When to use dictionaries versus lists or sets</li>
<li>What is a key in a dictionary</li>
<li>How to iterate over a dictionary</li>
<li>What is a lambda function</li>
<li>What are the map, reduce and filter functions</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

</div>
<br />

## 0. Squared simple
<p>Write a function that computes the square value of all integers of a matrix.</p>

<ul>
<li>Prototype: <code>def square_matrix_simple(matrix=[]):</code></li>
<li><code>matrix</code> is a 2 dimensional array</li>
<li>Returns a new matrix:

<ul>
<li>Same size as <code>matrix</code></li>
<li>Each value should be the square of the value of the input</li>
</ul></li>
<li>Initial matrix should not be modified</li>
<li>You are not allowed to import any module</li>
<li>You are allowed to use regular loops, <code>map</code>, etc.</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x04$ cat 0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__(&#39;0-square_matrix_simple&#39;).square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/0x04$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/0x04$ 
</code></pre>
<br />

## 1. Search and replace
<p>Write a function that replaces all occurrences of an element by another in a new list.</p>

<ul>
<li>Prototype: <code>def search_replace(my_list, search, replace):</code></li>
<li><code>my_list</code> is the initial list</li>
<li><code>search</code> is the element to replace in the list</li>
<li><code>replace</code> is the new element</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x04$ cat 1-main.py
#!/usr/bin/python3
search_replace = __import__(&#39;1-search_replace&#39;).search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x04$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
guillaume@ubuntu:~/0x04$ 
</code></pre>
<br />

## 2. Unique addition
<p>Write a function that adds all unique integers in a list (only once for each integer).</p>

<ul>
<li>Prototype: <code>def uniq_add(my_list=[]):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x04$ cat 2-main.py
#!/usr/bin/python3
uniq_add = __import__(&#39;2-uniq_add&#39;).uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print(&quot;Result: {:d}&quot;.format(result))

guillaume@ubuntu:~/0x04$ ./2-main.py
Result: 15
guillaume@ubuntu:~/0x04$ 
</code></pre>
<br />

## 3. Present in both
<p>Write a function that returns a set of common elements in two sets.</p>

<ul>
<li>Prototype: <code>def common_elements(set_1, set_2):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x04$ cat 3-main.py
#!/usr/bin/python3
common_elements = __import__(&#39;3-common_elements&#39;).common_elements

set_1 = { &quot;Python&quot;, &quot;C&quot;, &quot;Javascript&quot; }
set_2 = { &quot;Bash&quot;, &quot;C&quot;, &quot;Ruby&quot;, &quot;Perl&quot; }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

guillaume@ubuntu:~/0x04$ ./3-main.py
[&#39;C&#39;]
guillaume@ubuntu:~/0x04$ 
</code></pre>
<br />

## 4. Only differents
<p>Write a function that returns a set of all elements present in only one set.</p>

<ul>
<li>Prototype: <code>def only_diff_elements(set_1, set_2):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x04$ cat 4-main.py
#!/usr/bin/python3
only_diff_elements = __import__(&#39;4-only_diff_elements&#39;).only_diff_elements

set_1 = { &quot;Python&quot;, &quot;C&quot;, &quot;Javascript&quot; }
set_2 = { &quot;Bash&quot;, &quot;C&quot;, &quot;Ruby&quot;, &quot;Perl&quot; }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

guillaume@ubuntu:~/0x04$ ./4-main.py
[&#39;Bash&#39;, &#39;Javascript&#39;, &#39;Perl&#39;, &#39;Python&#39;, &#39;Ruby&#39;]
guillaume@ubuntu:~/0x04$ 
</code></pre>
<br />

## 5. Number of keys
<p>Write a function that returns the number of keys in a dictionary.</p>

<ul>
<li>Prototype: <code>def number_keys(a_dictionary):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x04$ cat 5-main.py
#!/usr/bin/python3
number_keys = __import__(&#39;5-number_keys&#39;).number_keys

a_dictionary = { &#39;language&#39;: &quot;C&quot;, &#39;number&#39;: 13, &#39;track&#39;: &quot;Low level&quot; }
nb_keys = number_keys(a_dictionary)
print(&quot;Number of keys: {:d}&quot;.format(nb_keys))

guillaume@ubuntu:~/0x04$ ./5-main.py
Number of keys: 3
guillaume@ubuntu:~/0x04$ 
</code></pre>
<br />

## 6. Print sorted dictionary
<p>Write a function that prints a dictionary by ordered keys.</p>

<ul>
<li>Prototype: <code>def print_sorted_dictionary(a_dictionary):</code></li>
<li>You can assume that all keys are strings</li>
<li>Keys should be sorted by alphabetic order</li>
<li>Only sort keys of the first level (don&rsquo;t sort keys of a dictionary inside the main dictionary)</li>
<li>Dictionary values can have any type</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x04$ cat 6-main.py
#!/usr/bin/python3
print_sorted_dictionary = __import__(&#39;6-print_sorted_dictionary&#39;).print_sorted_dictionary

a_dictionary = { &#39;language&#39;: &quot;C&quot;, &#39;Number&#39;: 89, &#39;track&#39;: &quot;Low level&quot;, &#39;ids&#39;: [1, 2, 3] }
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/0x04$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
guillaume@ubuntu:~/0x04$ 
</code></pre>
<br />

## 7. Update dictionary
<p>Write a function that replaces or adds key/value in a dictionary.</p>

<ul>
<li>Prototype: <code>def update_dictionary(a_dictionary, key, value):</code></li>
<li><code>key</code> argument will be always a string</li>
<li><code>value</code> argument will be any type</li>
<li>If a key exists in the dictionary, the value will be replaced</li>
<li>If a key doesn&rsquo;t exist in the dictionary, it will be created</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x04$ cat 7-main.py
#!/usr/bin/python3
update_dictionary = __import__(&#39;7-update_dictionary&#39;).update_dictionary
print_sorted_dictionary = __import__(&#39;6-print_sorted_dictionary&#39;).print_sorted_dictionary

a_dictionary = { &#39;language&#39;: &quot;C&quot;, &#39;number&#39;: 89, &#39;track&#39;: &quot;Low level&quot; }
new_dict = update_dictionary(a_dictionary, &#39;language&#39;, &quot;Python&quot;)
print_sorted_dictionary(new_dict)
print(&quot;--&quot;)
print_sorted_dictionary(a_dictionary)

print(&quot;--&quot;)
print(&quot;--&quot;)

new_dict = update_dictionary(a_dictionary, &#39;city&#39;, &quot;San Francisco&quot;)
print_sorted_dictionary(new_dict)
print(&quot;--&quot;)
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/0x04$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
guillaume@ubuntu:~/0x04$ 
</code></pre>
<br />

## 8. Simple delete by key
<p>Write a function that deletes a key in a dictionary.</p>

<ul>
<li>Prototype: <code>def simple_delete(a_dictionary, key=&quot;&quot;):</code></li>
<li><code>key</code> argument will be always a string</li>
<li>If a key doesn&rsquo;t exist, the dictionary won&rsquo;t change</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x04$ cat 8-main.py
#!/usr/bin/python3
simple_delete = __import__(&#39;8-simple_delete&#39;).simple_delete
print_sorted_dictionary = \
    __import__(&#39;6-print_sorted_dictionary&#39;).print_sorted_dictionary

a_dictionary = { &#39;language&#39;: &quot;C&quot;, &#39;Number&#39;: 89, &#39;track&#39;: &quot;Low&quot;, &#39;ids&#39;: [1, 2, 3] }
new_dict = simple_delete(a_dictionary, &#39;track&#39;)
print_sorted_dictionary(a_dictionary)
print(&quot;--&quot;)
print_sorted_dictionary(new_dict)

print(&quot;--&quot;)
print(&quot;--&quot;)
new_dict = simple_delete(a_dictionary, &#39;c_is_fun&#39;)
print_sorted_dictionary(a_dictionary)
print(&quot;--&quot;)
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/0x04$ ./8-main.py
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
guillaume@ubuntu:~/0x04$ 
</code></pre>
<br />

## 9. Multiply by 2
<p>Write a function that returns a new dictionary with all values multiplied by 2</p>

<ul>
<li>Prototype: <code>def multiply_by_2(a_dictionary):</code></li>
<li>You can assume that all values are only integers</li>
<li>Returns a new dictionary</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x04$ cat 9-main.py
#!/usr/bin/python3
multiply_by_2 = __import__(&#39;9-multiply_by_2&#39;).multiply_by_2
print_sorted_dictionary = \
    __import__(&#39;6-print_sorted_dictionary&#39;).print_sorted_dictionary

a_dictionary = {&#39;John&#39;: 12, &#39;Alex&#39;: 8, &#39;Bob&#39;: 14, &#39;Mike&#39;: 14, &#39;Molly&#39;: 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print(&quot;--&quot;)
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/0x04$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
guillaume@ubuntu:~/0x04$ 
</code></pre>
<br />

## 10. Best score
<p>Write a function that returns a key with the biggest integer value.</p>

<ul>
<li>Prototype: <code>def best_score(a_dictionary):</code></li>
<li>You can assume that all values are only integers</li>
<li>If no score found, return <code>None</code></li>
<li>You can assume all students have a different score</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x04$ cat 10-main.py
#!/usr/bin/python3
best_score = __import__(&#39;10-best_score&#39;).best_score

a_dictionary = {&#39;John&#39;: 12, &#39;Bob&#39;: 14, &#39;Mike&#39;: 14, &#39;Molly&#39;: 16, &#39;Adam&#39;: 10}
best_key = best_score(a_dictionary)
print(&quot;Best score: {}&quot;.format(best_key))

best_key = best_score(None)
print(&quot;Best score: {}&quot;.format(best_key))

guillaume@ubuntu:~/0x04$ ./10-main.py
Best score: Molly
Best score: None
guillaume@ubuntu:~/0x04$ 
</code></pre>
<br />

## 11. Multiply by using map
<p>Write a function that returns a list with all values multiplied by a number without using any loops.</p>

<ul>
<li>Prototype: <code>def multiply_list_map(my_list=[], number=0):</code></li>
<li>Returns a new list:

<ul>
<li>Same length as <code>my_list</code></li>
<li>Each value should be multiplied by <code>number</code></li>
</ul></li>
<li>Initial list should not be modified</li>
<li>You are not allowed to import any module</li>
<li>You have to use <code>map</code></li>
<li>Your file should be max 3 lines</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x04$ cat 11-main.py
#!/usr/bin/python3
multiply_list_map = __import__(&#39;11-multiply_list_map&#39;).multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)

guillaume@ubuntu:~/0x04$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
guillaume@ubuntu:~/0x04$ 
</code></pre>
<br />

## 12. Roman to Integer
<p><strong>Technical interview preparation</strong>: </p>

<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>

<p>Create a function <code>def roman_to_int(roman_string):</code> that converts a <a href="/rltoken/g7UKrGGWwbRJRkdB3tFThg" title="Roman numeral" target="_blank">Roman numeral</a> to an integer.</p>

<ul>
<li>You can assume the number will be between 1 to 3999.</li>
<li><code>def roman_to_int(roman_string)</code> must return an integer</li>
<li>If the <code>roman_string</code> is not a string or <code>None</code>, return 0</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x04$ cat 12-main.py
#!/usr/bin/python3
&quot;&quot;&quot; Roman to Integer test file
&quot;&quot;&quot;
roman_to_int = __import__(&#39;12-roman_to_int&#39;).roman_to_int

roman_number = &quot;X&quot;
print(&quot;{} = {}&quot;.format(roman_number, roman_to_int(roman_number)))

roman_number = &quot;VII&quot;
print(&quot;{} = {}&quot;.format(roman_number, roman_to_int(roman_number)))

roman_number = &quot;IX&quot;
print(&quot;{} = {}&quot;.format(roman_number, roman_to_int(roman_number)))

roman_number = &quot;LXXXVII&quot;
print(&quot;{} = {}&quot;.format(roman_number, roman_to_int(roman_number)))

roman_number = &quot;DCCVII&quot;
print(&quot;{} = {}&quot;.format(roman_number, roman_to_int(roman_number)))

guillaume@ubuntu:~/0x04$ ./12-main.py
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
guillaume@ubuntu:~/0x04$ 
</code></pre>
<br />

## 13. Weighted average!
<p>Write a function that returns the weighted average of all integers tuple <code>(&lt;score&gt;, &lt;weight&gt;)</code></p>

<ul>
<li>Prototype: <code>def weight_average(my_list=[]):</code></li>
<li>Returns <code>0</code> if the list is empty</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x04$ cat 100-main.py
#!/usr/bin/python3
weight_average = __import__(&#39;100-weight_average&#39;).weight_average

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print(&quot;Average: {:0.2f}&quot;.format(result))

guillaume@ubuntu:~/0x04$ ./100-main.py
Average: 2.80
guillaume@ubuntu:~/0x04$ 
</code></pre>
<br />

## 14. Squared by using map
<p>Write a function that computes the square value of all integers of a matrix using <code>map</code></p>

<ul>
<li>Prototype: <code>def square_matrix_map(matrix=[]):</code></li>
<li><code>matrix</code> is a 2 dimensional array</li>
<li>Returns a new matrix:

<ul>
<li>Same size as <code>matrix</code></li>
<li>Each value should be the square of the value of the input</li>
</ul></li>
<li>Initial matrix should not be modified</li>
<li>You are not allowed to import any module</li>
<li>You have to use <code>map</code></li>
<li>You are not allowed to use <code>for</code> or <code>while</code></li>
<li>Your file should be max 3 lines</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x04$ cat 101-main.py
#!/usr/bin/python3
square_matrix_map = \
    __import__(&#39;101-square_matrix_map&#39;).square_matrix_map

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/0x04$ ./101-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/0x04$ 
</code></pre>
<br />

## 15. Delete by value
<p>Write a function that deletes keys with a specific value in a dictionary.</p>

<ul>
<li>Prototype: <code>def complex_delete(a_dictionary, value):</code></li>
<li>If the value doesn&rsquo;t exist, the dictionary won&rsquo;t change</li>
<li>All keys having the searched value have to be deleted</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x04$ cat 102-main.py
#!/usr/bin/python3
complex_delete = __import__(&#39;102-complex_delete&#39;).complex_delete
print_sorted_dictionary = \
    __import__(&#39;6-print_sorted_dictionary&#39;).print_sorted_dictionary

a_dictionary = {&#39;lang&#39;: &quot;C&quot;, &#39;track&#39;: &quot;Low&quot;, &#39;pref&#39;: &quot;C&quot;, &#39;ids&#39;: [1, 2, 3]}
new_dict = complex_delete(a_dictionary, &#39;C&#39;)
print_sorted_dictionary(a_dictionary)
print(&quot;--&quot;)
print_sorted_dictionary(new_dict)

print(&quot;--&quot;)
print(&quot;--&quot;)
new_dict = complex_delete(a_dictionary, &#39;c_is_fun&#39;)
print_sorted_dictionary(a_dictionary)
print(&quot;--&quot;)
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/0x04$ ./102-main.py
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
--
--
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
guillaume@ubuntu:~/0x04$ 
</code></pre>
<br />

## 16. CPython #1: PyBytesObject
<p>Create two C functions that print some basic info about Python lists and Python bytes objects.<br />
<br />
<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/8030f8429cb90b3fc145b994112e2dae8c4030e0.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220105%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220105T172453Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=116d20baae97b20d136c24aae80a0f86dc4aa104c894dce8f047c1433a9faa9b" alt="" style="" />
<br />
Python lists:</p>

<ul>
<li>Prototype: <code>void print_python_list(PyObject *p);</code></li>
<li>Format: see example</li>
</ul>

<p>Python bytes:</p>

<ul>
<li>Prototype: <code>void print_python_bytes(PyObject *p);</code></li>
<li>Format: see example</li>
<li>Line &ldquo;first X bytes&rdquo;: print a maximum of 10 bytes</li>
<li>If <code>p</code> is not a valid <code>PyBytesObject</code>, print an error message (see example)</li>
<li>Read <code>/usr/include/python3.4/bytesobject.h</code></li>
</ul>

<p>About:</p>

<ul>
<li>Python version: 3.4</li>
<li>Your shared library will be compiled with this command line: <code>gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c</code></li>
<li>You are not allowed to use the following macros/functions:

<ul>
<li><code>Py_SIZE</code></li>
<li><code>Py_TYPE</code></li>
<li><code>PyList_GetItem</code></li>
<li><code>PyBytes_AS_STRING</code></li>
<li><code>PyBytes_GET_SIZE</code></li>
</ul></li>
</ul>

<pre><code>julien@ubuntu:~/CPython$ python3 --version
Python 3.4.3
julien@ubuntu:~/CPython$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
julien@ubuntu:~/CPython$ cat 103-tests.py 
import ctypes

lib = ctypes.CDLL(&#39;./libPython.so&#39;)
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
s = b&quot;Hello&quot;
lib.print_python_bytes(s);
b = b&#39;\xff\xf8\x00\x00\x00\x00\x00\x00&#39;;
lib.print_python_bytes(b);
b = b&#39;What does the \&#39;b\&#39; character do in front of a string literal?&#39;;
lib.print_python_bytes(b);
l = [b&#39;Hello&#39;, b&#39;World&#39;]
lib.print_python_list(l)
del l[1]
lib.print_python_list(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], b&quot;Holberton&quot;, &quot;Betty&quot;]
lib.print_python_list(l)
l = []
lib.print_python_list(l)
l.append(0)
lib.print_python_list(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list(l)
l.pop()
lib.print_python_list(l)
l = [&quot;Holberton&quot;]
lib.print_python_list(l)
lib.print_python_bytes(l);
julien@ubuntu:~/CPython$ python3 103-tests.py 
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[.] bytes object info
  size: 8
  trying string: �
  first 9 bytes: ff f8 00 00 00 00 00 00 00
[.] bytes object info
  size: 60
  trying string: What does the &#39;b&#39; character do in front of a string literal?
  first 10 bytes: 57 68 61 74 20 64 6f 65 73 20
[*] Python list info
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: bytes
[.] bytes object info
  size: 5
  trying string: World
  first 6 bytes: 57 6f 72 6c 64 00
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[*] Python list info
[*] Size of the Python List = 8
[*] Allocated = 8
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: bytes
[.] bytes object info
  size: 9
  trying string: Holberton
  first 10 bytes: 48 6f 6c 62 65 72 74 6f 6e 00
Element 7: str
[*] Python list info
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Python list info
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Python list info
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 1
Element 0: str
[.] bytes object info
  [ERROR] Invalid Bytes Object
julien@ubuntu:~/CPython$ 
</code></pre>
<br />
