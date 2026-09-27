# Chapter 4 — Python Collections & Data Structures

Python provides several built-in data structures for storing and organizing multiple values.

The four most commonly used collection types are:

- `list`
- `tuple`
- `set`
- `dict`

Understanding these data structures is essential for writing, reading, and reviewing Python code.

---

## 1. What Are Collections?

A collection is a data structure that allows us to store multiple values together.

Instead of:

```python
student1 = "Alice"
student2 = "Bob"
student3 = "Charlie"
```

we can use:

```python
students = ["Alice", "Bob", "Charlie"]
```

Now we can easily:

- iterate over the students
- access individual students
- add or remove students
- search for a student
- pass the collection to a function

Collections are used everywhere in Python applications, including:

- APIs
- databases
- configuration
- data processing
- machine learning
- robotics
- ROS/ROS2
- backend systems

---

# 2. Python's Main Collection Types

| Type | Ordered | Mutable | Duplicates | Main Purpose |
|---|---|---|---|---|
| `list` | Yes | Yes | Yes | General-purpose collection |
| `tuple` | Yes | No | Yes | Fixed collection of values |
| `set` | No guaranteed order | Yes | No | Unique values / membership |
| `dict` | Yes* | Yes | Keys: No | Key-value relationships |

\* Python dictionaries preserve insertion order.

A useful mental model:

```text
list   → ordered collection of items
tuple  → fixed ordered collection
set    → unique collection of items
dict   → key → value mapping
```

---

# 3. Choosing the Right Data Structure

The choice of data structure should depend on what the program needs to do.

Ask:

1. Do I need ordering?
2. Can the data change?
3. Are duplicate values allowed?
4. Do I need fast membership checking?
5. Do I need to associate keys with values?

### Use a `list` when:

You need an ordered, changeable collection.

```python
numbers = [10, 20, 30, 40]
```

### Use a `tuple` when:

You have a fixed group of related values.

```python
coordinates = (28.61, 77.20)
```

### Use a `set` when:

You need unique values or frequent membership checks.

```python
languages = {"Python", "Java", "C++"}
```

### Use a `dict` when:

You need to associate one piece of information with another.

```python
student = {
    "name": "Alice",
    "age": 20,
    "marks": 90
}
```

---

# 4. Lists

A `list` is an ordered and mutable collection.

```python
numbers = [10, 20, 30, 40]
```

Lists:

- preserve order
- support indexing
- support slicing
- can be modified
- allow duplicate values
- can contain different types

Example:

```python
data = [10, "Python", True, 3.14]
```

Python lists can contain objects of different types.

---

## 4.1 List Indexing

Indexes start from `0`.

```python
numbers = [10, 20, 30, 40]
```

```text
Index:   0    1    2    3
Value:  10   20   30   40
```

Therefore:

```python
numbers[0]    # 10
numbers[2]    # 30
```

---

## 4.2 Negative Indexing

Python supports negative indexes.

```text
Index:  -4   -3   -2   -1
Value:  10   20   30   40
```

Therefore:

```python
numbers[-1]   # 40
numbers[-2]   # 30
```

Negative indexing is useful when accessing values from the end of a collection.

---

## 4.3 List Slicing

Lists support slicing just like strings.

```python
numbers = [10, 20, 30, 40, 50]
```

```python
numbers[1:4]
```

Result:

```python
[20, 30, 40]
```

The general syntax is:

```python
collection[start:stop:step]
```

Remember:

> `stop` is excluded.

Examples:

```python
numbers[:3]
numbers[2:]
numbers[::2]
numbers[::-1]
```

---

# 5. Lists Are Mutable

Lists can be modified after they are created.

```python
numbers = [10, 20, 30]

numbers[1] = 99

print(numbers)
```

Output:

```text
[10, 99, 30]
```

This is called **mutation**.

Compare this with strings:

```python
name = "Sam"
```

Strings cannot be modified in place because strings are immutable.

---

# 6. Adding Elements to a List

## `append()`

Adds one element to the end.

```python
numbers = [10, 20, 30]

numbers.append(40)
```

Result:

```python
[10, 20, 30, 40]
```

---

## `insert()`

Adds an element at a specific index.

```python
numbers = [10, 20, 30]

numbers.insert(1, 99)
```

Result:

```python
[10, 99, 20, 30]
```

---

## `extend()`

