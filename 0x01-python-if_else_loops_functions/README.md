# 0x01. Python - if/else, loops, functions

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/YLjvfmHv_JJ-J-cyn8bS2Q" title="More Control Flow Tools" target="_blank">More Control Flow Tools</a> (<em>Read until &ldquo;4.6. Defining Functions&rdquo; included</em>)</li>
<li><a href="/rltoken/Y-HaMMJBKPseiVDo_v9PVg" title="Myths about Indentation" target="_blank">Myths about Indentation</a> </li>
<li><a href="/rltoken/AorC2VSZ4yCOx-AbatvKLA" title="IndentationError" target="_blank">IndentationError</a> </li>
<li><a href="/rltoken/arGQeiwUbFn3JOoYpw84yA" title="How To Use String Formatters in Python 3" target="_blank">How To Use String Formatters in Python 3</a> </li>
<li><a href="/rltoken/mlo-dauC8pSM_NrO5VYobw" title="Learn to Program" target="_blank">Learn to Program</a> </li>
<li><a href="/rltoken/mlo-dauC8pSM_NrO5VYobw" title="Learn to Program 2 : Looping" target="_blank">Learn to Program 2 : Looping</a> </li>
<li><a href="/rltoken/5uFnbDmoyPNoxwXUNxEypw" title="Pycodestyle -- Style Guide for Python Code" target="_blank">Pycodestyle &ndash; Style Guide for Python Code</a> </li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>python3</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/zTORGnHYbsyIZDwVtF_aZw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>Why indentation is so important in Python</li>
<li>How to use the <code>if</code>, <code>if ... else</code> statements</li>
<li>How to use comments</li>
<li>How to affect values to variables</li>
<li>How to use the <code>while</code> and <code>for</code> loops</li>
<li>How is Python&rsquo;s <code>for</code> different from <code>C</code>&lsquo;s?</li>
<li>How to use the <code>break</code> and <code>continues</code> statements</li>
<li>How to use <code>else</code> clauses on loops</li>
<li>What does the <code>pass</code> statement do, and when to use it</li>
<li>How to use <code>range</code></li>
<li>What is a function and how do you use functions</li>
<li>What does return a function that does not use any <code>return</code> statement</li>
<li>Scope of variables</li>
<li>What&rsquo;s a traceback</li>
<li>What are the arithmetic operators and how to use them</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

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

<h3>C Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89</li>
<li>All your files should end with a new line</li>
<li>Your code should use the <code>Betty</code> style. It will be checked using <a href="https://github.com/holbertonschool/Betty/blob/master/betty-style.pl" title="betty-style.pl" target="_blank">betty-style.pl</a> and <a href="https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl" title="betty-doc.pl" target="_blank">betty-doc.pl</a></li>
<li>You are not allowed to use global variables</li>
<li>No more than 5 functions per file</li>
<li>In the following examples, the <code>main.c</code> files are shown as examples. You can use them to test your functions, but you don&rsquo;t have to push them to your repo (if you do we won&rsquo;t take them into account). We will use our own <code>main.c</code> files at compilation. Our <code>main.c</code> files might be different from the one shown in the examples</li>
<li>The prototypes of all your functions should be included in your header file called <code>lists.h</code></li>
<li>Don’t forget to push your header file</li>
<li>All your header files should be include guarded</li>
</ul>

<h2>More Info</h2>

<p><em>Note</em>: you do not need to understand lists yet.</p>

</div>

## 0. Positive anything is better than negative nothing
<p>This program will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print whether the number stored in the variable <code>number</code> is positive or negative.</p>

<ul>
<li>You can find the source code <a href="/rltoken/2S3G4vOnRrWymCjKYd6Wew" title="here" target="_blank">here</a></li>
<li>The variable <code>number</code> will store a different value every time you will run this program</li>
<li>You don&rsquo;t have to understand what <code>import</code>, <code>random. randint</code> do. Please do not touch this code</li>
<li>The output of the program should be:

<ul>
<li>The number, followed by

<ul>
<li>if the number is greater than 0: <code>is positive</code></li>
<li>if the number is 0: <code>is zero</code></li>
<li>if the number is less than 0: <code>is negative</code></li>
</ul></li>
<li>followed by a new line</li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-4 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
0 is zero
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-3 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-10 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
10 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-5 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
6 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
7 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
5 is positive
guillaume@ubuntu:~/0x01$ 
</code></pre>
<br />

