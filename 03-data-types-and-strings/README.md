# Chapter 3 — Python Data Types & Strings

This chapter explains Python's basic built-in data types and gives a strong foundation for working with strings.

The goal is not only to remember syntax, but to understand:

- what objects are
- how names refer to objects
- how Python's basic types behave
- how strings are indexed and sliced
- which string operations return new objects
- what mutable and immutable mean
- how to read and review Python code involving these concepts

---

## 1. The Python Object Model

A useful mental model is:

> **Names refer to objects. Objects have a type and a value.**

For example:

```python
age = 24
name = "Sam"
active = True
```

Think of it as:

```text
age    ───────> 24
                  │
                  └── int object

name   ───────> "Sam"
                  │
                  └── str object

active ───────> True
                  │
                  └── bool object
```

A name can later refer to an object of another type:

```python
age = 24
age = "twenty four"
```

The name `age` changed what object it refers to. The objects themselves still have types.

---

## 2. Checking Types

Use `type()`:

```python
age = 24
name = "Sam"
price = 99.5
active = True

print(type(age))
print(type(name))
print(type(price))
print(type(active))
```

Typical output:

```text
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
```

When reading Python code, asking **"What type is this object?"** is often one of the first useful questions.

---

## 3. Important Built-in Types

| Type | Example | Purpose |
|---|---|---|
| `int` | `24` | Whole numbers |
| `float` | `24.5` | Floating-point numbers |
| `complex` | `3 + 4j` | Complex numbers |
| `bool` | `True` | Boolean values |
| `str` | `"Python"` | Text |
| `NoneType` | `None` | Absence of a value |

Later chapters introduce `list`, `tuple`, `set`, `dict`, and other important types.

---

## 4. Integers — `int`

```python
age = 24
count = 100
temperature = -10
```

Python integers can grow very large:

```python
x = 10 ** 100
print(x)
```

Unlike Java's fixed-width `int` and `long`, Python's normal `int` supports arbitrarily large integers.

---

## 5. Floating-Point Numbers — `float`

```python
price = 99.99
temperature = 36.5
ratio = 0.75
```

Floating-point numbers have limited precision.

```python
print(0.1 + 0.2)
```

may produce:

```text
0.30000000000000004
```

This is a general binary floating-point limitation, not a Python-specific bug.

---

## 6. Complex Numbers — `complex`

Python has built-in support for complex numbers:

```python
z = 3 + 4j

print(z.real)
print(z.imag)
```

Output:

```text
3.0
4.0
```

You will not use these heavily in ordinary backend development, but they can appear in scientific computing.

---

## 7. Booleans — `bool`

Python uses:

```python
True
False
```

Example:

```python
is_logged_in = True
is_admin = False
```

A useful detail is that `bool` is a subtype of `int`:

```python
print(True + True)
```

produces:

```text
2
```

because:

```text
True  -> 1
False -> 0
```

---

## 8. `None`

`None` represents the absence of a value:

```python
result = None
```

A common check is:

```python
if result is None:
    print("No result")
```

For a Java developer, the closest initial comparison is:

```text
Python None ≈ Java null
```

but they are not identical in every detail.

Prefer:

```python
value is None
```

rather than:

```python
value == None
```

---

## 9. Type Conversion

Python provides functions for converting values:

```python
age = int("24")
price = float("99.5")
text = str(100)
```

Other examples:

```python
bool(1)      # True
bool(0)      # False
```

Conversions can fail:

```python
int("hello")
```

raises `ValueError`.

Conversion generally produces another object:

```python
age = "24"
new_age = int(age)
```

Now:

```text
age      -> "24"   (str)
new_age  -> 24     (int)
```

---

# Strings

## 10. Strings — `str`

Strings represent text:

```python
name = "Sam"
city = 'Lucknow'
```

Both single and double quotes are valid.

A string is also a **sequence of characters**.

For example:

```text
Python
012345
```

---

## 11. String Indexing

Python uses zero-based indexing:

```python
word = "Python"

print(word[0])
print(word[1])
print(word[2])
```

Output:

```text
P
y
t
```

This is conceptually similar to Java's:

```java
word.charAt(0);
```

but Python uses:

```python
word[0]
```

---

## 12. Negative Indexing

Python supports indexing from the end:

```python
word = "Python"

print(word[-1])
print(word[-2])
```

Output:

```text
n
o
```

The indexes are:

```text
 P   y   t   h   o   n
 0   1   2   3   4   5
-6  -5  -4  -3  -2  -1
```

Therefore:

```python
word[-1]
```

means "get the last character."

---

## 13. `len()`

Use `len()` to get the length of a string:

```python
word = "Python"

print(len(word))
```

Output:

```text
6
```

Java equivalent:

```java
word.length()
```

Python uses the general function:

```python
len(object)
```

---

## 14. Strings Are Immutable

You cannot modify a character inside a string:

```python
word = "Python"

word[0] = "J"
```

This raises an error.

Strings are **immutable**:

> Once a string object is created, its contents cannot be changed.

You can create a new string instead:

```python
word = "Python"
word = "J" + word[1:]
```

Now `word` refers to:

```text
Jython
```

The original string was not modified.

---

## 15. Java Comparison — String Immutability

Java:

```java
String name = "Sam";
name = name.toUpperCase();
```

Python:

```python
name = "Sam"
name = name.upper()
```

In both cases, the original string is not modified. A new string is produced and the name refers to it.

---

## 16. String Concatenation

Strings can be combined with `+`:

```python
first_name = "Sam"
last_name = "Parihar"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Sam Parihar
```

---

## 17. String Repetition

Python supports repetition:

```python
print("ha" * 3)
```

Output:

```text
hahaha
```

The meaning of an operator depends on the types involved:

```python
3 * 5          # multiplication
"ha" * 3       # string repetition
```

---

## 18. Escape Sequences

Common escape sequences:

| Escape | Meaning |
|---|---|
| `\\n` | New line |
| `\\t` | Tab |
| `\\\\` | Backslash |
| `\\"` | Double quote |
| `\\'` | Single quote |

Example:

```python
print("Hello\\nWorld")
```

---

## 19. Multiline Strings

Triple quotes allow strings to span multiple lines:

```python
message = """
Hello
Welcome
Good morning
"""
```

They are often used for multiline text, documentation, templates, and docstrings.

---

## 20. Raw Strings

A raw string uses the `r` prefix:

```python
path = r"C:\\Users\\Sam\\Documents"
```

Raw strings are useful when backslashes should generally be treated literally, especially with Windows paths and regular expressions.

---

## 21. String Slicing

The basic form is:

```python
text[start:stop]
```

The `start` index is included and the `stop` index is excluded.

```python
text = "Python"

print(text[0:3])
```

Output:

```text
Pyt
```

Remember:

```text
start -> included
stop  -> excluded
```

---

## 22. More Slicing

```python
text = "Python"

text[:3]       # Pyt
text[2:]       # thon
text[:]        # Python
```

---

## 23. Slicing with a Step

Full syntax:

```python
text[start:stop:step]
```

Example:

```python
text = "Python"

print(text[0:6:2])
```

Output:

```text
Pto
```

It takes indexes `0`, `2`, and `4`.

---

## 24. Reversing a String

A common Python idiom:

```python
text = "Python"

print(text[::-1])
```

Output:

```text
nohtyP
```

This means the sequence is traversed with a step of `-1`.

---

## 25. String Membership

Check whether text exists inside another string:

```python
text = "Python programming"

print("Python" in text)
print("Java" in text)
```

Output:

```text
True
False
```

You can also use:

```python
"Java" not in text
```

---

## 26. String Comparison

Strings can be compared:

```python
a = "apple"
b = "banana"

print(a == b)
print(a != b)
print(a < b)
```

Ordering follows Unicode code-point ordering.

---

# String Methods

## 27. `upper()` and `lower()`

```python
text = "Python"

print(text.upper())
print(text.lower())
```

Output:

```text
PYTHON
python
```

They return new strings.

---

## 28. `strip()`

Useful for cleaning input:

```python
name = "   Sam   "

print(name.strip())
```

Output:

```text
Sam
```

Related methods:

```python
lstrip()
rstrip()
```

---

## 29. `replace()`

```python
text = "I like Java"

new_text = text.replace("Java", "Python")

print(new_text)
```

Output:

```text
I like Python
```

The original string is unchanged.

---

## 30. `split()`

`split()` converts a string into a list of pieces:

```python
sentence = "Python is easy"

words = sentence.split()

print(words)
```

Output:

```text
['Python', 'is', 'easy']
```

You can specify a separator:

```python
data = "apple,banana,orange"
items = data.split(",")
```

Result:

```text
['apple', 'banana', 'orange']
```

Lists are covered deeply in Chapter 4.

---

## 31. `join()`

`join()` combines strings using a separator:

```python
words = ["Python", "is", "fun"]

sentence = " ".join(words)

print(sentence)
```

Output:

```text
Python is fun
```

Another example:

```python
"-".join(["2026", "09", "22"])
```

Result:

```text
2026-09-22
```

Remember:

```text
split() -> break text apart
join()  -> combine pieces
```

---

## 32. `startswith()` and `endswith()`

```python
filename = "model.pt"

print(filename.endswith(".pt"))
```

Output:

```text
True
```

Another example:

```python
url = "https://example.com"

print(url.startswith("https://"))
```

---

## 33. `find()`

```python
text = "Python programming"

print(text.find("program"))
```

It returns the starting index.

If the substring is not found, `find()` returns:

```text
-1
```

---

## 34. `count()`

```python
text = "banana"

print(text.count("a"))
```

Output:

```text
3
```

---

# Formatting and Text

## 35. f-Strings

f-strings are the preferred way to build many formatted strings:

```python
name = "Sam"
age = 24

message = f"My name is {name} and I am {age} years old."

print(message)
```

Expressions can also be placed inside:

```python
price = 100
quantity = 3

print(f"Total: {price * quantity}")
```

Output:

```text
Total: 300
```

---

## 36. Formatting Numbers with f-Strings

```python
price = 123.456789

print(f"{price:.2f}")
```

Output:

```text
123.46
```

`.2f` means a floating-point number with two decimal places.

---

## 37. Unicode

Python 3 strings support Unicode text:

```python
name = "समृद्धि"
message = "Hello दुनिया"
```

Python strings are not limited to English or ASCII.

---

## 38. `str` vs `bytes`

These are different types:

```python
text = "hello"
data = b"hello"

print(type(text))
print(type(data))
```

Output:

```text
<class 'str'>
<class 'bytes'>
```

Useful mental model:

```text
str
 ↓
text

bytes
 ↓
raw byte data
```

`bytes` becomes important when working with files, networking, binary protocols, images, sensors, and robotics systems.

---

# Understanding Code

## 39. `==` vs `is`

```python
a == b
```

asks:

> Do these objects have equal values?

```python
a is b
```

asks:

> Are these the exact same object?

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Expected:

```text
True
False
```

Same contents, different objects.

A common use of `is`:

```python
if value is None:
    ...
```

---

## 40. Truthiness

Python objects can be evaluated in Boolean contexts.

```python
name = ""

if name:
    print("Name exists")
```

Nothing is printed because an empty string is falsy.

A non-empty string is truthy:

```python
name = "Sam"

if name:
    print("Name exists")
```

This is common Python:

```python
if username:
    ...
```

---

## 41. Reading Python Expressions

When reading code, ask:

1. What object is this name referring to?
2. What is its type?
3. Is it mutable?
4. What operation is being performed?
5. Does the operation modify the object?
6. Or does it return a new object?
7. What type does the result have?

Example:

```python
name = "  SAM  "
name = name.strip().lower()
```

Trace it as:

```text
"  SAM  "
    ↓
strip()
    ↓
"SAM"
    ↓
lower()
    ↓
"sam"
    ↓
name
```

This style of tracing is useful when reading unfamiliar Python code.

---

# Java → Python Quick Comparison

| Concept | Java | Python |
|---|---|---|
| Integer | `int` | `int` |
| Decimal | `double` | `float` |
| Boolean | `boolean` | `bool` |
| String | `String` | `str` |
| Null value | `null` | `None` |
| String length | `str.length()` | `len(str)` |
| Character access | `str.charAt(0)` | `str[0]` |
| String slicing | More manual | `str[start:stop]` |
| String formatting | `String.format()` etc. | f-strings |
| String immutable | Yes | Yes |
| Logical AND | `&&` | `and` |
| Logical OR | `||` | `or` |
| Logical NOT | `!` | `not` |

Use these comparisons to orient yourself, but learn Python's own model rather than translating every line from Java.

---

# Practice Checklist

By the end of Chapter 3, be comfortable with:

```python
type(x)
len(x)

x[0]
x[-1]

x[start:stop]
x[start:stop:step]
x[::-1]

x.upper()
x.lower()
x.strip()
x.replace()
x.split()

"separator".join(items)

x.startswith(...)
x.endswith(...)
x.find(...)
x.count(...)

"x" in text
"x" not in text

f"{name} is {age} years old"
```

Also understand:

```text
int
float
complex
bool
str
None
```

and:

```text
==  -> value equality
is  -> object identity
```

as well as:

```text
mutable
immutable
```

---

# Chapter 3 Practice

Suggested repository location:

```text
02-python-fundamentals/
└── 05-data-types-and-strings.py
```

Practice:

1. Type explorer
2. String analyzer
3. Username processor
4. Email analyzer
5. Reverse text
6. Palindrome checker
7. Word counter
8. Basic text formatter

Also practice code reading and review involving:

- indexing
- slicing
- immutability
- truthiness
- `==` vs `is`
- string methods
- input edge cases
- idiomatic Python

---

# Key Takeaways

### 1. Names refer to objects

```python
age = 24
```

The name `age` refers to an integer object.

### 2. Objects have types

```python
type(age)
```

tells you the object's type.

### 3. Strings are sequences

```python
text[0]
text[-1]
text[1:4]
```

### 4. Strings are immutable

Methods such as:

```python
upper()
lower()
replace()
strip()
```

return new strings.

### 5. Python has powerful slicing

```python
text[start:stop:step]
```

### 6. `==` and `is` are different

```text
==  -> value equality
is  -> object identity
```

### 7. Python has truthiness

```python
if text:
```

is a normal and useful Python pattern.

### 8. `split()` and `join()` are fundamental

```text
split -> break text apart
join  -> combine pieces
```

### 9. `str` and `bytes` are different

```text
str   -> text
bytes -> raw byte data
```

### 10. Mutability will become fundamental

Understanding:

```text
immutable objects
vs
mutable objects
```

is essential before learning Python's collections and OOP.
"""

path = Path("/mnt/data/03-data-types-and-strings")
path.mkdir(parents=True, exist_ok=True)
file_path = path / "README.md"
file_path.write_text(content, encoding="utf-8")
print(file_path)