Adds multiple elements from another iterable.

```python
numbers = [1, 2, 3]

numbers.extend([4, 5])
```

Result:

```python
[1, 2, 3, 4, 5]
```

This is different from:

```python
numbers.append([4, 5])
```

which produces:

```python
[1, 2, 3, [4, 5]]
```

The list `[4, 5]` becomes a single element.

---

# 7. Removing Elements from a List

## `remove()`

Removes the first matching value.

```python
numbers = [10, 20, 30]

numbers.remove(20)
```

Result:

```python
[10, 30]
```

`remove()` works with a **value**, not an index.

---

## `pop()`

Removes and returns an element using its index.

```python
numbers = [10, 20, 30]

value = numbers.pop(1)
```

Now:

```python
value      # 20
numbers    # [10, 30]
```

Without an index:

```python
numbers.pop()
```

removes and returns the last element.

---

## `del`

You can delete an element using its index:

```python
numbers = [10, 20, 30]

del numbers[1]
```

Result:

```python
[10, 30]
```

---

## `clear()`

Removes all elements:

```python
numbers.clear()
```

Result:

```python
[]
```

---

# 8. Membership and Length

Use `in` to check membership:

```python
numbers = [10, 20, 30]

20 in numbers
```

Result:

```text
True
```

Use `not in`:

```python
50 not in numbers
```

Use `len()` to find the number of elements:

```python
len(numbers)
```

---

# 9. Iterating Over Lists

The most common way to iterate over a list is:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Python allows direct iteration over the values without manually managing an index.

---

# 10. `enumerate()`

Sometimes both the index and value are needed.

Instead of:

```python
for i in range(len(numbers)):
    print(i, numbers[i])
```

Python provides `enumerate()`:

```python
for i, number in enumerate(numbers):
    print(i, number)
```

Output:

```text
0 10
1 20
2 30
```

This is a very common Python pattern.

---

# 11. Sorting

Python provides two important ways to sort collections.

## `sort()`

`sort()` modifies the existing list.

```python
numbers = [30, 10, 20]

numbers.sort()

print(numbers)
```

Result:

```python
[10, 20, 30]
```

---

## `sorted()`

`sorted()` returns a new sorted collection.

```python
numbers = [30, 10, 20]

result = sorted(numbers)
```

Now:

```python
numbers   # [30, 10, 20]
result    # [10, 20, 30]
```

The key difference:

```text
list.sort()
    ↓
modifies the existing list

sorted(...)
    ↓
returns a new sorted result
```

This distinction is important when reviewing code for unintended mutations.

---

# 12. References and Aliasing

Python variables are names referring to objects.

Consider:

```python
a = [1, 2, 3]
b = a
```

`b = a` does **not** create a new list.

Both names refer to the same list object.

```text
        ┌──────────────┐
a ─────►│  [1, 2, 3]   │
        └──────────────┘
               ▲
b ─────────────┘
```

Therefore:

```python
b.append(4)

print(a)
```

produces:

```python
[1, 2, 3, 4]
```

This behavior is called **aliasing**.

---

# 13. `==` vs `is`

When working with collections, understanding this distinction is essential.

## `==`

Checks whether two objects have equal values.

```python
a = [1, 2, 3]
b = [1, 2, 3]

a == b
```

Result:

```text
True
```

---

## `is`

Checks whether two names refer to the exact same object.

```python
a is b
```

Result:

```text
False
```

Because `a` and `b` are separate list objects.

But:

```python
c = a

a is c
```

is:

```text
True
```

Mental model:

```text
==  → same value?

is  → same object?
```

---

# 14. Copying a List

To create a separate list:

```python
a = [1, 2, 3]

b = a.copy()
```

Now:

```python
b.append(4)
```

does not modify `a`.

```python
a   # [1, 2, 3]
b   # [1, 2, 3, 4]
```

Another common approach is:

```python
b = a[:]
```

---

# 15. Tuples

A `tuple` is an ordered and immutable collection.

```python
coordinates = (10, 20)
```

Tuples:

- preserve order
- support indexing
- support slicing
- allow duplicates
- cannot be modified after creation

---

## 15.1 Tuple Immutability

This is invalid:

```python
coordinates = (10, 20)

coordinates[0] = 50
```

because tuples cannot be changed after creation.

This makes tuples useful for representing fixed groups of related values.

