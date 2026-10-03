# Chapter 6 — Python Exceptions & Error Handling

Exceptions are Python's mechanism for representing and handling situations where normal program execution cannot continue as expected.

This chapter covers how exceptions are:

- raised
- caught
- propagated
- translated
- re-raised
- customized
- used for validation and recovery
- handled at appropriate application layers

The goal is not simply to learn `try`/`except`, but to understand **how failures move through a Python program** and how to design error handling that does not hide bugs.

---

## 1. What Is an Exception?

An exception represents an abnormal situation during program execution.

```python
number = int("hello")
```

Python cannot convert `"hello"` into an integer, so it raises a `ValueError`.

Conceptually:

```text
Operation
    ↓
Operation fails
    ↓
Exception object created
    ↓
Python looks for a matching handler
    ↓
┌───────────────┐
│ Handler found │ → Handle exception
└───────────────┘

If no handler is found:
    ↓
Exception propagates
    ↓
Program/application boundary
```

Exceptions are objects.

```python
try:
    number = int("hello")
except ValueError as error:
    print(type(error))
    print(error)
```

The variable `error` refers to the exception object.

---

# 2. Basic Exception Handling

The fundamental structure is:

```python
try:
    # code that may fail
except SomeException:
    # handle failure
```

Example:

```python
try:
    number = int(value)
except ValueError:
    print("Invalid number")
```

The `try` block contains code that may raise an exception.

The `except` block defines what should happen when a matching exception occurs.

---

# 3. Catch Specific Exceptions

Prefer specific exception types.

Good:

```python
try:
    number = int(value)
except ValueError:
    print("Invalid number")
```

Avoid unnecessarily broad handlers:

```python
try:
    number = int(value)
except:
    print("Something went wrong")
```

A broad handler can hide unrelated problems.

For example:

```python
try:
    number = int(value)
    result = 100 / number
    save_to_database(result)
except:
    print("Something went wrong")
```

The failure could come from:

- integer conversion
- division by zero
- database operation
- programmer error
- another unexpected condition

Specific exception handling preserves useful information.

---

# 4. Multiple Exceptions

Different failures can be handled separately.

```python
try:
    number = int(value)
    result = 100 / number
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Multiple exceptions can also share one handler:

```python
try:
    ...
except (ValueError, TypeError):
    ...
```

Use this only when both exceptions genuinely require the same handling.

---

# 5. Python's Exception Hierarchy

Python exceptions form a class hierarchy.

A simplified view:

```text
BaseException
│
├── SystemExit
├── KeyboardInterrupt
└── Exception
     │
     ├── ValueError
     ├── TypeError
     ├── KeyError
     ├── IndexError
     ├── ZeroDivisionError
     ├── FileNotFoundError
     ├── OSError
     └── ...
```

Most ordinary application errors derive from `Exception`.

Therefore:

```python
except Exception:
    ...
```

can catch many application-level exceptions.

However:

```python
except BaseException:
    ...
```

is much broader and includes things such as `KeyboardInterrupt` and `SystemExit`.

For normal application code, `BaseException` should not be caught casually.

---

# 6. `else`

A `try` statement can have an `else` block.

```python
try:
    number = int(value)
except ValueError:
    print("Invalid number")
else:
    print("Conversion succeeded")
```

The `else` block runs only when the `try` block completes successfully.

Execution:

```text
try
 │
 ├── exception → except
 │
 └── success → else
```

Using `else` can keep the exception-sensitive section small.

For example:

```python
try:
    result = process(data)
except ValueError:
    handle_error()
else:
    save(result)
```

This is different from putting everything into `try`:

```python
try:
    result = process(data)
    save(result)
except ValueError:
    handle_error()
```

The second version may accidentally catch a `ValueError` raised by `save()`.

---

# 7. `finally`

`finally` runs regardless of whether an exception occurred.

```python
try:
    process()
except ValueError:
    handle_error()
finally:
    cleanup()
```

Conceptually:

```text
             ┌── success ──┐
try ─────────┤             ├── finally
             └── failure ──┘
