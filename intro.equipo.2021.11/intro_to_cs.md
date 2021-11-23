---
title: Intro to programming using Python
subtitle: Equipo Academy's College Simulation Day
date: 2021.11.24
author: Hugo O. Rivera
---

# Intros

# Intros

- Mexican-American dreamer (DACA) raised in Santa Fe, NM
- graduated with computer science and math degrees from New Mexico Tech in 2018
- Triplebyte recruitment agency
- started working in a healthcare startup
- currently at a large renewable energy company building software for electric vehicle charging stations and large-scale batteries for powering buildings

# Useful Websites

- Pick one:
  - Type [bit.ly/3FDoRlt](https://bit.ly/3FDoRlt)
  - Go to [roguh.com](https://roguh.com), scroll to bottom and click **"A brief intro to computer science and programming"**
  - Type [roguh.com/intro.equipo.2021.11](/intro.equipo.2021.11/)
- Run Python code at repl.it [repl.it/languages/python3](https://repl.it/languages/python3)
  - REPL: Read, Evaluate, Print, Loop
    - Read: you type in code, the computer reads it
    - Evaluate: the computer runs the code
    - Print: the computer prints the results
    - Loop: this same thing happens all over again
  - You'll need an account later

(you can use a smartphone if you don't have a laptop)

# What to Expect

- You'll think about a few versions of 11 programs
- You'll do a few Python exercises on your Chromebook
- I'll quickly show you about 25 topics

# What is programming?

> [Programming is the art and science of translating a set of ideas into a program](https://en.wikiversity.org/wiki/What_is_%22programming%22)

> [A program is **a list of [exact] instructions a computer can follow**.](https://en.wikiversity.org/wiki/What_is_%22programming%22)

# What is programming, really?

<iframe style="margin:0 auto" width="100%" height="100%" src="https://www.youtube-nocookie.com/embed/Ct-lOOUqmyY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

youtu.be/Ct-lOOUqmyY

# What is programming, really?

You are controlling a computer: a very fast but very dumb machine.
Good thing it's very flexible! Computers are **programmable**, which means you can
change its behavior easily.

Giving instructions to someone that takes very literally, but has
special powers.

# Computer science

> [Computer science, the study of computers and computing, including their theoretical and algorithmic foundations, hardware and software, and their uses for processing information.](https://www.britannica.com/science/computer-science)

(Follow the rabbit hole)

- computers - what are they? what do they do?
- theoretical foundations - high-level math
- algorithms - instructions, recipes
- information - what exactly do they mean by this word? how does a computer store it?
- processing information - how do you do this quickly and accurately?

# What can you do with computers?

- **controlling technology** (a LOT of technology?)
- automating tasks: computers can do the boring things quickly
- analyzing data and discovering new insights
- all forms of science: biology, medicine, physics, rocket science, mathematics
- improve communication, access to knowledge
- **organizing information.** uses many fascinating branches of mathematics
- make new forms of art
- improving existing industries (healthcare, electric vehicle charging, ...)
- out-competing existing businesses

# What is a programming language?

<!-- TODO -->

# Python

<!-- TODO logo -->

# What's Python used for?

- The SciPy ecosystem is used by scientists, mathematicians, and analysts every day to process all kinds of data.
- Tensorflow is one of the most popular machine learning
  **libraries** (a tool you can use to write programs).
  It's used to create neural networks, a type of artificial intelligence.
- Flask and Django are used to power some of your favorite websites.
- Gluing things together (electric vehicle charging <-> app)
- Prototyping and practicing.
- Teaching and learning.

It's a friendly programming language :)

# We need repl.it

[repl.it/languages/python3](https://repl.it/languages/python3)

make an account later to save your programs!

# Program 0

Yes, in computer science, counting starts at 0

```python
print("Hello, world!")
```

# Program 1

```python
name = "Alice"
message = "Hello," + name
print(message)
```

# Program 1: details

```python
name = "Alice"
message = "Hello," + name
print(message)
```

## from the computer's point of view, what's happening???

- line 1: does nothing! comments are meant for people to read
- line 2: stores data
- line 3:
  - reads data AND
  - processes data AND
  - stores data
- line 4:
  - reads data AND
  - processes data

# Program 1: output

```python
name = "Alice"
message = "Hello," + name
print(message)
```

### Output

```
Hello,Alice
```

# Program 1.1

```python
name = "Alice"
message = "Hello, " + name
print(message)
```

The line that starts with `#` is a **comment** meant to help people reading the code.

## Output

```
Hello, Alice
```

# Program 1.2

```python
name = "Alice"
print("Hello, " + name + "!")
```

# Program 1.2: output

```python
name = "Alice"
print("Hello, " + name + "!")
```

## Output

```
Hello, Alice!
```

# Program 2: Two variables

```python
name = "Zach"
greeting = "Goodbye"
print(greeting + name)
```

<!-- what does it do? can you fix it? -->

# What do `>>>` and `$` at the beginning of a line mean?

# Problem: ABBA

```
a = "a"
b = "b"
print(<YOUR CODE HERE>)
```

Output:

```
abba
```

# Other test cases

Test 2:

```
a = "alpha"
b = "bet"
```

Output:

```
alphabetbetalpha
```

Test 3:

```
a = "word"
b = "word"
```

Output:

```
wordwordwordword
```

# CodingBat!

codingbat.com -> Python -> String-1 -> `make_abba`

[codingbat.com/prob/p182144](https://codingbat.com/prob/p182144)

To do more coding bat you'll need to learn about list/string slices
and other Python concepts...

# Program 3: Arithmetic and Numbers

```python
```

# Program 3.1: A googol

```python
```

# Program 4: More math and modules/libraries

```python
```

# Program 5: Input

```python
```

# I/O

# Program 6: Turtle basics

```python
```

# How to run

To run turtle programs in repl.it, you need to make an account.

[replit.com/languages/python_turtle](https://replit.com/languages/python_turtle)

You also need it for programs 9 to 11 to download things from the web.

# Program 7: Stairs

```python
```

# Program 8: For loops (AKA iteration)

```python
import turtle

for color in ['red', 'green', 'orange', 'blue']:
    turtle.color(color)
    turtle.forward(75)
    turtle.left(90)
```

# Program 8.1: Speedup turtle when drawing complex things

```python
```

# Optional program A: for loop with code repetition

```python
```

## Output

```shell
```

# Optional program B: doubly nested for loop

```python
```

## Output

```shell
```

# Optional program C: function

```python
```

## Output

```shell
```

# Optional program D: recursion

```python
```

# Optional program E: recursion vs iteration

```python
```

## Output

```shell
```

# Program 9: lists and indexing

```python
```

# Optional program X: list slices

```python
```

# Optional program Y: list length

```python
```

# Optional program Z: dictionaries

```python
```

# Optional program H: boolean and if-statements

```python
```

# Optional program G: string methods

```python
```

# Program 11: HTTP requests with `requests` library

```python
```

# Program 11.1: requests to Google Maps

```python
```

# Program 11.2: requests to Open Street Maps

```python
```

# Program 11.3: requests to NASA

```python
```

# Your Machine

# Yak-shaving

# Installing Python

# A warning!

Python version 2 is very old and no longer maintained.

```python
print "Hello, world!"
```

Find newer resources!

# A good sign

```
$ python --version
Python 3.9.7
```

```
>>> import sys
>>> sys.version
'3.9.7 (default, Oct 10 2021, 15:13:22) \n[GCC 11.1.0]'
```
# Turbo overview

# A list of Python features

# Linux

# Types

# Python Type hints

# Algorithms

# Algorithms: Sorting

# Algorithms: Image processing

# Data structures

# Data structures: images

# Data structures: trees

# Data structures: tries

# Databases

# HTTP

# HTML and CSS

Not programming languages. A markup language and a styling language.

# Example videogame

# Recommended resources:

- Python Tutor to get a deep understanding of the code [pythontutor.com/](https://pythontutor.com)
- GOOGLE
- official Python documentation [docs.python.org/3.9/](https://docs.python.org/3.9/)
  - Pick the Python version you have!
- a sturdy textbook
- YouTube
- free online courses

# Learning resources

All you need is a computer and time.

- self-teaching is common and feasible thanks to open-source
- the "real world" tools are freely available!
- the state of the art tools are sometimes freely available too!
- so are often-official tutorials and documentation

# Links

- [**http://learnpythonthehardway.org/**](http://learnpythonthehardway.org/)
- [practicepython.org/](https://www.practicepython.org/)
- Corey Schafer [youtube.com/user/schafer5/playlists](https://www.youtube.com/user/schafer5/playlists)
- [automatetheboringstuff.com](https://automatetheboringstuff.com/)
- MIT course on edX: [edx.org/course/introduction-to-computer-science-and-programming-7](https://edx.org/course/introduction-to-computer-science-and-programming-7)
- [wikiversity](https://en.wikiversity.org/wiki/Category:Introduction_to_Computer_Science)
- [pyladies.com/resources/](https://www.pyladies.com/resources/)

# You can also start with JavaScript

Try JavaScript!

It is used to make websites and web servers.

Learning resources are bountiful. Ask me if you want advice.

# Installing JavaScript

- You already have it!
- TypeScript, npm or yarn, node

# Program 12: JavaScript

```javascript
let num = 10
console.log(num * 20)
```

# Projects

find a project you're passionate about. make programming a hobby.

- make a cooking tool
- make a video game
- make an AI
- make a website, add JavaScript
- make an app
- run a scientific experiment
- make *a project* run faster, handle lots of users, or lots of different scenarios
- scrape a website: youtube downloader, instagram downloader, wikipedia
  - how to do it nicely?

https://www.reddit.com/r/dailyprogrammer/

# How to supercharge your learning

- find a group to learn and practice with: online or IRL
- university degree
- bootcamps
- WORK EXPERIENCE

I can always help if you're stuck with a program or want any advice.
Reach out to me with any questions you have!

[hugo@roguh.com](mailto:hugo@roguh.com)

[roguh.com/contact](https://roguh.com/contact)

# Other programming languages

- TypeScript: JavaScript with more reliability
  - Web servers, websites
- Python with type hints: like TypeScript
- Rust: Very advanced, very fast, very reliable
  - Hardware control, web servers
- Go: Not as advanced, very fast, very reliable
  - Web servers
- C++, C: Very advanced, very fast, not so reliable. Can make Python code faster.
  - Videogames, multimedia, hardware control, operating systems, Python itself
- Java
  - Android apps (Also see Kotlin)
- Haskell, OCaml: Functional programming. OCaml is faster, Haskell has more interesting features.

# Docker

# Kubernetes

# The software at my work

# Learning computer science

Programming is a great first step.

Computer science will improve your knowledge of computers and will help you write better code.

<!-- TODO link to that mega list -->
<!-- TODO link Galassi's book -->











<!--
start with my background

students should
name themselves
why they want to program
why they'd like to learn computer science
-->

<!--
that one youtube video:

there's always errors
syntax, runtime, logic

why use data structures?
speed incredible, but is limited




ME: MANY FREE AND HIGH QUALITY (STATE OF THE ART) RESOURCES!!!!!!
a better computer and good internet can help, but you can get started on any machine and even a slow connection






https://medium.com/upperlinecode/stop-teaching-code-a1039983b39

coding <-> computer science
cooking <-> chemistry

So here are the criteria I use to determine whether a code example counts as “good”:

    Can students who don’t know this syntax yet still figure out what this code does?
    Is the code reasonably similar to what one might see “in the wild” later on?
    Are my literals meaningful (no foos and bars) and are my variables well named (no str1 and myarray)?
    Do my questions allow students to focus in on the most important part of what’s happening here?
    Do my examples rely on prior experience marketed to just one subset of my students (e.g. video games) or am I digging for examples that nearly everyone can relate to (e.g favorite foods)?





https://www.youtube.com/watch?v=MHPGeQD8TvI

explore outside of school and assignments! explore a lot!

go through basics quickly, a few hours a day. don't get stuck on the details
or take a ton of notes on syntax
just focus on understanding and trying them out
don't focus on the details yet

when you're ready, do some of your own projects
look for projects r/dailyprogrammer?
passion projects: interesting/useful
start small
don't be afraid to do something has already done!

just don't copy code without understanding
you won't learn!

ME: Python docs :D
ME: you can make your own! docs are very important
ME: sometimes I write the docs before the code
TODO ME: look at an example

try a bunch of things with your code!
reveal new things you can learn

learn how to get unstuck
EVERYONE gets stuck
everyone uses stackoverflow.com
TODO ME: give real work example

read read read read read read read read read read read read read read read read read read read read 

be ok with not knowing things
stay calm
even for good programmers, writing code without errors is rare

find a community or get a job/internship!!!
try very hard to do this

everyone always must learn!
always update, always new details to learn, always can go deeper
--->
