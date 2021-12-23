# 0x02. Python - import & modules

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/4SOY6RYv_fYUM-4NNB3Abg" title="Modules" target="_blank">Modules</a> </li>
<li><a href="/rltoken/pIjNhhRLMFfHoqcTM7u3_A" title="Command line arguments" target="_blank">Command line arguments</a> </li>
<li><a href="/rltoken/ngVTmU2SAH3NW1Z2IGqmLA" title="Pycodestyle -- Style Guide for Python Code" target="_blank">Pycodestyle &ndash; Style Guide for Python Code</a> </li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>python3</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/GzK0HyXjvp5fcKQiiTyLRQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>How to import functions from another file</li>
<li>How to use imported functions</li>
<li>How to create a module</li>
<li>How to use the built-in function <code>dir()</code></li>
<li>How to prevent code in your script from being executed when imported</li>
<li>How to use command line arguments with your Python programs</li>
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

## 0. Import a simple function from a simple file

<p>Write a program that imports the function <code>def add(a, b):</code> from the file <code>add_0.py</code> and prints the result of the addition <code>1 + 2 = 3</code></p>

<ul>
<li>You have to use <code>print</code> function with string format to display integers</li>
<li>You have to assign:

<ul>
<li>the value <code>1</code> to a variable called <code>a</code> </li>
<li>the value <code>2</code> to a variable called <code>b</code></li>
<li>and use those two variables as arguments when calling the functions <code>add</code> and <code>print</code></li>
</ul></li>
<li><code>a</code> and <code>b</code> must be defined in 2 different lines: <code>a = 1</code> and another <code>b = 2</code></li>
<li>Your program should print: <code>&lt;a value&gt; + &lt;b value&gt; = &lt;add(a, b) value&gt;</code> followed with a new line</li>
<li>You can only use the word <code>add_0</code> once in your code</li>
<li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
<li>Your code should not be executed when imported - by using <code>__import__</code>, like the example below</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x02$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    &quot;&quot;&quot;My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    &quot;&quot;&quot;
    return (a + b)

guillaume@ubuntu:~/0x02$ ./0-add.py
1 + 2 = 3
guillaume@ubuntu:~/0x02$ cat 0-import_add.py
__import__(&quot;0-add&quot;)
guillaume@ubuntu:~/0x02$ python3 0-import_add.py 
guillaume@ubuntu:~/0x02$ 
</code></pre>
<br />

## 1. My first toolbox!

<p>Write a program that imports functions from the file <code>calculator_1.py</code>, does some Maths, and prints the result.</p>

<ul>
<li>Do not use the function <code>print</code> (with string format to display integers) more than 4 times </li>
<li>You have to define:

<ul>
<li>the value <code>10</code> to a variable <code>a</code></li>
<li>the value <code>5</code> to a variable <code>b</code></li>
<li>and use those two variables only, as arguments when calling functions (including <code>print</code>)</li>
</ul></li>
<li><code>a</code> and <code>b</code> must be defined in 2 different lines: <code>a = 10</code> and another <code>b = 5</code></li>
<li>Your program should call each of the imported functions. See example below for format</li>
<li>the word <code>calculator_1</code> should be used only once in your file</li>
<li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    &quot;&quot;&quot;My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    &quot;&quot;&quot;
    return (a + b)


def sub(a, b):
    &quot;&quot;&quot;My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    &quot;&quot;&quot;
    return (a - b)


def mul(a, b):
    &quot;&quot;&quot;My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    &quot;&quot;&quot;
    return (a * b)


def div(a, b):
    &quot;&quot;&quot;My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    &quot;&quot;&quot;
    return int(a / b)

guillaume@ubuntu:~/0x02$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
guillaume@ubuntu:~/0x02$
</code></pre>

## 2. How to make a script dynamic!
<p>Write a program that prints the number of and the list of its arguments.</p>

<ul>
<li>The output should be:

<ul>
<li>Number of argument(s) followed by <code>argument</code> (if number is one) or <code>arguments</code> (otherwise), followed by</li>
<li><code>:</code> (or <code>.</code> if no arguments were passed) followed by</li>
<li>a new line, followed by (if at least one argument),</li>
<li>one line per argument:

<ul>
<li>the position of the argument (starting at <code>1</code>) followed by <code>:</code>, followed by the argument value and a new line</li>
</ul></li>
</ul></li>
<li>Your code should not be executed when imported</li>
<li>The number of elements of <code>argv</code> can be retrieved by using: <code>len(argv)</code></li>
<li>You do not have to fully understand lists yet, but imagine that <code>argv</code> can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x02$ ./2-args.py 
0 arguments.
guillaume@ubuntu:~/0x02$ ./2-args.py Hello
1 argument:
1: Hello
guillaume@ubuntu:~/0x02$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
guillaume@ubuntu:~/0x02$ 
</code></pre>
<br />

## 3. Infinite addition
<p>Write a program that prints the result of the addition of all arguments</p>

<ul>
<li>The output should be the result of the addition of all arguments, followed by a new line</li>
<li>You can cast arguments into integers by using <code>int()</code> (you can assume that all arguments can be casted into integers)</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x02$ ./3-infinite_add.py
0
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10
89
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10 -40 -300 89 
-162
guillaume@ubuntu:~/0x02$ 
</code></pre>