## 1. The last digit
<p>This program will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable <code>number</code>.</p>

<ul>
<li>You can find the source code <a href="/rltoken/e9k9---MJXcMmIjlMdlBpw" title="here" target="_blank">here</a></li>
<li>The variable <code>number</code> will store a different value every time you will run this program</li>
<li>You don&rsquo;t have to understand what <code>import</code>, <code>random.randint</code> do. <strong>Please do not touch this code</strong>. This line should not change: <code>number = random.randint(-10000, 10000)</code></li>
<li>The output of the program should be:

<ul>
<li>The string <code>Last digit of</code>, followed by</li>
<li>the number, followed by</li>
<li>the string <code>is</code>, followed by the last digit of <code>number</code>, followed by

<ul>
<li>if the last digit is greater than 5: the string <code>and is greater than 5</code></li>
<li>if the last digit is 0: the string <code>and is 0</code></li>
<li>if the last digit is less than 6 and not 0: the string <code>and is less than 6 and not 0</code></li>
</ul></li>
<li>followed by a new line</li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ 
</code></pre>
<br />

## 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
<p>Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.</p>

<ul>
<li>You can only use one <code>print</code> function with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to store characters in a variable</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x01$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:~/0x01$
</code></pre>
<br />

## 3. When I was having that alphabet soup, I never thought that it would pay off
<p>Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.</p>

<ul>
<li>Print all the letters except <code>q</code> and <code>e</code></li>
<li>You can only use one <code>print</code> function with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to store characters in a variable</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x01$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyzguillaume@ubuntu:~/0x01$
</code></pre>
<br />

## 4. Hexadecimal printing
<p>Write a program that prints all numbers from <code>0</code> to <code>98</code> in decimal and in hexadecimal (as in the following example)</p>

<ul>
<li>You can only use one <code>print</code> function with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to store numbers or strings in a variable</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x01$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
guillaume@ubuntu:~/0x01$
</code></pre>
<br />

## 5. 00...99
<p>Write a program that prints numbers from <code>0</code> to <code>99</code>.</p>

<ul>
<li>Numbers must be separated by <code>,</code>, followed by a space</li>
<li>Numbers should be printed in ascending order, with two digits</li>
<li>The last number should be followed by a new line</li>
<li>You can only use no more than 2 <code>print</code> functions with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to store numbers or strings in a variable</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x01$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
guillaume@ubuntu:~/0x01$ 
</code></pre>
<br />

## 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
<p>Write a program that prints all possible different combinations of two digits.</p>

<ul>
<li>Numbers must be separated by <code>,</code>, followed by a space</li>
<li>The two digits must be different</li>
<li><code>01</code> and <code>10</code> are considered the same combination of the two digits <code>0</code> and <code>1</code></li>
<li>Print only the smallest combination of two digits</li>
<li>Numbers should be printed in ascending order, with two digits</li>
<li>The last number should be followed by a new line</li>
<li>You can only use no more than 3 <code>print</code> functions with string format</li>
<li>You can only use no more than 2 loops in your code</li>
<li>You are not allowed to store numbers or strings in a variable</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x01$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
guillaume@ubuntu:~/0x01$ 
</code></pre>
<br />

## 7. islower
<p>Write a function that checks for lowercase character. </p>

<ul>
<li>Prototype: <code>def islower(c):</code></li>
<li>Returns <code>True</code> if <code>c</code> is lowercase</li>
<li>Returns <code>False</code> otherwise</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>str.upper()</code> and <code>str.isupper()</code></li>
<li><a href="/rltoken/Wqb18-TGOnY9dZAWrWX03A" title="Tips: ord()" target="_blank">Tips: ord()</a></li>
</ul>

<p>You don&rsquo;t need to understand <code>__import__</code></p>

