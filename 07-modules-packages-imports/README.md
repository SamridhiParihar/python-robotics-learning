# Chapter 7 — Python Modules, Packages & Imports

Python programs are rarely written as a single file.

As applications grow, code is divided into:

- modules
- packages
- subpackages
- functions
- classes

Python's import system connects these pieces.

This chapter focuses on understanding **how Python organizes code and how modules communicate with each other**.

The goal is not just to know import syntax.

The goal is to be able to open an unfamiliar Python repository and understand:

> **What is this module, where did this object come from, and how are the different parts of this project connected?**

---

# 1. Module

A Python file is a module.

For example:

```text
calculator.py
```

can be imported by another Python file.

```python
# calculator.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

Another file:

```python
import calculator

print(calculator.add(10, 20))
```

Mental model:

```text
calculator.py
     │
     │ import
     ▼
another_module.py
     │
     ▼
calculator.add()
```

A module can contain:

- functions
- classes
- variables
- constants
- imports
- executable module-level code

---

# 2. Why Modules Exist

Putting an entire application into one file quickly becomes difficult to maintain.

Instead of:

```text
main.py
└── 5000 lines
```

we can separate responsibilities:

```text
project/
├── users.py
├── authentication.py
├── database.py
├── validation.py
└── configuration.py
```

Each module can have a focused responsibility.

This improves:

- readability
- maintainability
- testing
- reuse
- separation of concerns
- dependency management

---

# 3. `import module`

The most basic import form is:

```python
import calculator
```

Access objects through the module:

```python
calculator.add(10, 20)
calculator.subtract(20, 5)
```

The mental model is:

```text
calculator
    │
    ├── add
    ├── subtract
    └── multiply
```

This form makes the origin of the object explicit.

---

# 4. `from module import object`

You can import specific objects:

```python
from calculator import add

result = add(10, 20)
```

Multiple objects:

```python
from calculator import add, subtract
```

Now the functions are available directly in the current namespace.

Compare:

```python
import calculator

calculator.add(10, 20)
```

with:

```python
from calculator import add

add(10, 20)
```

The first makes the source explicit.

The second is shorter.

When reading unfamiliar code, always ask:

> **Where did this name come from?**

---

# 5. Aliases with `as`

Modules can be given aliases.

```python
import calculator as calc

calc.add(10, 20)
```

Specific objects can also be aliased:

```python
from calculator import multiply as mul

mul(5, 6)
```

A very common real-world example is:

```python
import numpy as np
```

Then:

```python
np.array([1, 2, 3])
```

Aliases are particularly useful when:

- module names are long
- a conventional alias exists
- a name would otherwise conflict with something else

---

# 6. What Happens During Import?

`import` is not simply a textual copy-paste operation.

Conceptually:

```text
import calculator
       │
       ▼
Find module
       │
       ▼
Load module
       │
       ▼
Execute module-level code
       │
       ▼
Create/reuse module object
       │
       ▼
Bind module name
```

This means:

> **Importing a module can execute code.**

For example:

```python
# logger.py

print("Logger loaded")

def log(message):
    print(message)
```

Then:

```python
import logger
```

will print:

```text
Logger loaded
```

because the module-level statement executed during import.

---

# 7. Module-Level Code

Consider:

```python
x = 10

print("Module loaded")


def add(a, b):
    return a + b
```

When the module is imported:

```python
x = 10
print("Module loaded")
```

execute immediately.

The function body doesn't execute until the function is called.

```text
Import
  │
  ├── execute module-level statements
  │
  └── define functions/classes
```

This is important because unexpected module-level code can create **import side effects**.

---

# 8. Module Namespace

When Python imports a module:

```python
import calculator
```

`calculator` refers to a module object.

Conceptually:

```text
calculator
    │
    ├── add
    ├── subtract
    └── multiply
```

Therefore:

```python
calculator.add(...)
```

means:

> Access `add` from the `calculator` module namespace.

This namespace concept is fundamental when reading Python code.

---

# 9. The `__name__` Variable

Every Python module has a special variable:

```python
__name__
```

If a module is imported:

```python
import calculator
```

then inside `calculator.py`:

```python
print(__name__)
```

will generally produce:

```text
calculator
```

If the file is executed directly:

```bash
python calculator.py
```

then:

```python
print(__name__)
```

produces:

```text
__main__
```

Mental model:

```text
Imported:
    __name__ == "calculator"

