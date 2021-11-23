---
title: Intro to programming using Python
subtitle: Equipo Academy's College Simulation Day
date: 2021.11.24
author: Hugo O. Rivera
---

<!-- translate title -->

# Intros

<!-- name, why learn programming? -->

# Intros

<!-- translate -->

- Mexican, DACA
- Santa Fe, NM
- computer science and math, New Mexico Tech, 2018
- Triplebyte recruitment
- healthcare startups
- renewable energy company building software for electric vehicle charging stations

# Visit

- [roguh.com/e](/e)
- [roguh.com/equipo](/equipo)

# What to Expect

<!-- translate -->

- 12 + 1 programs
- Python exercises on your Chromebook

# What is programming?

<!-- ask a student to read it -->

> [Programming is the art and science of translating a set of ideas into a program](https://en.wikiversity.org/wiki/What_is_%22programming%22)

> [A program is **a list of [exact] instructions a computer can follow**.](https://en.wikiversity.org/wiki/What_is_%22programming%22)

# What is programming, really?

<iframe style="margin:0 auto" width="100%" height="100%" src="https://www.youtube-nocookie.com/embed/Ct-lOOUqmyY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

youtu.be/Ct-lOOUqmyY

# What is programming, really?

<!-- translate -->

Computers:

- Fast
- Very dumb
- Very flexible. **Programmable**
- Takes instructions very literally, has special powers.
  - What special powers?

# What can you do with computers?

<!-- translate -->

- **controlling technology** (a LOT of technology?)
- automating tasks: computers can do the boring things quickly
- analyzing data and discovering new insights
- all forms of science: biology, medicine, physics, rocket science, mathematics
- improve communication, access to knowledge
- **organizing information.** uses many fascinating branches of mathematics
- make new forms of art
- improving existing industries (healthcare, electric vehicle charging, ...)
- out-competing existing businesses

# Visit

[repl.it/languages/python3](https://repl.it/languages/python3)

- REPL: Read, Evaluate, Print, Loop
  <!-- translate -->
  - Read: you type in code, the computer reads it
  - Evaluate: the computer runs the code
  - Print: the computer prints the results
  - Loop: this same thing happens all over again

# Program 0

```python
print("Hello, world!")
```

<!-- translate -->

# Program 1

```python
name = "Alice"
message = "Hello," + name
print(message)
```

<!-- translate -->

# Program 1: details

```python
name = "Alice"
message = "Hello," + name
print(message)
```

## If you typed this program, what would it show?

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

## Output

```
Hello, Alice
```

# What is a programming language for?

<!-- translate -->

> for expressing a set of detailed instructions for a digital computer

[Read an overview of programming languages here](https://www.britannica.com/technology/computer-programming-language)

# Python

![](./python.svg)

<!-- translate -->

Easy to learn, commonly used by scientist and companies.

# Uses?

<!-- translate -->

- [SciPy](https://scipy.org/), [Numpy](https://numpy.org/), [Pandas](https://pandas.pydata.org/): scientists, mathematicians, and analysts every day to process all kinds of data.
- [Tensorflow](https://www.tensorflow.org/): popular machine learning **libraries**.
  - Neural networks, artificial intelligence.
- [Flask](https://flask.palletsprojects.com/) and [Django](https://www.djangoproject.com/): web servers.
- My work: controlling how fast electric vehicles charge

In general:

- Writing programs quickly.
- Practicing.
- Learning.

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

<!-- translate -->

# Problem: ABBA

```
first = "a"
second = "b"
print(<YOUR CODE HERE>)
```

It should print:

```
abba
```

# CodingBat!

codingbat.com -> Python -> String-1 -> `make_abba`

[codingbat.com/prob/p182144](https://codingbat.com/prob/p182144)

To do more coding bat you'll need to learn about list/string slices
and other Python concepts...

# Program 3: Arithmetic and Numbers

```python
print(1 + 2 * 4 - 10 / 2)
print(2 ** 10)
print(195.51 // 10)
```

# Program 3.1: A googol and scientific notation

```python
print(10 ** 100)
print(1e100)
```

- `5e23` means `5 * 10 ** 23`
- `3.95e-5` means `3.95 * 10 ** (-5)`
- `^` has a different meaning in Python.
  - `142 ^ 51` is not `142 ** 51`

# Program 4: More math and modules/libraries

```python
import math
radius = 145
print(math.pi * radius ** 2)
```

# Program 5: Input

```python
import math
user_input = input("Please enter the radius: ")
radius = float(user_input)
print(math.pi * radius ** 2)
```

## Names for numbers

<!-- translate -->

A float is a number with a "floating point": 1.1, 1.0, 99.124124, 0.000123, -50.05

An integer is a whole number: 1, -50, 0, 1000000000000

# Exercise: compute the volume of a cube

<!-- translate -->

```
user_input = <YOUR CODE HERE>
side_length = float(user_input)
print(<YOUR CODE HERE>)
```

# Exercise: compute the volume of a cube

```
user_input = <YOUR CODE HERE>
side_length = float(user_input)
print(<YOUR CODE HERE>)
```

<!-- translate -->

- How to get the side length?
- How to compute the volume of a cube?

# I/O

<!-- translate -->

Two very important things a computer does:

- Input. Receive information from the world.
  - Keyboard, touch screen
  - Thermometer, other special hardware
  - GPS
  - Hard drives, SSDs, RAM, memory
  - Network (other computers)
- Output. Deliver information to the world.
  - Screens
  - How fast a rocket should go, other special hardware
  - Hard drives, SSDs, RAM, memory
  - Network (other computers)

# Program 6: Turtle basics

```python
import turtle

turtle.forward(100)
turtle.color("red")
turtle.left(90)
turtle.forward(50)
```

# How to run

<!-- translate -->

You need a free account.

[replit.com/languages/python_turtle](https://replit.com/languages/python_turtle)

# Program 7: Stairs

```python
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
```

# Program 8: For loops (AKA iteration)

```python
import turtle

for color in ['red', 'green', 'orange', 'blue']:
    turtle.color(color)
    turtle.forward(75)
    turtle.left(90)
```

# Program 8.1: Stairs v2

Version 2

```python
import turtle

for stair_count in range(40)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
```

# Program 8.2: Colorful Stairs

```python
import turtle

colors = ["red", "orange", "green", "blue", "purple"]

for stair_count in range(40):
    # Pick a color
    turtle.color(colors[stair_count % len(colors])
    # Draw 1 stair
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
```

# Exercise: Draw a square

<!-- translate -->

```
import turtle

side_length = 100

<YOUR CODE HERE>
```

# Exercise: Draw a square next to a triangle

<!-- translate -->

```
import turtle

side_length = 100

<YOUR CODE HERE>
```

# Trick: Speedup turtle when drawing complex things

```python
turtle.speed("fastest")
```

```python
turtle.tracer(False) # Hide the turtle until it's done
turtle.update() # Show what the turtle drew
```

# Advanced program: recursion

```python
import turtle

def koch_line(width, depth=0):
    if depth <= 0:
        turtle.forward(width)
    else:
        koch_line(width / 3, depth - 1)
        turtle.left(60)
        koch_line(width / 3, depth - 1)
        turtle.right(2 * 60)
        koch_line(width / 3, depth - 1)
        turtle.left(60)
        koch_line(width / 3, depth - 1)

def koch_snowflake(width=100, depth=1):
    for _ in range(3):
        koch_line(width, depth)
        turtle.right(180 - 60)

turtle.speed('fastest')
koch_snowflake(200, 3)
turtle.done()
```

- functions
- recursive functions
- more for loops
- if-statements
- `number1 <= number2`
- function arguments with default values

<!-- maybe l8r... bilingual and we have to make accounts... and it's 26 students

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

--->

# Program 11: HTTP requests with `requests` library

<!-- translate -->

<!-- TODO -->

You need a repl.it account for these programs!

```python
```

# Program 11.1: requests to Google Maps

<!-- TODO -->

```python
```

# Program 11.2: requests to Open Street Maps

<!-- TODO -->

```python
```

# Program 11.3: requests to NASA

<!-- TODO -->

```python
```

# A warning!

<!-- translate -->

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
# A list of Python features

<!-- TODO -->

- Type hints

# Some computer science and programming topics

- Linux: install it on a laptop
- Types
- Algorithms: Sorting, image processing
- Data structures: lists, trees, searching for words quickly, organize data
- Databases
- HTTP
- HTML and CSS
- Docker, Kubernetes

# Videogames in Python

Use pygame at [replit.com/new/pygame](https://replit.com/new/pygame)

[askpython.com/python/examples/easy-games-in-python](https://www.askpython.com/python/examples/easy-games-in-python)

[realpython.com/pygame-a-primer/](https://realpython.com/pygame-a-primer/)

Free and powerful: [Unity](https://unity.com/) and [Godot](https://godotengine.org/).

# Recommended resources:

<!-- translate -->

Everyone uses these, even professionals:

- Google
- Stackoverflow
- Python documentation [docs.python.org/3.9/](https://docs.python.org/3.9/)
  - Pick the Python version you have!

Free:

- Python Tutor to get a deep understanding of the code [pythontutor.com/](https://pythontutor.com)
- A sturdy textbook
- [YouTube](https://www.youtube.com/results?search_query=python+for+beginners)
- [Introduction to Python Programming at Udacity](https://classroom.udacity.com/courses/ud1110)
- Many more

Money:

- $29.99 [Learn Python 3 The Hard Way](https://shop.learncodethehardway.org/access/buy/9/)

# Learning resources

<!-- translate -->

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
- [Mark Galassi's serious programming course](https://markgalassi.sourceforge.io/small-courses-html/index.html)

# You can also start with JavaScript

<!-- translate -->

Try JavaScript!

It is used to make websites and web servers.

Learning resources are bountiful. Ask me if you want advice.

# Installing JavaScript

- You already have it!
  - Press Ctrl+Shift+C on your web browser
- When you know more, install: TypeScript, npm or yarn, node

![](./ctrl_shift_c.png)

# Program 12: JavaScript

<!-- translate -->

```javascript
let user_input = prompt("Enter the size of a square")
let number = Number(user_input)
let area = number * number
console.log("The area is " + area)
```

# Projects

<!-- translate -->

find a project you're passionate about. make programming a hobby.

- a cooking tool
- a video game
- an AI
- a website, add JavaScript
- an app
- a scientific experiment
- faster, lots of users, different scenarios
- scrape a website: youtube downloader, instagram downloader, wikipedia

[reddit.com/r/dailyprogrammer/](https://www.reddit.com/r/dailyprogrammer/)

# Aprende a aprender

<!-- translate -->
<!-- TODO -->

Learn to teach yourself

As a professional, I have to learn new technologies every few years.

# How to learn more

- a group
- a group online
- university degree
- bootcamps
- internships
- work experience

[hugo@roguh.com](mailto:hugo@roguh.com)

[roguh.com/contact](https://roguh.com/contact)

# Other programming languages

<!-- translate -->
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


# Advice

<!-- translate -->

[How I would learn to code (if I could start over)](https://www.youtube.com/watch?v=MHPGeQD8TvI)

- explore outside of school and assignments! explore a lot!

- go through basics quickly, a few hours a day.
  - don't get stuck on the details or take a ton of notes on syntax
  - just focus on understanding and trying things out

- when you're ready, do some of your own projects
  - passion projects: interesting/useful
  - start small
  - don't be afraid to do something has already done!

- just don't copy code without understanding. you won't learn!

- try a bunch of things with your code!
  - reveal new things you can learn

- learn how to get unstuck
  - EVERYONE gets stuck
  - everyone uses stackoverflow.com
- read read read read read read read read read read read read read read read read read read read read 

- be ok with not knowing things
  - stay calm
- even for good programmers, writing code without errors is rare

- find a community or get a job/internship!!! try very hard to do this

- everyone always must learn!
  - always update, always new details to learn, always can go deeper