```

`finally` is commonly used for cleanup.

```python
resource = acquire_resource()

try:
    use(resource)
finally:
    release(resource)
```

Even if `use()` raises an exception, the cleanup code executes.

---

# 8. `try`, `except`, `else`, `finally`

All four can be used together:

```python
try:
    result = process()
except ValueError:
    handle_error()
else:
    handle_success(result)
finally:
    cleanup()
```

### Successful execution

```text
try
 ↓
else
 ↓
finally
```

### Exception handled by `except`

```text
try
 ↓
except
 ↓
finally
```

### Exception not handled

```text
try
 ↓
finally
 ↓
exception propagates
```

`finally` does not automatically suppress the exception.

---

# 9. Raising Exceptions

Use `raise` to explicitly raise an exception.

```python
raise ValueError("Invalid age")
```

Example:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    return age
```

The caller can then handle it:

```python
try:
    set_age(-5)
except ValueError as error:
    print(error)
```

---

# 10. Exceptions as Function Contracts

A function can use exceptions to communicate that the caller violated its expected input contract.

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount
```

Conceptually:

```text
Valid input
    ↓
perform operation
    ↓
return result

Invalid input
    ↓
raise exception
```

Exceptions therefore become part of a function's behavioral contract.

---

# 11. Returning Errors vs Raising Exceptions

A function could return a special value:

```python
def divide(a, b):
    if b == 0:
        return None

    return a / b
```

Or raise an exception:

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return a / b
```

These have different semantics.

Returning `None` means:

> "The function completed and this is the result representing failure/no-result."

Raising an exception means:

> "Normal execution could not produce the requested result."

The correct choice depends on the API and expected failure semantics.

---

# 12. Exception Propagation

If an exception isn't handled in the current function, Python propagates it up the call stack.

Consider:

```python
def database():
    raise ConnectionError("Database unavailable")


def service():
    database()


def controller():
    service()
```

The flow is:

```text
controller()
    ↓
service()
    ↓
database()
    ↓
ConnectionError
    ↑
service()
    ↑
controller()
```

Python searches for a matching exception handler as it moves upward through the call stack.

This is one of the most important concepts for reading real Python code.

---

# 13. Handling at the Appropriate Layer

Consider a backend:

```text
HTTP Request
     ↓
Controller
     ↓
Service
     ↓
Repository
     ↓
Database
```

Suppose the database connection fails.

The repository shouldn't necessarily do:

```python
try:
    ...
except Exception:
    return None
```

This may destroy important information about the failure.

Instead, the exception may propagate upward until a layer capable of making the appropriate decision handles it.

For example:

```text
Database failure
      ↓
Repository
      ↓
Service
      ↓
API boundary
      ↓
HTTP 503
```

The exact architecture depends on the application, but the principle is:

> **Handle a failure at the layer that has enough context to make the correct decision.**

---

# 14. Re-Raising Exceptions

Sometimes a function needs to perform some local action but should not hide the original failure.

```python
try:
    process()
except ValueError:
    log_error()
    raise
```

The bare:

```python
raise
```

re-raises the currently handled exception.

Flow:

```text
failure
   ↓
catch
   ↓
log / cleanup / add context
   ↓
raise
   ↓
caller handles it
```

This is common in production systems.

---

# 15. Never Silently Swallow Exceptions

A dangerous pattern is:

```python
try:
    process()
except Exception:
    pass
```

The error disappears.

Another problematic pattern:

```python
try:
    process()
except Exception:
    print("Something went wrong")
```

and then continuing as though the operation succeeded.

Logging an error is not necessarily the same as handling it.

The important question is:

> What should happen after the failure?

Possible answers include:

- recover
- retry
- return an error
- translate the exception
- stop the operation
- propagate the exception
- trigger a fallback

---

# 16. `except Exception` Is Not Always Wrong

Broad exception handling can be appropriate at carefully chosen boundaries.

For example:

```python
try:
    run_application()
except Exception:
    logger.exception("Application failed")
```

An application boundary may need to prevent an uncontrolled crash while recording diagnostic information.

The problem isn't simply:

