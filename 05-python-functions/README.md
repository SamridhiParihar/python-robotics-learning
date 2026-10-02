# Chapter 5 — Python Functions

Functions are one of the fundamental building blocks of Python programs.

They allow us to:

- organize logic
- avoid repetition
- reuse code
- divide large problems into smaller pieces
- control dependencies
- make code easier to test and maintain

A good understanding of functions is essential for reading and reviewing real Python codebases.

---

# 1. What Is a Function?

A function is a reusable block of code that performs a specific task.

For example:

```python
def greet():
    print("Hello")
```

The function can then be called:

```python
greet()
```

Output:

```text
Hello
```

Instead of writing the same logic repeatedly, we define it once and call it whenever required.

---

# 2. Defining vs Calling a Function

These are two different operations.

## Defining a Function

```python
def greet():
    print("Hello")
```

This tells Python to create a function called `greet`.

The function does not execute yet.

## Calling a Function

```python
greet()
```

This executes the function.

Mental model:

```text
Function definition
        ↓
Create reusable logic
        ↓
Function call
        ↓
Execute the logic
```

---

# 3. Anatomy of a Function

Consider:

```python
def calculate_area(length, width):
    return length * width
```

The different parts are:

```text
def
 ↓
Function definition keyword

calculate_area
 ↓
Function name

length, width
 ↓
Parameters

:
 ↓
Start of function body

return length * width
 ↓
Function logic + return value
```

---

# 4. Parameters and Arguments

These terms are related but different.

```python
def greet(name):
    print("Hello", name)
```

Here:

```text
name
```

is a **parameter**.

When we call:

```python
greet("Sam")
```

`"Sam"` is an **argument**.

### Mental model

```text
Parameter
    ↓
Variable defined by the function

Argument
    ↓
Actual value supplied to the function
```

---

# 5. Multiple Parameters

A function can accept multiple parameters:

```python
def add(a, b):
    return a + b
```

Calling:

```python
result = add(10, 20)
```

produces:

```text
30
```

The arguments are assigned according to their position unless keyword arguments are used.

---

# 6. Return Values

The `return` statement sends a value back to the caller.

```python
def add(a, b):
    return a + b
```

Then:

```python
result = add(10, 20)

print(result)
```

Output:

```text
30
```

Think of a function as:

```text
Arguments
    ↓
┌─────────────────┐
│     Function    │
│                 │
│      Logic      │
└─────────────────┘
    ↓
Return value
```

---

# 7. `print()` vs `return`

This distinction is extremely important.

## `print()`

Displays something.

```python
def add(a, b):
    print(a + b)
```

The result is displayed, but it is not returned to the caller.

Therefore:

```python
result = add(10, 20)

print(result)
```

prints:

```text
30
None
```

---

## `return`

Returns the value to the caller:

```python
def add(a, b):
    return a + b
```

Now:

```python
result = add(10, 20)
```

means `result` contains `30`.

### Mental model

```text
print()
    ↓
Display something

return
    ↓
Give something back to the caller
```

Reusable functions generally benefit more from returning values than directly printing them.

---

# 8. A Function Without `return`

If a function does not explicitly return a value:

```python
def greet():
    print("Hello")
```

then:

```python
result = greet()
```

makes:

```python
result is None
```

Python implicitly returns `None`.

---

# 9. `return` Ends Function Execution

Once Python executes `return`, the function exits.

```python
def test():
    print("A")
    return
    print("B")
```

Calling:

```python
test()
```

produces:

```text
A
```

`"B"` is never executed.

This is useful for early exits:

```python
def process(value):
    if value is None:
        return

    # continue processing
```

---

# 10. Functions Can Return Any Object

A function can return any Python object.

For example:

### Integer

```python
def get_age():
    return 24
```

### String

```python
def get_name():
    return "Sam"
```

### List

```python
def get_numbers():
    return [1, 2, 3]
```

### Dictionary

```python
def get_user():
    return {
        "name": "Sam",
        "age": 24
    }
```

Python functions are not restricted to returning primitive values.

---

# 11. Returning Multiple Values

Python allows:

```python
def get_coordinates():
    return 10, 20
```

This actually returns a tuple:

```python
(10, 20)
```

It can be unpacked:

```python
x, y = get_coordinates()
```

This is a common Python idiom.

---

# 12. Type Hints

Python supports type annotations.

```python
def add(a: int, b: int) -> int:
    return a + b
```

This communicates that:

```text
a → expected int
b → expected int
return value → expected int
```