<pre><code>guillaume@ubuntu:~/0x01$ cat 7-main.py
#!/usr/bin/env python3
islower = __import__(&#39;7-islower&#39;).islower

print(&quot;a is {}&quot;.format(&quot;lower&quot; if islower(&quot;a&quot;) else &quot;upper&quot;))
print(&quot;H is {}&quot;.format(&quot;lower&quot; if islower(&quot;H&quot;) else &quot;upper&quot;))
print(&quot;A is {}&quot;.format(&quot;lower&quot; if islower(&quot;A&quot;) else &quot;upper&quot;))
print(&quot;3 is {}&quot;.format(&quot;lower&quot; if islower(&quot;3&quot;) else &quot;upper&quot;))
print(&quot;g is {}&quot;.format(&quot;lower&quot; if islower(&quot;g&quot;) else &quot;upper&quot;))

guillaume@ubuntu:~/0x01$ ./7-main.py
a is lower
H is upper
A is upper
3 is upper
g is lower
guillaume@ubuntu:~/0x01$ 
</code></pre>
<br />

## 8. To uppercase
<p>Write a function that prints a string in uppercase followed by a new line.</p>

<ul>
<li>Prototype: <code>def uppercase(str):</code></li>
<li>You can only use no more than 2 <code>print</code> functions with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>str.upper()</code> and <code>str.isupper()</code></li>
<li><a href="/rltoken/Wqb18-TGOnY9dZAWrWX03A" title="Tips: ord()" target="_blank">Tips: ord()</a></li>
</ul>

<p>You don&rsquo;t need to understand <code>__import__</code></p>

<pre><code>guillaume@ubuntu:~/0x01$ cat 8-main.py
#!/usr/bin/env python3
uppercase = __import__(&#39;8-uppercase&#39;).uppercase

uppercase(&quot;best&quot;)
uppercase(&quot;Best School 98 Battery street&quot;)

guillaume@ubuntu:~/0x01$ ./8-main.py
BEST
BEST SCHOOL 98 BATTERY STREET
guillaume@ubuntu:~/0x01$ 
</code></pre>
<br />

## 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important
<p>Write a function that prints the last digit of a number.</p>

<ul>
<li>Prototype: <code>def print_last_digit(number):</code></li>
<li>Returns the value of the last digit</li>
<li>You are not allowed to import any module</li>
</ul>

<p>You don&rsquo;t need to understand <code>__import__</code></p>

<pre><code>guillaume@ubuntu:~/0x01$ cat 9-main.py
#!/usr/bin/env python3
print_last_digit = __import__(&#39;9-print_last_digit&#39;).print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

guillaume@ubuntu:~/0x01$ ./9-main.py
8044
guillaume@ubuntu:~/0x01$ 
</code></pre>
<br />

## 10. a + b
 <p>Write a function that adds two integers and returns the result.</p>

<ul>
<li>Prototype: <code>def add(a, b):</code></li>
<li>Returns the value of <code>a + b</code></li>
<li>You are not allowed to import any module</li>
</ul>

<p>You don&rsquo;t need to understand <code>__import__</code></p>

<pre><code>guillaume@ubuntu:~/0x01$ cat 10-main.py
#!/usr/bin/env python3
add = __import__(&#39;10-add&#39;).add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))

guillaume@ubuntu:~/0x01$ ./10-main.py
3
98
98
guillaume@ubuntu:~/0x01$ 
</code></pre>
<br />

## 11. a ^ b
<p>Write a function that computes <code>a</code> to the power of <code>b</code> and return the value.</p>

<ul>
<li>Prototype: <code>def pow(a, b):</code></li>
<li>Returns the value of <code>a ^ b</code></li>
<li>You are not allowed to import any module</li>
</ul>

<p>You don&rsquo;t need to understand <code>__import__</code></p>

<pre><code>guillaume@ubuntu:~/0x01$ cat 11-main.py
#!/usr/bin/env python3
pow = __import__(&#39;11-pow&#39;).pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))

guillaume@ubuntu:~/0x01$ ./11-main.py
4
9604
1
0.0001
-1024
guillaume@ubuntu:~/0x01$ 
</code></pre>
<br />

## 12. Fizz Buzz
<p>Write a function that prints the numbers from 1 to 100 separated by a space. </p>

<ul>
<li>For multiples of three print <code>Fizz</code> instead of the number and for multiples of five print <code>Buzz</code>. </li>
<li>For numbers which are multiples of both three and five print <code>FizzBuzz</code>.</li>
<li>Prototype: <code>def fizzbuzz():</code></li>
<li>Each element should be followed by a space</li>
<li>You are not allowed to import any module</li>
</ul>

<p>You don&rsquo;t need to understand <code>__import__</code></p>

<pre><code>guillaume@ubuntu:~/0x01$ cat 12-main.py
#!/usr/bin/env python3
fizzbuzz = __import__(&#39;12-fizzbuzz&#39;).fizzbuzz

fizzbuzz()
print(&quot;&quot;)

guillaume@ubuntu:~/0x01$ ./12-main.py | cat -e
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz $
guillaume@ubuntu:~/0x01$ 
</code></pre>
<br />

## 13. Insert in sorted linked list
<p><strong>Technical interview preparation</strong>: </p>

<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>

<p>Write a function in C that inserts a number into a sorted singly linked list.</p>

<ul>
<li>Prototype: <code>listint_t *insert_node(listint_t **head, int number);</code></li>
<li>Return: the address of the new node, or <code>NULL</code> if it failed</li>
</ul>

<pre><code>carrie@ubuntu:0x01$ cat lists.h 
#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
</code></pre>

<pre><code>carrie@ubuntu:0x01$ cat linked_lists.c 
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &quot;lists.h&quot;

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf(&quot;%i\n&quot;, current-&gt;n);
        current = current-&gt;next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new-&gt;n = n;
    new-&gt;next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current-&gt;next != NULL)
            current = current-&gt;next;
        current-&gt;next = new;
    }

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head-&gt;next;
        free(current);
    }
}
</code></pre>

<pre><code>carrie@ubuntu:0x01$ cat 13-main.c 
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include &quot;lists.h&quot;

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&amp;head, 0);
    add_nodeint_end(&amp;head, 1);
    add_nodeint_end(&amp;head, 2);
    add_nodeint_end(&amp;head, 3);
    add_nodeint_end(&amp;head, 4);
    add_nodeint_end(&amp;head, 98);
    add_nodeint_end(&amp;head, 402);
    add_nodeint_end(&amp;head, 1024);
    print_listint(head);

    printf(&quot;-----------------\n&quot;);

    insert_node(&amp;head, 27);

    print_listint(head);

    free_listint(head);

    return (0);
}
</code></pre>