> "`except Exception` is bad."

The real question is:

> **Why is this code catching everything here?**

Good exception handling is about **scope, intent, and responsibility**.

---

# 17. Logging Exceptions

For production applications, use a logging system rather than relying on `print()`.

Inside an exception handler:

```python
try:
    process()
except Exception:
    logger.exception("Processing failed")
```

`logger.exception()` is particularly useful inside an exception handler because it records the traceback.

A traceback provides information about:

- exception type
- message
- call stack
- location of failure

This is critical when debugging production systems.

---

# 18. Exception Chaining

Sometimes a low-level error should be translated into an application-level error.

Example:

```python
try:
    load_config()
except FileNotFoundError as error:
    raise RuntimeError(
        "Configuration could not be loaded"
    ) from error
```

This creates a relationship:

```text
RuntimeError
     │
     └── caused by
           ↓
     FileNotFoundError
```

The syntax is:

```python
raise NewException(...) from original_error
```

Exception chaining preserves the original cause while providing a more meaningful error at a higher abstraction level.

---

# 19. Custom Exceptions

Python allows you to define domain-specific exceptions.

```python
class UserNotFoundError(Exception):
    pass
```

Then:

```python
raise UserNotFoundError("User does not exist")
```

And:

```python
try:
    find_user(username)
except UserNotFoundError:
    ...
```

Custom exceptions make application failures more expressive.

Compare:

```python
raise Exception("User doesn't exist")
```

with:

```python
raise UserNotFoundError("User doesn't exist")
```

The second communicates the meaning directly to the caller and to anyone reading the code.

---

# 20. Custom Exception Hierarchies

Custom exceptions can form their own hierarchy.

```python
class ApplicationError(Exception):
    pass


class UserError(ApplicationError):
    pass


class UserNotFoundError(UserError):
    pass


class InvalidUserError(UserError):
    pass
```

Now you can catch specifically:

```python
except UserNotFoundError:
```

or more generally:

```python
except UserError:
```

or even:

```python
except ApplicationError:
```

depending on what level of abstraction the caller needs.

---

# 21. EAFP vs LBYL

Python commonly discusses two approaches.

### LBYL — Look Before You Leap

Check before performing an operation.

```python
if username in users:
    user = users[username]
```

### EAFP — Easier to Ask Forgiveness Than Permission

Perform the operation and handle the failure.

```python
try:
    user = users[username]
except KeyError:
    user = None
```

Python often favors EAFP, but this does **not** mean exceptions should replace every conditional.

For a dictionary lookup, this may be even clearer:

```python
user = users.get(username)
```

Choose the clearest approach for the situation.

---

# 22. Context Managers and `with`

Resource cleanup is often easier with a context manager.

Instead of:

```python
file = open("data.txt")

try:
    data = file.read()
finally:
    file.close()
```

Python provides:

```python
with open("data.txt") as file:
    data = file.read()
```

The `with` statement manages the resource lifecycle.

Conceptually:

```text
Enter resource
      ↓
Execute operation
      ↓
Exit resource
      ↓
Cleanup
```

Cleanup occurs even when an exception is raised.

Context managers are therefore closely connected to exception safety.

---

# 23. Don't Use Exceptions to Hide Bugs

Consider:

```python
try:
    result = user["name"]
except Exception:
    result = "Unknown"
```

This could hide many different problems:

- `user` is `None`
- `user` is the wrong type
- data is malformed
- a programmer mistake occurred

A broad handler can convert a useful failure into incorrect behavior.

Good error handling should make systems **more observable and reliable**, not make problems disappear.

---

# 24. Exceptions vs Programming Bugs

Not every exception should be "handled."

Some exceptions represent expected operational failures:

```text
FileNotFoundError
ConnectionError
TimeoutError
ValueError
```

Other exceptions may reveal programming bugs:

```text
TypeError
AttributeError
unexpected KeyError
incorrect assumptions about data
```

For example:

```python
def calculate_total(items):
    return items["total"]
```

If `items` unexpectedly becomes a list, catching the resulting exception and returning `0` may hide a real bug.

