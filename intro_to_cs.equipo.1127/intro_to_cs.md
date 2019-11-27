---
title: Intro to programming using Python
subtitle: Equipo Academy's College Simulation Day
date: 2019.11.27
author: Hugo O. Rivera
---

<!--
start with my background

students should
name themselves
why they want to program
why they'd like to learn computer science
-->

# Intros

# Intros

- Mexican-American dreamer raised in Santa Fe, NM (thank you, DACA)
- graduated with computer science and math degrees from New Mexico Tech
- aced Triplebyte recruitment agency's assessment
- started working in a healthcare startup, now do consulting in that space
- currently at a large company making the world a greener place
- [roguh.com](https://roguh.com)

# Intros

(feel free to follow along at [roguh.com/intro_to_cs.equipo.1127](https://roguh.com/intro_to_cs.equipo.1127/)

# What is programming?

> [Programming is the art and science of translating a set of ideas into a program - **a list of [exact] instructions a computer can follow**. The person writing a program is known as a programmer (also a coder).](https://en.wikiversity.org/wiki/What_is_%22programming%22)

# What is programming, really?

<iframe style="margin:0 auto" width="100%" height="100%" src="https://www.youtube-nocookie.com/embed/Ct-lOOUqmyY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

youtu.be/Ct-lOOUqmyY

<!-- at the end of the day, you get a sandwich after nuthin' but a bit of scribblin -->

# Computer science

> [Computer science, the study of computers and computing, including their theoretical and algorithmic foundations, hardware and software, and their uses for processing information.](https://www.britannica.com/science/computer-science)

(Follow the rabbit hole)

- information - how does a computer store it?
- processing information - how do you do this quickly and accurately?
- algorithms - instructions, recipes

# What's computer science used for?

- **controlling technology** (which technology?)
- automating tasks
- analyzing data and discovering new insights
- out-competing existing businesses
- improving existing industries (healthcare, electric vehicle charging, ...)
- all forms of science

<!-- programmers! -->

# What's Python used for?

- Tensorflow is one of the most popular deep learning libraries on earth.
  It's used to create neural networks, a type of **AI**.
- The SciPy ecosystem is used by scientists, mathematicians, and analysts every day to process all kinds of data.
- Flask and Django are used to power some of your favorite websites.
- Teaching, learning. It's a friendly programming language :)

# Program 1

```python
# 1.0.py
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

# Program 1

```python
# 1.0.py
name = "Alice"
message = "Hello," + name
print(message)
```

### Output

```
$ python 1.0.py
HelloAlice
```

# Program 1.1

```
# 1.1.py
name = "Alice"
message = "Hello, " + name
print(message)
print("Hello, " + name + "!")
```

## Output

```
$ python 1.1.py
Hello Alice
Hello, Alice!
```

# Program 2: lists.py

```
favorite_foods = ["TAMALES", "nigiri sushi", "nutella"]

number_of_favorite_foods = len(favorite_foods)
index_of_favorite_food = 0

print("of my ",
      number_of_favorite_foods,
      " favorites, ",
      favorite_foods[index_of_favorite_food],
      " are my most favorite food")
```

## Output

```
of my 3 favorites, TAMALES are my most favorite food
```

# Questions about lists:

how to read each element in a list? how to add or remove elements to a list? 2D lists? quick searches for an element?

# Strings are lists

```
> len("Hello!")
> [1, 2] + [3, 4]
```

# Program 3: Slices vs. indices

Python supports slices.

|     |      |
|=====|======|
| index: | `favorite_foods[0]` |
| slice: | `favorite_foods[0:3]` |

```
most_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado"]
top_states = most_states[0:3]
print(top_states)
```

# Program 4: more slices

```
print("Hello, world!"[0:5])
```

# Program 4 output

```
print("Hello, world!"[0:5])
```

```
Hello
```


# Program 5: negative indices

```
print("Hello, world!"[-1])
print("Hello, world!"[-4:-1])
print("Hello, world!"[-4:-1])
```

# Exercises

Let's use CodingBat!

- [`hello_name` in Codingbat module String-1](https://codingbat.com/prob/p115413)
- `make_abba`
- `make_tags`

## Recommended resources:

- Python Tutor to get a deep understanding of the code [http://www.pythontutor.com/](https://pythontutor.com)
- repl.it to quickly run some code [https://repl.it/languages/python3](https://repl.it/languages/python3)
- GOOGLE, official Python documentation, a sturdy textbook, peers, etc.

# For-loops! Append! Pop!

Look at each element in a list.

```
numbers = [2, 4, 8]
total = 0
for number in numbers
    total = total + number

highest_known_power_of_two = numbers.pop()

numbers.append(6)
numbers.append(8)
numbers.append(10)

print(total)
print(numbers)
```

# Program 3: dictionaries_for_polyglots.py

```
greetings = {
  "english": "Hello, ",
  "español": "hola, "
}

greetings["sinhala"] = "හෙලෝ "
greetings["es"] = greetings["español"]
greetings["en"] = greetings["english"]

print(greetings["en"] + name)
```

Dictionaries assign **keys** to **values**.

# Program 3: dictionaries_for_polyglots.py output

```
Traceback (most recent call last):
  File, line 8, in <module>
NameError: name 'name' is not defined
```

too bad :(

# Thought-experiment

*lists can be thought of as "weaker" dictionaries*: think of a list as a dictionary with its keys set to numbers 0, 1, 2, ..., `len(list)-1`

```
list = ["a", "b", "c"]
list[0]
silly_dictionary = {-1: "negative", 0: "zero", 1: "one", "1": 1, "one": 1}
print(dictionary[0])
print(dictionary[-1])
print(dictionary[1])
print(dictionary["1"])
```

# Questions about dictionaries:

what else might you use

# Program 4: functions.py

```
def greet(person)
  message = "Hello " + person
  print(message)
```

# Program 4: functions.py output

```
```

you defined the function "`greet`" but didn't do anything with it! (that's ok)

questions:

- can a function take more arguments?
- can a function call another function?
- can a function call itself?

# Program 5: python.py

```
def run_code(instructions):
    names = {}
    stack = []

    for each_step in instructions:
        instruction, associated_data = each_step

        if instruction == "ADD_LAST_TWO":
            result = stack.pop() + stack.pop()
            stack.append(result)
        elif instruction == "PRINT":
            value = stack.pop()
            print(value)
        elif instruction == "STORE_NAME":
            name, value = associated_data
            names[name] = value
        elif instruction == "LOAD_NAME":
            stack.append(names[name])
        elif instruction == "LOAD_LITERAL":
            stack.append(associated_data)
        else:
            print("WARNING: unknown instruction", instruction)

run_code([
    ["STORE_NAME", ["name", "Alice"]],
    ["LOAD_NAME", "name"],
    ["LOAD_LITERAL", "Hello "],
    ["ADD_LAST_TWO", []],
    ["PRINT", []]
])
```

hints:

- `names` is an empty dictionary, `stack` is an empty list
- read the bottom part first

[aosabook.org/en/500L/a-python-interpreter-written-in-python.html](https://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html)

# Learning resources

All you need is a computer and some time.

- self-teaching is common and feasible thanks to open-source
  - the "real world" tools are freely available!
  - so are often-official tutorials and documentation
- examples:
  - [**http://learnpythonthehardway.org/**](http://learnpythonthehardway.org/)
  - [practicepython.org/](https://www.practicepython.org/)
  - Corey Schafer [youtube.com/user/schafer5/playlists](https://www.youtube.com/user/schafer5/playlists)
  - [automatetheboringstuff.com](https://automatetheboringstuff.com/)
  - MIT course on edX: edx.org/course/introduction-to-computer-science-and-programming-7
  - [wikiversity](https://en.wikiversity.org/wiki/Category:Introduction_to_Computer_Science)
  - https://www.pyladies.com/resources/
- find a project you're passionate about. make programming your hobby.
  - make a website
  - make a video game
  - make an AI
  - make an app
  - make *it* run fast, handle lots of users, or lots of different scenarios
- find a group to learn with
- university degree

Reach out to me with any questions you have!

[hugo@roguh.com](mailto:hugo@roguh.com)

# Language doesn't matter

Python is friendly and has many real-world uses.

Try JavaScript! Or C if you want more control over the machine, or Haskell if you want to peek into the future of programming.

Learning resources are bountiful. Ask me if you want advice.