Executed directly:
    __name__ == "__main__"
```

---

# 10. `if __name__ == "__main__"`

This is one of the most important Python patterns.

```python
def main():
    print("Application started")


if __name__ == "__main__":
    main()
```

When the file is run directly:

```bash
python application.py
```

the condition is true.

When the file is imported:

```python
import application
```

the condition is false.

Therefore:

```text
                 application.py
                       │
             ┌─────────┴─────────┐
             │                   │
       Run directly           Imported
             │                   │
      __name__ ==            __name__ ==
      "__main__"             "application"
             │                   │
             ▼                   ▼
       main() runs        main() doesn't run
```

---

# 11. Why the `__main__` Guard Matters

Without the guard:

```python
# robot.py

start_robot()
```

another file doing:

```python
import robot
```

would automatically start the robot.

That is an undesirable import side effect.

Instead:

```python
def start_robot():
    ...


if __name__ == "__main__":
    start_robot()
```

Now importing the module only defines the functionality.

The caller decides when to execute it.

This is especially important for:

- robotics
- database connections
- servers
- ML inference
- command-line applications
- scripts used as libraries

---

# 12. Packages

As projects grow, modules can be organized into packages.

Example:

```text
shop/
├── users.py
├── orders.py
└── payments.py
```

could evolve into:

```text
shop/
├── users/
│   └── ...
├── orders/
│   └── ...
└── payments/
    └── ...
```

Conceptually:

```text
Package
   │
   ├── Module
   ├── Module
   └── Module
```

Packages provide structure for related modules.

---

# 13. `__init__.py`

You will frequently see:

```text
my_package/
├── __init__.py
├── users.py
└── orders.py
```

`__init__.py` is a special module associated with the package.

Modern Python supports namespace packages, so `__init__.py` is not required in every possible package layout.

However, it remains extremely common in application and library code.

It can be used for:

- package initialization
- exposing selected objects
- defining package-level variables
- organizing the package API

---

# 14. Using `__init__.py` as a Package API

Suppose:

```text
utilities/
├── __init__.py
└── math_utils.py
```

`math_utils.py`:

```python
def square(number):
    return number * number
```

`__init__.py`:

```python
from .math_utils import square
```

Now callers can write:

```python
from utilities import square
```

instead of:

```python
from utilities.math_utils import square
```

The package is effectively exposing a simpler public interface.

---

# 15. Modules vs Packages

Keep the distinction clear.

### Module

Usually a Python file:

```text
user.py
```

### Package

A structured collection of Python modules:

```text
users/
├── __init__.py
├── user.py
└── validation.py
```

Mental model:

```text
Package
   │
   ├── Module
   ├── Module
   └── Module
```

---

# 16. Absolute Imports

An absolute import describes the path from the project's import root.

Example:

```python
from app.models.user import User
```

Conceptually:

```text
app
 └── models
      └── user.py
           └── User
```

Absolute imports make the source of the imported object explicit.

They are common in larger Python applications.

---

# 17. Relative Imports

Relative imports describe the location relative to the current package.

Example:

```python
from ..models.user import User
```

The dots represent package levels.

Conceptually:

```text
.   → current package
..  → parent package
```

Relative imports are useful within packages, but deeply nested relative imports can become difficult to follow.

---

# 18. Absolute vs Relative Imports

Compare:

```python
from app.models.user import User
```

with:

```python
from ..models.user import User
```

The first is explicit about the package path.

The second depends on the current module's location.

When reading relative imports, inspect the directory structure before trying to understand the import.

---

# 19. Import Search Path

Python needs to know where to search for modules.

The search locations are available through:

```python
import sys

print(sys.path)
```

Conceptually:

```text
import something
       ↓
Python checks import locations
       ↓
module found
       ↓
module loaded
```

If Python can't find the requested module, you may get:

```text
ModuleNotFoundError
```

---

# 20. `sys.path`

`sys.path` is a list of locations Python searches when resolving imports.

You can inspect it:

```python
import sys

for path in sys.path:
    print(path)