The right response may be to fix the underlying programming error rather than suppress it.

---

# 25. Input Validation

Exceptions are commonly used for validating function inputs.

```python
def parse_age(value):
    try:
        age = int(value)
    except ValueError:
        raise ValueError("Age must be a number")

    if age < 0:
        raise ValueError("Age cannot be negative")

    return age
```

There are two different failure sources:

```text
"abc"
 ↓
int() fails
 ↓
ValueError
```

and:

```text
-5
 ↓
conversion succeeds
 ↓
validation fails
 ↓
our ValueError
```

This distinction is useful when designing validation functions.

---

# 26. Exceptions in Backend Applications

Consider a backend service:

```text
Request
   ↓
Controller
   ↓
Service
   ↓
Repository
   ↓
Database
```

The service might raise:

```python
UserNotFoundError
```

The API layer could translate it into:

```text
HTTP 404
```

An invalid request could produce:

```python
InvalidUserError
```

which could become:

```text
HTTP 400
```

A database outage might become:

```text
HTTP 503
```

This demonstrates an important architectural pattern:

> **Internal exceptions can be translated into external representations at system boundaries.**

---

# 27. Exceptions and Transactions

Exception handling becomes more complicated when multiple operations form one logical transaction.

Consider:

```python
create_order()
charge_payment()
send_email()
```

Suppose:

```text
create_order() → success
charge_payment() → failure
```

Now the system may have partially completed an operation.

Proper failure handling may involve:

- rollback
- compensation
- cleanup
- retries
- idempotency
- consistency
- logging
- user notification

Therefore, exception handling is connected to broader system-design concepts.

---

# 28. Retrying Exceptions

Some failures are transient.

Examples:

```text
network timeout
temporary connection failure
service temporarily unavailable
```

A system may retry:

```python
for attempt in range(max_attempts):
    try:
        connect()
        break
    except ConnectionError:
        ...
```

But retries must be designed carefully.

Questions to consider:

- Is the operation safe to repeat?
- How many times should we retry?
- Should there be a delay?
- Is the failure transient?
- What happens after all attempts fail?
- Could retrying duplicate an operation?

For example, blindly retrying a payment operation could potentially cause duplicate charges if the first request actually succeeded but its response was lost.

---

# 29. Exceptions in Robotics

The same principles apply to robotics.

A simplified pipeline might be:

```text
Camera
   ↓
Image acquisition
   ↓
Computer vision
   ↓
Model inference
   ↓
Decision
   ↓
Actuator
```

Potential failures include:

```text
camera disconnected
      ↓
timeout
      ↓
invalid frame
      ↓
model inference failure
      ↓
hardware communication failure
```

Different failures may require different responses:

```text
retry
recover
fallback
stop
restart
report
propagate
```

For example, silently ignoring a sensor failure with:

```python
except Exception:
    pass
```

would generally be a poor design for a robotics system.

The correct response depends on the safety and reliability requirements of the system.

---

# 30. Example: Sensor Exception Hierarchy

A robotics application might define:

```python
class SensorError(Exception):
    pass


class SensorReadError(SensorError):
    pass


class InvalidSensorValueError(SensorError):
    pass
```

Now callers can distinguish:

```python
try:
    temperature = read_sensor()
except SensorReadError:
    recover_sensor()
except InvalidSensorValueError:
    reject_reading()
```

Or handle both at a higher level:

```python
except SensorError:
    report_sensor_failure()
```

This is the same exception hierarchy principle used in backend systems.

---

# 31. Exceptions and System Boundaries

A useful general model is:

```text
External Input
      ↓
Validation
      ↓
Business Logic
      ↓
External Systems
      ↓
Output
```

Failures can occur anywhere.

The exception mechanism allows the failure to move toward a layer capable of deciding what to do.

```text
Failure
   ↓
Exception
   ↓
Propagation
   ↓
Appropriate boundary
   ↓
Handle / Translate / Retry / Recover / Re-raise
```

The key question is not:

> "Where can I catch this?"

It is:

> **"Where should this failure be handled?"**

---