Examples:

```python
coordinates = (28.61, 77.20)
rgb = (255, 100, 50)
dimensions = (1920, 1080)
```

---

# 16. Tuple Unpacking

Python allows a tuple to be unpacked into separate variables.

```python
person = ("Sam", 24, "Engineer")

name, age, profession = person
```

Now:

```text
name       → "Sam"
age        → 24
profession → "Engineer"
```

The same concept works with other iterable objects.

---

# 17. Multiple Assignment

Python supports:

```python
a, b = 10, 20
```

This can also be used for swapping values:

```python
a = 10
b = 20

a, b = b, a
```

After the operation:

```text
a → 20
b → 10
```

This is a common Python idiom.

---

# 18. Sets

A `set` is a collection of unique values.

```python
numbers = {1, 2, 3, 4}
```

Adding an existing value does not create a duplicate:

```python
numbers.add(3)
```

The set still contains only one `3`.

Sets are particularly useful when:

- uniqueness matters
- ordering does not matter
- membership checking is frequent

---

# 19. Creating a Set from a List

A common use of sets is removing duplicates:

```python
numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)
```

Result:

```python
{1, 2, 3, 4}
```

Be aware that converting to a set does not preserve the original list ordering as a set concept.

---

# 20. Set Membership

Sets are designed for efficient membership checking.

```python
allowed_users = {"alice", "bob", "charlie"}

if "bob" in allowed_users:
    print("Allowed")
```

This is one of the most common reasons to use a set instead of a list.

---

# 21. Set Methods

### `add()`

```python
numbers.add(10)
```

### `remove()`

```python
numbers.remove(10)
```

Raises an error if the value does not exist.

### `discard()`

```python
numbers.discard(10)
```

Does nothing if the value does not exist.

---

# 22. Set Operations

Given:

```python
a = {1, 2, 3}
b = {3, 4, 5}
```

## Union

All values from both sets:

```python
a | b
```

Result:

```python
{1, 2, 3, 4, 5}
```

---

## Intersection

Values present in both:

```python
a & b
```

Result:

```python
{3}
```

---

## Difference

Values in `a` but not in `b`:

```python
a - b
```

Result:

```python
{1, 2}
```

---

## Symmetric Difference

Values present in either set but not both:

```python
a ^ b
```

Result:

```python
{1, 2, 4, 5}
```

---

# 23. Dictionaries

A dictionary stores data as key-value pairs.

```python
student = {
    "name": "Sam",
    "age": 24,
    "marks": 90
}
```

The structure is:

```text
key   → value
```

For example:

```text
"name"  → "Sam"
"age"   → 24
"marks" → 90
```

Dictionary keys must be unique.

---

# 24. Accessing Dictionary Values

Values can be accessed using their keys:

```python
student["name"]
```

Result:

```text
"Sam"
```

Another example:

```python
student["marks"]
```

Result:

```text
90
```

---

# 25. Adding and Updating Dictionary Values

Assigning to an existing key updates its value:

```python
student["marks"] = 95
```

Assigning to a new key adds a new entry:

```python
student["city"] = "Delhi"
```

---

# 26. `get()`

Direct access:

```python
student["email"]
```

raises a `KeyError` if the key doesn't exist.

When a key may not exist, use:

```python
student.get("email")
```

which returns:

```text
None
```

You can also provide a default:

```python
student.get("email", "Not Available")
```

Result:

```text
"Not Available"
```

Use `.get()` when a missing key is an expected possibility.

---

# 27. Checking Dictionary Keys

The `in` operator checks dictionary keys.

```python
if "name" in student:
    print("Name exists")
```

Important:

```python
"name" in student
```

checks keys, not values.

---

# 28. Dictionary Views

Python provides:

```python
student.keys()
student.values()
student.items()
```

### Keys

```python
student.keys()
```

### Values

```python
student.values()
```

### Key-value pairs

```python
student.items()
```

---

# 29. Iterating Over Dictionaries

Iterating directly over a dictionary gives its keys:

```python
for key in student:
    print(key)
```

For values:

```python
for value in student.values():
    print(value)
```

For both keys and values:

```python
for key, value in student.items():
    print(key, value)
```

The `items()` pattern is extremely common in Python codebases.

---

# 30. Nested Collections

Real-world Python programs frequently combine multiple data structures.

For example:

```python
student = {
    "name": "Sam",
    "marks": [80, 90, 85],
    "skills": {"Python", "Java"},
    "address": {
        "city": "Delhi",
        "country": "India"
    }
}
```

This structure contains:

```text
dict
 ├── string
 ├── list
 ├── set
 └── dict
```

When reading complex Python code, break the structure down one layer at a time.

---

# 31. List of Dictionaries

A very common Python pattern is a list containing dictionaries.

```python
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 92},
    {"name": "Charlie", "marks": 78}
]
```

Accessing data:

```python
students[0]["name"]
```

Result:

```text
"Alice"
```

Iterating:

```python
for student in students:
    print(student["name"], student["marks"])
```

This pattern appears frequently in:

- API responses
- JSON data
- database results
- configuration
- data processing

---

# 32. Nested Lists

Lists can contain other lists.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Accessing an element:

```python
matrix[0][1]
```

Result:

```text
2
```

Think of this as:

```text
matrix
   ↓
 list
 ├── list
 ├── list
 └── list
```

Nested lists are an important concept before learning NumPy arrays.

---

# 33. Shallow Copy

A normal `.copy()` creates a shallow copy.

Consider:

```python
a = [
    [1, 2],
    [3, 4]
]

b = a.copy()
```

The outer list is copied, but the inner lists are still shared.

Conceptually:

```text
a ─────► outer list
           │
           ├──► [1, 2]
           │
           └──► [3, 4]

b ─────► another outer list
           │
           ├──► [1, 2]
           │
           └──► [3, 4]
```

Therefore:

```python
b[0].append(99)
```

also affects the inner list visible through `a`.

This is called a **shallow copy**.

Deep copying is a separate concept that will become useful when working with more complex nested objects.

---

# 34. List Comprehensions — Introduction

Python provides a compact syntax for creating lists.

Traditional approach:

```python
numbers = []

for i in range(5):
    numbers.append(i * 2)
```

Equivalent list comprehension:

```python
numbers = [i * 2 for i in range(5)]
```

Result:

```python
[0, 2, 4, 6, 8]
```

General form:

```python
[expression for item in iterable]
```

List comprehensions are powerful, but they should remain readable.

More advanced comprehensions will be covered later.

---

# 35. Python Collections vs Java Collections

Coming from Java, the following comparisons are useful:

| Python | Rough Java Equivalent |
|---|---|
| `list` | `ArrayList` |
| `tuple` | No exact direct equivalent |
| `set` | `HashSet` |
| `dict` | `HashMap` |
| `append()` | `add()` |
| `len(collection)` | `size()` |
| `x in collection` | `contains(x)` |
| `dict[key]` | `map.get(key)` |
| `for x in collection` | Enhanced `for` loop |

These are conceptual comparisons, not exact equivalents.

Python's object model, mutability rules, iteration model, and syntax are different from Java.

The goal is eventually to **think in Python**, rather than translating Java code into Python syntax.

---

# 36. Mutability

Mutability is an important Python concept.

### Mutable objects

Can be changed after creation.

Examples:

```text
list
set
dict
```

### Immutable objects

Cannot be changed after creation.

Examples:

```text
tuple
str
int
float
bool
```

For example:

```python
numbers = [1, 2, 3]
numbers.append(4)
```

works because lists are mutable.

But:

```python
coordinates = (10, 20)
coordinates[0] = 50
```

does not work because tuples are immutable.

---

# 37. Common Collection Mistakes

## Mistake 1 — Confusing `append()` and `extend()`

```python
numbers.append([4, 5])
```

adds one element:

```python
[1, 2, 3, [4, 5]]
```

Whereas:

```python
numbers.extend([4, 5])
```

adds two elements:

```python
[1, 2, 3, 4, 5]
```

---

## Mistake 2 — Confusing `remove()` and `pop()`

```python
numbers.remove(2)
```

means:

> Remove the value `2`.

Whereas:

```python
numbers.pop(2)
```

means:

> Remove the element at index `2`.

---

## Mistake 3 — Assuming assignment creates a copy

```python
b = a
```

does not create a new collection.

It creates another reference to the same object.

---

## Mistake 4 — Forgetting that dictionary keys may not exist

This:

```python
data["email"]
```

can raise:

```text
KeyError
```

when `"email"` is missing.

Depending on the situation:

```python
data.get("email")
```