```

This is useful when debugging import problems.

However, manually modifying `sys.path` is generally not the preferred way to structure an application.

Prefer proper:

- package structure
- project configuration
- environment management
- installation
- module execution

---

# 21. `ModuleNotFoundError`

A common error is:

```text
ModuleNotFoundError: No module named 'something'
```

Don't immediately assume the file doesn't exist.

Possible causes include:

- incorrect import path
- incorrect project structure
- wrong working/execution context
- package not installed
- wrong Python environment
- incorrect `sys.path`
- typo in module name

A useful debugging sequence is:

```text
Does the file exist?
        ↓
Is the package structure correct?
        ↓
What Python environment is active?
        ↓
How is the application being executed?
        ↓
What does sys.path contain?
        ↓
Is the import path correct?
```

---

# 22. Standard Library, Third-Party, Local Imports

When reading a Python file, classify imports.

### Standard library

```python
import os
import sys
import json
from pathlib import Path
```

These come with Python.

### Third-party

```python
import numpy
import torch
import requests
```

These are external dependencies.

### Local project code

```python
from app.models.user import User
from app.services.user_service import UserService
```

These belong to the application itself.

This classification is an excellent first step when reading an unfamiliar Python file.

---

# 23. Import Caching

Python keeps imported modules in:

```python
sys.modules
```

Conceptually:

```text
First import
    ↓
Find module
    ↓
Execute module
    ↓
Store module
    ↓
sys.modules
```

Later:

```text
Another import
    ↓
Module already loaded
    ↓
Reuse existing module
```

For example:

```python
import counter
import counter
```

doesn't normally execute the module's top-level code from scratch twice within the same Python process.

---

# 24. `sys.modules`

You can inspect the loaded modules:

```python
import sys

print(sys.modules)
```

Or check for one specifically:

```python
print("numpy" in sys.modules)
```

This is useful for understanding import behavior and debugging.

---

# 25. Import Side Effects

Because module-level code executes during import, modules should generally avoid surprising side effects.

Potentially problematic:

```python
# database.py

print("Connecting...")

connection = connect_to_database()
```

Now:

```python
import database
```

automatically connects to the database.

A better design:

```python
def connect_to_database():
    ...
```

and let the caller explicitly decide when to connect.

Good modules generally make important side effects explicit.

---

# 26. Circular Imports

A circular import occurs when modules depend on each other.

Example:

```text
user.py
   ↓
order.py
   ↓
user.py
```

For example:

```python
# user.py
from order import Order
```

and:

```python
# order.py
from user import User
```

This creates:

```text
user ↔ order
```

and can result in import-time errors or partially initialized modules.

---

# 27. Fixing Circular Dependencies

Circular imports are often an architectural problem.

Instead of:

```text
A ↔ B
```

consider extracting shared functionality:

```text
       common
       /    \
      A      B
```

For example:

```text
common.py
user.py
order.py
```

Both `user.py` and `order.py` can depend on `common.py` without depending directly on each other.

The correct solution depends on what the modules actually need to share.

---

# 28. Avoid `from module import *`

You may encounter:

```python
from module import *
```

This imports many names into the current namespace.

It is generally discouraged in application code because it makes the source of names unclear.

Prefer:

```python
import module

module.function()
```

or explicit imports:

```python
from module import function
```

Explicit imports make code easier to trace.

---

# 29. Name Collisions

Consider:

```python
from module_a import process
from module_b import process
```

The second import replaces the name `process` from the first import.

This can be confusing.

Better:

```python
import module_a
import module_b

module_a.process()
module_b.process()
```

Or:

```python
from module_a import process as process_a
from module_b import process as process_b
```

---

# 30. `python file.py` vs `python -m`

These execution styles are related but not identical.

### Direct execution

```bash
python app/main.py
```

### Module execution

```bash
python -m app.main
```

Module execution treats the target as a module within the package/module system.

This can affect:

- import resolution
- package context
- relative imports
- `__name__`

When debugging import problems, always consider **how the program is being executed**.

---

# 31. `__main__.py`

A package can contain:

```text
package/
├── __init__.py
└── __main__.py
```

Then:

```bash
python -m package
```

can execute:

```text
package/__main__.py
```

This is useful for making a package executable.

---

# 32. Importing Classes

A module can contain classes.

```python
# user.py

class User:
    def __init__(self, name):
        self.name = name
```

Another module:

```python
from user import User