Type hints improve:

- readability
- IDE support
- documentation
- static analysis
- maintainability

However, Python does not normally enforce these annotations at runtime.

For example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

does not itself prevent someone from passing values of another type.

---

# 13. Default Arguments

Functions can define default values.

```python
def greet(name="Guest"):
    print("Hello", name)
```

Now both work:

```python
greet()
```

and:

```python
greet("Sam")
```

The default value is used only when the argument is omitted.

---

# 14. Positional Arguments

Consider:

```python
def introduce(name, age):
    print(name, age)
```

Calling:

```python
introduce("Sam", 24)
```

assigns:

```text
name → "Sam"
age  → 24
```

The arguments are matched according to their position.

---

# 15. Keyword Arguments

Python also allows arguments to be passed by parameter name:

```python
introduce(name="Sam", age=24)
```

The order can be changed:

```python
introduce(age=24, name="Sam")
```

Keyword arguments can make function calls easier to understand, especially when there are several parameters.

---

# 16. Positional + Keyword Arguments

Python allows positional arguments followed by keyword arguments.

For example:

```python
def create_user(name, age, city):
    ...
```

This is valid:

```python
create_user("Sam", age=24, city="Delhi")
```

But positional arguments should not appear after a keyword argument.

Understanding argument ordering becomes important when reading more complex APIs and framework code.

---

# 17. Scope

Scope determines where a variable can be accessed.

Consider:

```python
def calculate():
    result = 100
    print(result)
```

`result` is local to the function.

This works:

```python
calculate()
```

But:

```python
print(result)
```

outside the function does not work because `result` does not exist in that scope.

---

# 18. Local Variables

Variables created inside a function are normally local to that function.

```python
def calculate():
    result = 10 + 20
    return result
```

`result` is local to `calculate()`.

This allows different functions to have variables with the same name without necessarily interfering with each other.

---

# 19. Global Variables

A variable defined outside a function belongs to the surrounding/global scope.

```python
message = "Hello"

def show_message():
    print(message)
```

The function can read `message`.

However, relying heavily on global mutable state can make code harder to:

- understand
- test
- debug
- reuse

Prefer passing dependencies explicitly when practical.

---

# 20. Explicit vs Hidden Dependencies

Consider:

```python
config = {
    "mode": "fast"
}

def process():
    print(config["mode"])
```

`process()` depends on the global `config`.

The dependency is hidden.

Compare:

```python
def process(config):
    print(config["mode"])
```

Now the dependency is explicit.

This is generally easier to understand and test.

### Code-review question

When reading a function, ask:

> What does this function depend on outside its parameters?

---

# 21. Functions Should Have Clear Responsibilities

A function should generally have one clear responsibility.

Avoid functions such as:

```python
def process_everything():
    # validate user
    # save user
    # send email
    # calculate analytics
    # generate report
```

Instead, separate responsibilities:

```python
def validate_user():
    ...

def save_user():
    ...

def send_email():
    ...

def generate_report():
    ...
```

Benefits include:

- easier testing
- easier debugging
- better readability
- better reuse
- easier maintenance

This idea is closely related to the **Single Responsibility Principle**.

---

# 22. Functions Calling Functions

Functions can use other functions.

```python
def calculate_tax(price):
    return price * 0.18


def calculate_total(price):
    tax = calculate_tax(price)
    return price + tax
```

The call flow becomes:

```text
calculate_total()
        ↓
calculate_tax()
        ↓
return tax
        ↓
calculate_total()
        ↓
return total
```

Large applications are built from many functions calling other functions.

---

# 23. Function Call Stack

When functions call other functions, Python maintains a call stack.

For:

```python
def a():
    b()

def b():
    c()

def c():
    print("Hello")

a()
```

The execution conceptually looks like:

```text
a()
 ↓
b()
 ↓
c()
 ↓
print()
```

When `c()` finishes:

```text
c() removed
 ↓
b() continues
 ↓
b() removed
 ↓
a() continues
```

This becomes useful when understanding Python stack traces and debugging errors.

---

# 24. Functions Are Objects

In Python, functions are objects.

Therefore:

```python
def greet():
    print("Hello")
```

You can assign the function to another variable:

```python
say_hello = greet
```

Then:

```python
say_hello()
```

works.

Both names refer to the same function object.

This is a fundamental feature of Python.

---

# 25. Passing Functions as Arguments

Because functions are objects, they can be passed to other functions.