<pre><code>carrie@ubuntu:0x01$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 13-main.c linked_lists.c 13-insert_number.c -o insert
carrie@ubuntu:0x01$ ./insert
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
27
98
402
1024
carrie@ubuntu:0x01$  
</code></pre>
<br />

## 14. Smile in the mirror
<p>Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (<code>z</code> in lowercase and <code>Y</code> in uppercase) , not followed by a new line.</p>

<ul>
<li>You can only use one <code>print</code> function with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to store characters in a variable</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x01$ ./100-print_tebahpla.py
zYxWvUtSrQpOnMlKjIhGfEdCbAguillaume@ubuntu:~/0x01$
</code></pre>
<br />

## 15. Remove at position
<p>Write a function that creates a copy of the string, removing the character at the position <code>n</code> (not the Python way, the &ldquo;C array index&rdquo;).</p>

<ul>
<li>Prototype: <code>def remove_char_at(str, n):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<p>You don&rsquo;t need to understand <code>__import__</code></p>

<pre><code>guillaume@ubuntu:~/0x01$ cat 101-main.py
#!/usr/bin/env python3
remove_char_at = __import__(&#39;101-remove_char_at&#39;).remove_char_at

print(remove_char_at(&quot;Best School&quot;, 3))
print(remove_char_at(&quot;Chicago&quot;, 2))
print(remove_char_at(&quot;C is fun!&quot;, 0))
print(remove_char_at(&quot;School&quot;, 10))
print(remove_char_at(&quot;Python&quot;, -2))

guillaume@ubuntu:~/0x01$ ./101-main.py
Bes School
Chcago
 is fun!
School
Python
guillaume@ubuntu:~/0x01$ 
</code></pre>
<br />

## 16. ByteCode -> Python #2
<p>Write the Python function <code>def magic_calculation(a, b, c):</code> that does exactly the same as the following Python bytecode:</p>

<pre><code>  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (&lt;)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     &gt;&gt;   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (&gt;)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     &gt;&gt;   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
</code></pre>
<br />
