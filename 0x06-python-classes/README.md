# 0x06. Python - Classes and Objects

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/izl1kO1isRJo6h_Ce2pmhw" title="Object Oriented Programming" target="_blank">Object Oriented Programming</a> (<em>Read everything until the paragraph &ldquo;Inheritance&rdquo; excluded. You do NOT have to learn about class attributes, <code>classmethod</code> and <code>staticmethod</code> yet</em>)</li>
<li><a href="/rltoken/hA0enGhhhBgtbDEED2FFYA" title="Object-Oriented Programming" target="_blank">Object-Oriented Programming</a> (<em>Please *</em>be careful*<em>: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON&rsquo;T have to learn about class attributes), Methods, The <code>__init__</code> Method, &ldquo;Data Abstraction, Data Encapsulation, and Information Hiding,&rdquo; &ldquo;Public, Protected, and Private Attributes&rdquo;</em>)</li>
<li><a href="/rltoken/33gDTd_1onhh3vkeKQv-Jw" title="Properties vs. Getters and Setters" target="_blank">Properties vs. Getters and Setters</a> </li>
<li><a href="/rltoken/aFk7Ki8TPw5vZZBx2JXvIQ" title="Learn to Program 9 : Object Oriented Programming" target="_blank">Learn to Program 9 : Object Oriented Programming</a> </li>
<li><a href="/rltoken/CFTUXsxbTVu4xb698_2bmQ" title="Python Classes and Objects" target="_blank">Python Classes and Objects</a> </li>
<li><a href="/rltoken/DK1vkIQ0xT1fmMrmBcSGiA" title="Object Oriented Programming" target="_blank">Object Oriented Programming</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/IGj3GprYnPJ9YUl7WM9TEg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome </li>
<li>What is OOP</li>
<li>&ldquo;first-class everything&rdquo;</li>
<li>What is a class</li>
<li>What is an object and an instance</li>
<li>What is the difference between a class and an object or instance</li>
<li>What is an attribute</li>
<li>What are and how to use public, protected and private attributes</li>
<li>What is <code>self</code></li>
<li>What is a method</li>
<li>What is the special <code>__init__</code> method and how to use it</li>
<li>What is Data Abstraction, Data Encapsulation, and Information Hiding</li>
<li>What is a property</li>
<li>What is the difference between an attribute and a property in Python</li>
<li>What is the Pythonic way to write getters and setters in Python</li>
<li>How to dynamically create arbitrary new attributes for existing instances of a class</li>
<li>How to bind attributes to object and classes</li>
<li>What is the <code>__dict__</code> of a class and/or instance of a class and what does it contain</li>
<li>How does Python find the attributes of an object or class</li>
<li>How to use the <code>getattr</code> function</li>
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
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h2>More Info</h2>

<p><strong>Documentation is now mandatory!</strong> Each module, class, and method must contain docstring as comments. <a href="/rltoken/SYdQnrcR2jL5hIs5TkIN5Q" title="Example Google Style Python Docstrings" target="_blank">Example Google Style Python Docstrings</a></p>

<h2>Trace</h2>

<p>To help you with your journey, feel free to try your code <a href="/rltoken/-sgdZGK2LrEOKZ75BGzjYA" title="here" target="_blank">here</a> with some dedicated test for each task. You will be able to see in real time your code and what is really happening.</p>