```python
def add(a, b):
    return a + b


def execute(operation, a, b):
    return operation(a, b)
```

Now:

```python
result = execute(add, 10, 20)
```

The function `add` is passed as an argument.

This idea is called using a **higher-order function**.

It becomes important for:

- callbacks
- decorators
- functional programming
- frameworks
- data processing

---

# 26. Lambda Functions

A lambda is a small anonymous function.

For example:

```python
square = lambda x: x * x
```

Equivalent normal function:

```python
def square(x):
    return x * x
```

Calling:

```python
square(5)
```

returns:

```text
25
```

Lambda functions are useful for short expressions.

However, if the logic becomes complicated, a normal named function is usually more readable.

---

# 27. `*args`

`*args` allows a function to accept an arbitrary number of positional arguments.

```python
def add_all(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

Calls:

```python
add_all(1, 2)
add_all(1, 2, 3)
add_all(1, 2, 3, 4, 5)
```

Inside the function, `numbers` is a tuple.

Conceptually:

```text
add_all(1, 2, 3)
        ↓
numbers = (1, 2, 3)
```

The name `args` is only a convention. The `*` is what matters.

For example:

```python
def add_all(*values):
    ...
```

works exactly the same way.

---

# 28. `**kwargs`

`**kwargs` allows a function to accept an arbitrary number of keyword arguments.

```python
def create_profile(**details):
    return details
```

Calling:

```python
create_profile(
    name="Sam",
    age=24,
    city="Delhi"
)
```

creates a dictionary inside the function:

```python
{
    "name": "Sam",
    "age": 24,
    "city": "Delhi"
}
```

Mental model:

```text
*args
   ↓
tuple of positional arguments

**kwargs
   ↓
dictionary of keyword arguments
```

Again, `kwargs` is only a conventional name.

---

# 29. Combining Parameters

Python allows functions such as:

```python
def example(name, *args, **kwargs):
    ...
```

Here:

```text
name
 ↓
normal parameter

*args
 ↓
additional positional arguments

**kwargs
 ↓
additional keyword arguments
```

The exact ordering rules become important when designing flexible APIs.

---

# 30. Mutable Arguments

Consider:

```python
def add_number(numbers):
    numbers.append(10)
```

Then:

```python
numbers = [1, 2, 3]

add_number(numbers)

print(numbers)
```

The original list becomes:

```python
[1, 2, 3, 10]
```

Why?

Because the function received a reference to the same list object.

Python's parameter passing is best understood as:

> Python passes object references by assignment.

The important practical point is:

> A function can mutate a mutable object passed to it.

---

# 31. Mutation vs Returning a New Object

Consider:

```python
def add_number(numbers):
    numbers.append(10)
```

This modifies the original object.

Alternatively:

```python
def add_number(numbers):
    result = numbers.copy()
    result.append(10)
    return result
```

Now the original list remains unchanged.

This distinction is important when designing APIs and reviewing code.

---

# 32. Side Effects

A function has a **side effect** when it changes something outside its local calculation.

Examples:

```python
database.save(user)
```

```python
file.write(data)
```

```python
global_list.append(item)
```

```python
send_email(...)
```

A simple function such as:

```python
def add(a, b):
    return a + b
```

has no obvious external side effect.

When reviewing a function, ask:

> Does this function only calculate something, or does it also change external state?

---

# 33. Pure Functions

A pure function generally:

- depends only on its inputs
- returns a result
- does not modify external state

Example:

```python
def square(x):
    return x * x
```

For the same input:

```python
square(5)
```

will consistently produce:

```text
25
```

Pure functions are generally easier to:

- test
- reason about
- reuse
- debug

Not every function in an application can or should be pure, but understanding the distinction is valuable.

---

# 34. Mutable Default Arguments

One of Python's classic pitfalls is using a mutable object as a default argument.

Avoid:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

The default list is created once and reused across calls.

This can lead to surprising behavior.

Instead:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

Now a new list is created when no list is supplied.

### Code-review rule

Be suspicious of:

```python
def function(items=[]):
```

or:

```python
def function(data={}):
```

or other mutable defaults.

Prefer:

```python
def function(items=None):
```

and initialize inside the function when necessary.

---

# 35. Docstrings

A docstring documents what a function does.

```python
def calculate_area(length, width):
    """Return the area of a rectangle."""
    return length * width