# 32. Python vs Java

Because Python is your secondary language and Java is your strongest programming language, the following comparison is useful.

| Java | Python |
|---|---|
| `try` | `try` |
| `catch` | `except` |
| `finally` | `finally` |
| `throw` | `raise` |
| Custom exceptions | Custom exceptions |
| Exception hierarchy | Exception hierarchy |
| Checked exceptions | No checked exceptions |
| `throws` | No direct equivalent |
| try-with-resources | `with` / context managers |

The biggest difference is that Python does **not** have Java-style checked exceptions.

Java:

```java
void loadConfig() throws IOException {
    ...
}
```

Python has no equivalent requirement that a function declare its possible exceptions.

Therefore, when reading Python code, pay attention to:

- implementation
- documentation
- type hints
- tests
- custom exception classes
- callers
- exception handlers

to understand what can fail.

---

# 33. Exception Handling Design Principles

### 1. Catch specific exceptions

```python
except ValueError:
```

is generally preferable to:

```python
except:
```

when you know the expected failure.

### 2. Don't hide failures

Avoid:

```python
except Exception:
    pass
```

unless there is a very deliberate reason.

### 3. Handle errors at the appropriate layer

The layer that has enough context should decide what to do.

### 4. Preserve useful information

Use exception chaining when translating errors:

```python
raise NewError(...) from error
```

### 5. Use domain-specific exceptions

Prefer:

```python
UserNotFoundError
```

over:

```python
Exception("user missing")
```

when the distinction matters.

### 6. Don't catch exceptions merely because you can

Ask:

> Can this layer actually recover?

If not, propagation may be better.

### 7. Don't confuse error handling with bug hiding

An exception can be evidence of a programming bug that should be fixed.

### 8. Make cleanup reliable

Use:

```python
finally
```

or preferably appropriate context managers:

```python
with ...
```

for resource lifecycle management.

### 9. Be careful with retries

Retry only when the failure is appropriate to retry and the operation is safe to repeat.

---

# 34. Code Reading Checklist

When reading unfamiliar Python code, ask:

### What can fail?

Identify operations such as:

```python
int(value)
data[key]
file.read()
socket.send()
database.query()
```

### What exceptions can they produce?

Look for:

```python
ValueError
KeyError
FileNotFoundError
ConnectionError
TimeoutError
```

### Where are they caught?

Find:

```python
try:
except
```

### Is the handler specific?

Compare:

```python
except ValueError:
```

with:

```python
except Exception:
```

### Is the error swallowed?

Look for:

```python
pass
return None
```

inside broad exception handlers.

### Is it re-raised?

Look for:

```python
raise
```

### Is it translated?

Look for:

```python
raise SomeOtherError(...) from error
```

### Is cleanup guaranteed?

Look for:

```python
finally
```

or:

```python
with
```

### Where does the exception ultimately go?

Trace the call stack upward.

---

# 35. Code Review Checklist

When reviewing Python exception handling, check:

- [ ] Are expected exceptions caught specifically?
- [ ] Is a bare `except` being used unnecessarily?
- [ ] Is `Exception` being caught too broadly?
- [ ] Are programming bugs being hidden?
- [ ] Are exceptions silently swallowed?
- [ ] Are meaningful error messages provided?
- [ ] Are custom exceptions appropriate?
- [ ] Is the exception hierarchy sensible?
- [ ] Is exception propagation intentional?
- [ ] Is re-raising preserving the original failure?
- [ ] Is exception chaining used where appropriate?
- [ ] Is cleanup guaranteed?
- [ ] Are resources managed using context managers where appropriate?
- [ ] Are retries bounded?
- [ ] Is retrying the operation actually safe?
- [ ] Is the exception being handled at the correct architectural layer?

---

# 36. Core Mental Model

The most important model from this chapter is:

```text
                  Something can fail
                         │
                         ▼
                 What operation failed?
                         │
                         ▼
               What exception represents it?
                         │
                         ▼
                Should I handle it here?
                    /            \
                  YES             NO
                   │               │
                   ▼               ▼
                Handle          Propagate
                   │               │
          ┌────────┼───────┐       │
          ↓        ↓       ↓       │
        Recover  Translate Retry    │
          │        │       │        │
          └────────┼───────┘        │
                   │                │
                   └───────┬────────┘
                           ↓
                    Appropriate layer
                           ↓
               Handle / Translate /
                Recover / Re-raise
```

Think of an exception as **control flow for failure**.

---

# 37. Quick Reference

## Basic handling

```python
try:
    operation()
except ValueError:
    handle_error()
```

## Multiple exceptions

```python
try:
    operation()
except ValueError:
    ...
except TypeError:
    ...
```

## Same handler

```python
except (ValueError, TypeError):
    ...
```

## `else`

```python
try:
    operation()
except ValueError:
    ...
else:
    success()
```

## `finally`

```python
try:
    operation()
finally:
    cleanup()
```

## Raise

```python
raise ValueError("Invalid input")
```

## Re-raise

```python
except ValueError:
    log_error()
    raise
```

## Custom exception

```python
class UserNotFoundError(Exception):
    pass
```

## Exception chaining

```python
except FileNotFoundError as error:
    raise ConfigurationError("Config missing") from error
```

## Context manager

```python
with open("data.txt") as file:
    data = file.read()
```

---

# 38. Python Exception vs Java Exception Mental Translation

When reading Python, you can roughly translate:

```python
try:
    operation()
except ValueError as error:
    handle(error)
```

to the Java mental model:

```java
try {
    operation();
} catch (ValueError error) {
    handle(error);
}
```

And:

```python
raise ValueError("Invalid")
```

to:

```java
throw new ValueError("Invalid");
```

But remember the important differences:

- Python has no checked exceptions.
- Python uses `except`, not `catch`.
- Python uses `raise`, not `throw`.
- Python commonly uses EAFP.
- Python's `with` provides context-manager-based resource management.
- Exception behavior is often documented through implementation and tests rather than a `throws` declaration.

---

# 39. Chapter Completion Criteria

You can consider this chapter complete when you can comfortably:

- explain what an exception is
- use `try` / `except`
- catch specific exceptions
- handle multiple exception types
- explain `else`
- explain `finally`
- raise exceptions manually
- re-raise exceptions
- trace exception propagation through function calls
- create custom exceptions
- design exception hierarchies
- use exception chaining
- explain EAFP vs LBYL
- understand context managers
- identify swallowed exceptions
- identify overly broad exception handling
- distinguish operational failures from programming bugs
- reason about retries
- review backend-style exception handling
- recognize how exception handling applies to robotics systems

---

# 40. Key Takeaways

1. **Exceptions are objects representing failures or abnormal conditions.**

2. **`try`/`except` controls how those failures are handled.**

3. **Catch the most specific exception you can meaningfully handle.**

4. **`raise` communicates failure explicitly to the caller.**

5. **Unhandled exceptions propagate through the call stack.**

6. **Don't automatically handle an exception at the point where it occurs.**

7. **Handle failures at the layer that has enough context to make the right decision.**

8. **Custom exceptions make domain-specific failures understandable.**

9. **Exception chaining preserves the original cause when translating errors.**

10. **`finally` and context managers help guarantee cleanup.**

11. **Broad exception handlers can hide real bugs.**

12. **Retrying is a system-design decision, not merely a loop around `try`/`except`.**

13. **Good exception handling makes failures visible, meaningful, and recoverable—not invisible.**

---

# Next Chapter

## Chapter 7 — Modules, Packages & Imports

The next chapter moves us from **individual Python programs** toward understanding **real Python projects**.

We'll cover:

```text
Modules
   ↓
Imports
   ↓
Packages
   ↓
__init__.py
   ↓
Import paths
   ↓
Absolute vs relative imports
   ↓
Python package structure
   ↓
__name__
   ↓
__main__
   ↓
Circular imports
   ↓
Public vs internal modules
   ↓
Real project architecture
```

This chapter will be particularly important for your goal of being able to **open an unfamiliar Python repository and understand how the codebase is organized and connected**.