user = User("Sam")
```

Here:

```text
user
```

is the module.

```text
User
```

is the class defined inside that module.

This distinction is important when reading imports.

---

# 33. Constants in Modules

Modules can also expose constants:

```python
# config.py

MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30
```

Then:

```python
from config import MAX_RETRIES
```

or:

```python
import config

config.MAX_RETRIES
```

A common naming convention is uppercase names for constants.

---

# 34. Module Responsibility

Modules should generally group related functionality.

Good:

```text
authentication.py
```

for authentication-related logic.

```text
validation.py
```

for validation.

```text
database.py
```

for database access.

Be cautious with giant generic modules such as:

```text
utils.py
```

containing unrelated:

```text
database helpers
email helpers
math functions
authentication
robot control
random utilities
```

Such modules can become difficult to understand and create unnecessary dependencies.

---

# 35. Import Graphs

Imports form a dependency graph.

Consider:

```text
main
 │
 ├── controller
 │       │
 │       └── service
 │              │
 │              ├── repository
 │              └── model
 │
 └── configuration
```

This graph can often be reconstructed by reading imports.

This is one of the most useful skills for understanding an unfamiliar Python repository.

---

# 36. Backend Example

A backend might look like:

```text
backend/
│
├── app/
│   ├── main.py
│   │
│   ├── controllers/
│   │   └── user_controller.py
│   │
│   ├── services/
│   │   └── user_service.py
│   │
│   ├── repositories/
│   │   └── user_repository.py
│   │
│   └── models/
│       └── user.py
```

Imports might produce:

```text
Controller
    ↓
Service
    ↓
Repository
    ↓
Database

Service
    ↓
Model
```

For example:

```python
# user_controller.py

from app.services.user_service import create_user
```

and:

```python
# user_service.py

from app.repositories.user_repository import save_user
from app.models.user import User
```

The imports reveal the architecture.

---

# 37. Robotics Example

A robotics project could look like:

```text
robot/
│
├── main.py
│
├── sensors/
│   ├── camera.py
│   └── imu.py
│
├── perception/
│   ├── detector.py
│   └── tracking.py
│
├── planning/
│   └── planner.py
│
├── control/
│   └── controller.py
│
└── models/
    └── policy.py
```

The dependency flow could become:

```text
Camera
   ↓
Perception
   ↓
Planning
   ↓
Control
   ↓
Actuator
```

As you move toward ROS 2 and embodied AI, understanding this kind of module dependency graph will become increasingly important.

---

# 38. Code Reading Strategy

When opening an unfamiliar Python file, start at the imports.

For example:

```python
import os
import numpy as np
from pathlib import Path

from app.models.user import User
from app.services.user_service import UserService
```

Classify them:

```text
os / pathlib
    ↓
standard library

numpy
    ↓
third-party dependency

User / UserService
    ↓
local project code
```

Then follow the local imports.

For example:

```text
UserService
     ↓
user_service.py
     ↓
what does it import?
     ↓
follow those dependencies
```

This gradually reconstructs the codebase.

---

# 39. Import Debugging Checklist

When you encounter an import error:

### 1. Check the file

Does the module actually exist?

### 2. Check the package structure

Are the directories arranged correctly?

### 3. Check the import statement

Is the path/name correct?

### 4. Check the Python environment

For your Pixi workflow:

```bash
pixi run python ...
```

or:

```bash
pixi shell
```

### 5. Check the Python interpreter

```bash
which python
python --version
```

### 6. Check the import path

```python
import sys

print(sys.path)
```

### 7. Check execution mode

Compare:

```bash
python file.py
```

with:

```bash
python -m package.module
```

### 8. Check circular dependencies

Trace:

```text
A → B → C → A
```

---

# 40. Python vs Java

Your Java background provides useful intuition, but Python's model isn't identical.

| Java | Python |
|---|---|
| `.java` source file | `.py` module |
| package | package |
| `import` | `import` |
| class | class |
| package hierarchy | package/module hierarchy |
| Maven/Gradle dependency | Python package/dependency |
| Classpath | Python import/search path |
| `main()` | `if __name__ == "__main__"` pattern |
| `package com.example...` | package/directory structure |

One major difference:

A Python module does **not** need to contain a class.

This is completely normal:

```python
def add(a, b):
    return a + b