```

Docstrings are useful for:

- developers reading the code
- IDE documentation
- generated documentation
- future maintenance

They can be accessed through:

```python
calculate_area.__doc__
```

---

# 36. Type Hints + Docstrings

Production Python code often combines type hints and documentation:

```python
def calculate_area(length: float, width: float) -> float:
    """Return the area of a rectangle."""
    return length * width
```

A reader can immediately understand:

```text
Function:
    calculate_area

Inputs:
    length → float
    width  → float

Output:
    float
```

This is especially useful in large codebases.

---

# 37. Function Naming

Python functions normally use `snake_case`.

Good:

```python
calculate_total()
get_user()
process_payment()
load_model()
generate_report()
```

Avoid Java-style naming:

```python
calculateTotal()
getUser()
processPayment()
```

Common Python naming conventions:

```text
functions → snake_case

classes → PascalCase

constants → UPPER_CASE
```

---

# 38. Functions and Error Handling

Functions often validate their inputs.

Example:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero")

    return a / b
```

Calling:

```python
divide(10, 2)
```

works.

Calling:

```python
divide(10, 0)
```

raises an exception.

Exception handling will be studied separately, but functions are often where invalid inputs are detected and handled.

---

# 39. Function Design Principles

A well-designed function generally has:

### 1. A clear name

```python
calculate_average()
```

is better than:

```python
process()
```

when the function specifically calculates an average.

### 2. A clear responsibility

One function should not perform unrelated tasks.

### 3. Understandable parameters

Avoid unnecessarily large parameter lists.

### 4. A predictable return value

The caller should understand what the function gives back.

### 5. Controlled side effects

External changes should be intentional and understandable.

### 6. Appropriate type hints

Type hints can communicate the expected interface.

### 7. Useful documentation

Use docstrings when the behavior needs explanation.

---

# 40. Reading Functions in an Existing Codebase

When you encounter an unfamiliar function, first inspect its interface before reading every line.

For example:

```python
def create_user(
    name: str,
    age: int,
    repository,
    send_email: bool = True
) -> dict:
    ...
```

Before reading the body, you already know:

```text
Function:
    create_user

Parameters:
    name
    age
    repository
    send_email

Optional parameter:
    send_email = True

Return:
    dict
```

Then inspect the implementation.

---

# 41. Function Code-Reading Checklist

When reading a function, ask:

### Interface

- What is the function called?
- What parameters does it accept?
- Which parameters have defaults?
- Are type hints present?
- What does it return?

### Behavior

- What does the function actually do?
- Does it call other functions?
- Are there branches or loops?
- What happens for invalid input?

### State

- Does it modify arguments?
- Does it modify global state?
- Does it modify external resources?

### Dependencies

- Does it depend on a database?
- Does it depend on a file?
- Does it depend on configuration?
- Does it depend on global variables?

### Error behavior

- Can it raise exceptions?
- Are errors handled inside the function or passed to the caller?

This process helps you understand unfamiliar Python code much faster.

---

# 42. Function Code-Review Checklist

When reviewing a function, consider:

```text
Responsibility
    ↓
Does it do one clear thing?

Naming
    ↓
Does the name describe its behavior?

Parameters
    ↓
Are they necessary and understandable?

Return value
    ↓
Is the output clear?

Side effects
    ↓
Does it modify external state?

Mutability
    ↓
Can input collections be modified?

Defaults
    ↓
Are mutable defaults avoided?

Dependencies
    ↓
Are important dependencies explicit?

Error handling
    ↓
Are invalid inputs handled appropriately?

Type hints
    ↓
Would they improve readability?

Complexity
    ↓
Is the function becoming too large?
```

---

# 43. Python vs Java

Coming from Java, functions require a small mental shift.

### Java

Methods normally belong to classes:

```java
class Calculator {

    int add(int a, int b) {
        return a + b;
    }
}
```

### Python

Functions can exist independently:

```python
def add(a, b):
    return a + b
```

Python functions can also be:

- stored in variables
- passed as arguments
- returned from functions

This makes functions first-class objects.

---

# 44. Java → Python Mental Model

| Concept | Java | Python |
|---|---|---|
| Function/method | Usually method inside class | Functions can exist independently |
| Parameters | Statically typed | Dynamically typed, optional annotations |
| Return type | Usually declared | Optional annotation |
| Default arguments | Not built into method parameters | Supported |
| Keyword arguments | Not directly equivalent | Supported |
| Variable arguments | `...` varargs | `*args` |
| Keyword variable arguments | No direct equivalent | `**kwargs` |
| Lambda | Lambda expressions | Lambda functions |
| Function as value | More restricted syntax/model | First-class function objects |

