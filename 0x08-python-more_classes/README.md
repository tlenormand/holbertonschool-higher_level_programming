# 0x08. Python - More Classes and Objects

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/VlISluyXK-teEwwPCu2tlg" title="Object Oriented Programming" target="_blank">Object Oriented Programming</a> (<em>Read everything until the paragraph &ldquo;Inheritance&rdquo; (excluded)</em>)</li>
<li><a href="/rltoken/zerKovWZrKMKWx0OVZBchw" title="Object-Oriented Programming" target="_blank">Object-Oriented Programming</a> (<em>Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: &ldquo;General Introduction,&rdquo; &ldquo;First-class Everything,&rdquo; &ldquo;A Minimal Class in Python,&rdquo; &ldquo;Attributes,&rdquo; &ldquo;Methods,&rdquo; &ldquo;The <code>__init__</code> Method,&rdquo;  &ldquo;Data Abstraction, Data Encapsulation, and Information Hiding,&rdquo; &ldquo;<code>__str__</code>- and <code>__repr__</code>-Methods,&rdquo; &ldquo;Public- Protected- and Private Attributes,&rdquo; &amp; &ldquo;Destructor&rdquo;</em>)</li>
<li><a href="/rltoken/tBuuWfzA2PIFAmX8X65YZg" title="Class and Instance Attributes" target="_blank">Class and Instance Attributes</a> </li>
<li><a href="/rltoken/ce7aZMwzugNBFgfYxNxwCw" title="classmethods and staticmethods" target="_blank">classmethods and staticmethods</a> </li>
<li><a href="/rltoken/sOlKSeY2hI6Ppf_hExxJvw" title="Properties vs. Getters and Setters" target="_blank">Properties vs. Getters and Setters</a> (<em>Mainly the last part &ldquo;Public instead of Private Attributes&rdquo;</em>)</li>
<li><a href="/rltoken/BnqS9rZ4oYsX_QMzgHNa8A" title="str vs repr" target="_blank">str vs repr</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/XAZQeGUjBYlhagBCUHKasQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

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
<li>What are the special <code>__str__</code> and <code>__repr__</code> methods and how to use them</li>
<li>What is the difference between <code>__str__</code> and <code>__repr__</code></li>
<li>What is a class attribute</li>
<li>What is the difference between a object attribute and a class attribute</li>
<li>What is a class method</li>
<li>What is a static method</li>
<li>How to dynamically create arbitrary new attributes for existing instances of a class</li>
<li>How to bind attributes to object and classes</li>
<li>What is and what does contain <code>__dict__</code> of a class and of an instance of a class</li>
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
</ul>

<h2>Trace</h2>

<p>To help you with your journey, feel free to try your code <a href="/rltoken/55Tftn2fWncAOZlnFpQiXg" title="here" target="_blank">here</a> with some dedicated test for each task. You will be able to see in real time your code and what is really happening.</p>