```

A module can simply expose functions.

---

# 41. Core Mental Model

The most important mental model from this chapter is:

```text
                  PYTHON PROJECT
                       │
              ┌────────┴────────┐
              │                 │
           Package           Package
              │
        ┌─────┴─────┐
        │           │
     Module       Module
        │
   ┌────┼────┐
   │    │    │
Functions Classes Constants
        │
        ▼
      IMPORT
        │
   ┌────┴─────┐
   │          │
Absolute   Relative
imports    imports
   │          │
   └────┬─────┘
        ↓
  module resolution
        ↓
     sys.path
        ↓
    sys.modules
        ↓
   loaded module
```

The key idea:

> **Imports create relationships between modules, and those relationships form part of the architecture of a Python application.**

---

# 42. Quick Reference

## Import a module

```python
import calculator
```

## Use module members

```python
calculator.add(1, 2)
```

## Import specific objects

```python
from calculator import add
```

## Alias

```python
import numpy as np
```

## Relative import

```python
from ..models.user import User
```

## Absolute import

```python
from app.models.user import User
```

## Main guard

```python
if __name__ == "__main__":
    main()
```

## Inspect import path

```python
import sys

print(sys.path)
```

## Inspect loaded modules

```python
import sys

print(sys.modules)
```

## Run a file

```bash
python file.py
```

## Run a module

```bash
python -m package.module
```

---

# 43. Code Review Checklist

When reviewing imports and package structure, check:

- [ ] Are imports explicit and understandable?
- [ ] Are standard-library, third-party, and local imports distinguishable?
- [ ] Are unnecessary imports avoided?
- [ ] Is `from module import *` avoided?
- [ ] Are aliases meaningful?
- [ ] Are there circular imports?
- [ ] Are module responsibilities clear?
- [ ] Are there unexpected import-time side effects?
- [ ] Is `__main__` used appropriately?
- [ ] Are relative imports understandable?
- [ ] Is the package structure logical?
- [ ] Are public package APIs intentionally exposed?
- [ ] Is `sys.path` being modified unnecessarily?
- [ ] Does execution mode affect imports?
- [ ] Are dependencies flowing in sensible directions?

---

# 44. Chapter Completion Criteria

You should now be able to:

- explain what a module is
- import modules
- import specific objects
- use aliases
- explain module namespaces
- explain `__name__`
- use `if __name__ == "__main__"`
- explain packages
- understand `__init__.py`
- expose package APIs
- use absolute imports
- use relative imports
- understand `sys.path`
- understand `sys.modules`
- diagnose basic `ModuleNotFoundError`
- identify circular imports
- identify import side effects
- understand `python file.py`
- understand `python -m module`
- distinguish standard-library, third-party, and local imports
- trace imports through a project
- understand how imports reveal application architecture

Most importantly:

> **You should be able to open a Python repository and start understanding its structure by following the imports.**

---

# 45. Key Takeaways

1. **A Python file is a module.**

2. **Packages organize related modules.**

3. **Imports connect modules and form dependency relationships.**

4. **Importing a module can execute its module-level code.**

5. **`__name__` tells you how a module is being executed.**

6. **`if __name__ == "__main__"` separates reusable code from direct execution.**

7. **`__init__.py` can initialize a package and expose a public API.**

8. **`sys.path` determines where Python searches for modules.**

9. **`sys.modules` stores modules that have already been loaded.**

10. **Circular imports are often symptoms of architectural dependency problems.**

11. **Unexpected import-time side effects make systems harder to reason about.**

12. **Imports are one of the best starting points for understanding an unfamiliar Python codebase.**

---

# Next Chapter

## Chapter 8 — Object-Oriented Programming in Python

The next chapter will connect Python's object model with the Java OOP concepts you already know.

We'll cover:

```text
Classes & Objects
       ↓
__init__
       ↓
Instance attributes
       ↓
Instance methods
       ↓
self
       ↓
Class attributes
       ↓
Class methods
       ↓
Static methods
       ↓
Encapsulation
       ↓
Inheritance
       ↓
Method overriding
       ↓
super()
       ↓
Composition
       ↓
Abstract base classes
       ↓
Protocols / duck typing
       ↓
Pythonic OOP design
       ↓
Code reading & review
```

This will be a particularly important chapter for you because **Python's OOP model looks familiar if you come from Java, but several Python concepts work differently enough that Java intuition can lead you into bad Python code.**