The goal is not to translate every Java concept directly.

The goal is to understand Python's own programming model.

---

# 45. Core Mental Model

A useful function model is:

```text
                 Arguments
                     ↓
             ┌───────────────┐
             │               │
             │   FUNCTION    │
             │               │
             │    Logic      │
             │               │
             └───────────────┘
                     │
                     ↓
               Return value
```

But a function can also interact with the outside world:

```text
                 ┌───────────────┐
                 │   FUNCTION    │
                 └───────────────┘
                    ↑     ↓
                    │     │
              dependencies
                    │     │
             side effects
```

Therefore, when reading a function, always think about both:

```text
Input → Logic → Output
```

and:

```text
What does this function change outside itself?
```

---

# 46. Chapter 5 Summary

The major concepts covered in this chapter are:

```text
Functions
   │
   ├── Definition
   ├── Calling
   ├── Parameters
   ├── Arguments
   ├── Return values
   ├── Default arguments
   ├── Positional arguments
   ├── Keyword arguments
   │
   ├── Scope
   │   ├── Local
   │   └── Global
   │
   ├── Type hints
   ├── Docstrings
   │
   ├── *args
   ├── **kwargs
   │
   ├── Functions as objects
   ├── Higher-order functions
   ├── Lambda
   │
   ├── Mutable arguments
   ├── Side effects
   ├── Pure functions
   └── Mutable default argument pitfall
```

---

# 47. Quick Reference

## Basic Function

```python
def greet():
    print("Hello")
```

## Parameters

```python
def greet(name):
    print(f"Hello {name}")
```

## Return

```python
def add(a, b):
    return a + b
```

## Default Parameter

```python
def greet(name="Guest"):
    print(name)
```

## Keyword Arguments

```python
greet(name="Sam")
```

## Type Hints

```python
def add(a: int, b: int) -> int:
    return a + b
```

## `*args`

```python
def add_all(*numbers):
    ...
```

`numbers` is a tuple.

## `**kwargs`

```python
def create_user(**details):
    ...
```

`details` is a dictionary.

## Function as an Object

```python
def square(x):
    return x * x

operation = square
```

## Passing a Function

```python
def execute(operation, value):
    return operation(value)
```

## Lambda

```python
square = lambda x: x * x
```

## Safe Mutable Default

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

---

# 48. Chapter 5 Completion Criteria

Before moving to the next chapter, you should be able to:

- [ ] Define and call functions.
- [ ] Explain parameters vs arguments.
- [ ] Use positional arguments.
- [ ] Use keyword arguments.
- [ ] Use default arguments.
- [ ] Understand `return`.
- [ ] Explain `print()` vs `return`.
- [ ] Return multiple values.
- [ ] Use type hints.
- [ ] Write useful docstrings.
- [ ] Understand local and global scope.
- [ ] Understand function dependencies.
- [ ] Pass lists and dictionaries to functions.
- [ ] Understand mutation and side effects.
- [ ] Use `*args`.
- [ ] Use `**kwargs`.
- [ ] Understand functions as objects.
- [ ] Pass functions as arguments.
- [ ] Understand basic lambda functions.
- [ ] Identify the mutable default argument problem.
- [ ] Design functions with clear responsibilities.
- [ ] Read unfamiliar functions.
- [ ] Review functions for correctness, readability, dependencies, and side effects.

---

# 49. Key Takeaways

The most important ideas from this chapter are not syntax.

Remember these:

```text
1. Functions package reusable logic.

2. Parameters describe what a function accepts.

3. Arguments are the actual values supplied.

4. return gives a value back to the caller.

5. print() only displays something.

6. Functions can return any Python object.

7. Python functions are first-class objects.

8. *args collects positional arguments into a tuple.

9. **kwargs collects keyword arguments into a dictionary.

10. Mutable objects can be modified inside functions.

11. External state creates side effects.

12. Global state creates hidden dependencies.

13. Mutable default arguments can create subtle bugs.

14. Good functions have clear responsibilities.

15. When reading code, understand the function interface before its implementation.
```

---

# 50. What Comes Next?

With functions and core collections understood, the next major step is to learn how Python handles **errors and exceptions**.

This will cover concepts such as:

- exceptions
- `try`
- `except`
- `else`
- `finally`
- `raise`
- custom exceptions
- exception propagation
- debugging
- writing robust Python programs

These concepts will build directly on the functions you've learned in this chapter.