<p>Last but not least, your program should also handle big numbers. And the good news is: if your program works for the above example, it will work for the following example:</p>

<pre><code>guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 1111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999990000000000000000000 11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334567788888899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334568900000011111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999989999999999999999999
guillaume@ubuntu:~/0x02$
</code></pre>
<br />

## 4. Who are you?
<p>Write a program that prints all the names defined by the compiled module <a href="https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc" title="hidden_4.pyc" target="_blank">hidden_4.pyc</a> (please download it locally).</p>

<ul>
<li>You should print one name per line, in alpha order</li>
<li>You should print only names that do <strong>not</strong> start with <code>__</code></li>
<li>Your code should not be executed when imported</li>
<li>Make sure you are running your code in Python3.8.x (<code>hidden_4.pyc</code> has been compiled with this version)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x02$ curl -Lso &quot;hidden_4.pyc&quot; &quot;https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc&quot;
guillaume@ubuntu:~/0x02$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
guillaume@ubuntu:~/0x02$ 
</code></pre>
<br />

## 5. Everything can be imported
<p>Write a program that imports the variable <code>a</code> from the file <code>variable_load_5.py</code> and prints its value.</p>

<ul>
<li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x02$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
&quot;&quot;&quot;Simple variable
&quot;&quot;&quot;

guillaume@ubuntu:~/0x02$ ./5-variable_load.py
98
guillaume@ubuntu:~/0x02$
</code></pre>
<br />

## 6. Build my own calculator!
<p>Write a program that imports all functions from the file <code>calculator_1.py</code> and handles basic operations.</p>

<ul>
<li>Usage: <code>./100-my_calculator.py a operator b</code>

<ul>
<li>If the number of arguments is not 3, your program has to:

<ul>
<li>print <code>Usage: ./100-my_calculator.py &lt;a&gt; &lt;operator&gt; &lt;b&gt;</code> followed with a new line</li>
<li>exit with the value <code>1</code></li>
</ul></li>
<li><code>operator</code> can be: 

<ul>
<li><code>+</code> for addition</li>
<li><code>-</code> for subtraction</li>
<li><code>*</code> for multiplication</li>
<li><code>/</code> for division</li>
</ul></li>
<li>If the operator is not one of the above:

<ul>
<li>print <code>Unknown operator. Available operators: +, -, * and /</code> followed with a new line</li>
<li>exit with the value <code>1</code></li>
</ul></li>
<li>You can cast <code>a</code> and <code>b</code> into integers by using <code>int()</code> (you can assume that all arguments will be castable into integers)</li>
<li>The result should be printed like this: <code>&lt;a&gt; &lt;operator&gt; &lt;b&gt; = &lt;result&gt;</code>, followed by a new line</li>
</ul></li>
<li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    &quot;&quot;&quot;My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    &quot;&quot;&quot;
    return (a + b)


def sub(a, b):
    &quot;&quot;&quot;My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    &quot;&quot;&quot;
    return (a - b)


def mul(a, b):
    &quot;&quot;&quot;My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    &quot;&quot;&quot;
    return (a * b)


def div(a, b):
    &quot;&quot;&quot;My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    &quot;&quot;&quot;
    return int(a / b)

guillaume@ubuntu:~/0x02$ ./100-my_calculator.py ; echo $?
Usage: ./100-my_calculator.py &lt;a&gt; &lt;operator&gt; &lt;b&gt;
1
guillaume@ubuntu:~/0x02$ ./100-my_calculator.py 3 + 5 ; echo $?
3 + 5 = 8
0
guillaume@ubuntu:~/0x02$ ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
1
guillaume@ubuntu:~/0x02$
</code></pre>
<br />

## 7. Easy print
<p>Write a program that prints <code>#pythoniscool</code>, followed by a new line, in the standard output.</p>

<ul>
<li>Your program should be maximum 2 lines long</li>
<li>You are not allowed to use <code>print</code> or <code>eval</code> or <code>open</code> or <code>import sys</code> in your file <code>101-easy_print.py</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x02$ ./101-easy_print.py
#pythoniscool
guillaume@ubuntu:~/0x02$ 
</code></pre>
<br />

## 8. ByteCode -> Python #3
<p>Write the Python function <code>def magic_calculation(a, b):</code> that does exactly the same as the following Python bytecode:</p>

<pre><code>  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 ((&#39;add&#39;, &#39;sub&#39;))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (&lt;)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        &gt;&gt;   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        &gt;&gt;   89 POP_BLOCK

  8     &gt;&gt;   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     &gt;&gt;   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
</code></pre>
<br />

## 9. Fast alphabet
<p>Write a program that prints the alphabet in uppercase, followed by a new line.</p>

<ul>
<li>Your program should be maximum 3 lines long</li>
<li>You are not allowed to use:

<ul>
<li>any loops</li>
<li>any conditional statements</li>
<li><code>str.join()</code></li>
<li>any string literal</li>
<li>any system calls</li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x02$ ./103-fast_alphabet.py
ABCDEFGHIJKLMNOPQRSTUVWXYZ
guillaume@ubuntu:~/0x02$ wc -l 103-fast_alphabet.py
3 103-fast_alphabet.py
guillaume@ubuntu:~/0x02$
</code></pre>
<br />