may be more appropriate.

---

## Mistake 5 — Modifying a collection while iterating

Code such as:

```python
for item in numbers:
    if item < 0:
        numbers.remove(item)
```

can cause unexpected behavior, including skipped elements.

Prefer creating a new collection or using a safer filtering approach when appropriate.

---

# 38. Collection Selection Guide

A simple decision guide:

```text
Need key → value?
       │
      Yes
       ↓
     dict

       No
       │
       ↓
Need unique values?
       │
      Yes
       ↓
      set

       No
       │
       ↓
Need the collection to be immutable?
       │
      Yes
       ↓
     tuple

       No
       │
       ↓
      list
```

This is a simplified guide. Real applications may have additional requirements.

---

# 39. Code Reading: What to Look For

When reading unfamiliar Python code, don't just look at the values.

Ask:

### For lists

- Is order important?
- Is the list being modified?
- Are duplicates expected?
- Is indexing being used?
- Is membership checking frequent?

### For tuples

- Why is the data immutable?
- Is it representing a fixed group?
- Is unpacking being used?

### For sets

- Is uniqueness important?
- Is ordering irrelevant?
- Is membership checking frequent?

### For dictionaries

- What do the keys represent?
- What do the values represent?
- Can a key be missing?
- Should `.get()` be used?
- Is the dictionary nested?

### For all collections

Ask:

> Who owns this object?

> Is this object being mutated?

> Are two variables referring to the same object?

> Is a copy required?

These questions are particularly important during debugging and code review.

---

# 40. Data Structure and Performance

Data structures are not only about storing data.

They also affect performance.

For example:

```python
users = ["alice", "bob", "charlie"]
```

Checking:

```python
"bob" in users
```

may require scanning through the list.

If the main requirement is membership checking:

```python
users = {"alice", "bob", "charlie"}
```

a set is generally more appropriate because sets are designed for efficient membership operations.

The important lesson is:

> Choose a data structure based on the operations your program performs.

You don't need to memorize every Big-O complexity at this stage. Focus first on understanding why different structures exist.

---

# 41. Important Mental Models

### List

```text
ordered + mutable + duplicates
```

### Tuple

```text
ordered + immutable + duplicates
```

### Set

```text
unique values + membership
```

### Dictionary

```text
key → value
```

### Assignment

```text
a = b
↓
another reference to the same object
```

### Copy

```text
a.copy()
↓
new outer collection
```

### Equality

```text
a == b
↓
same value?
```

### Identity

```text
a is b
↓
same object?
```

---

# 42. Chapter Summary

Python's four core collection types solve different problems:

```text
list
    ↓
Ordered, mutable collection

tuple
    ↓
Ordered, immutable collection

set
    ↓
Unique values and membership

dict
    ↓
Key-value relationships
```

The most important concepts from this chapter are:

- indexing
- slicing
- mutation
- iteration
- `enumerate()`
- sorting
- references
- aliasing
- copying
- shallow copying
- mutability
- tuple unpacking
- set operations
- dictionary operations
- nested collections
- choosing the right data structure

---

# 43. Chapter 4 — Quick Reference

## List

```python
numbers = [1, 2, 3]

numbers.append(4)
numbers.insert(0, 0)
numbers.remove(2)
numbers.pop()
numbers.sort()

len(numbers)
2 in numbers
```

---

## Tuple

```python
point = (10, 20)

x, y = point
```

---

## Set

```python
numbers = {1, 2, 3}

numbers.add(4)
numbers.remove(2)

a | b
a & b
a - b
a ^ b
```

---

## Dictionary

```python
student = {
    "name": "Sam",
    "marks": 90
}

student["name"]
student["marks"] = 95
student["city"] = "Delhi"

student.get("email")
student.keys()
student.values()
student.items()
```

---

## Identity vs Equality

```python
a == b    # same value?
a is b    # same object?
```

---

## Copy

```python
b = a.copy()
```

Remember that `.copy()` performs a **shallow copy** for nested collections.

---

# 44. What Comes Next?

After becoming comfortable with Python's core data structures, the next step is to learn how to organize reusable logic with:

- functions
- parameters
- return values
- scopes
- arguments
- `*args`
- `**kwargs`
- lambda functions
- comprehensions in more depth

These concepts will make the collection knowledge from this chapter much more useful in real Python programs.
