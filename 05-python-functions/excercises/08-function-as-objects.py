from collections.abc import Callable

# Exercise 29:
# Create a function square(number) that returns number * number.
#
# Assign the function itself to another variable:
# operation = square
#
# Call operation(5).
#
# Verify that operation and square refer to the same function object.

def square(number: int) -> int:
    return number**2

operation = square
print(operation(5))
print(operation==square)


# Exercise 30:
# Create:
#   add(a, b)
#   multiply(a, b)
#   subtract(a, b)
#
# Create:
#   apply_operation(operation, a, b)
#
# apply_operation() should call the supplied function with a and b
# and return the result.
#
# Test it by passing add, multiply, and subtract.

def add(a: int, b: int) -> int:
    return a+b

def subtract(a: int, b: int) -> int:
    return a-b

def multiply(a: int, b: int) -> int:
    return a*b

def apply_operation(operation: Callable[[int , int] , int] , a: int , b: int) -> int:
    return operation(a,b)

print(apply_operation(add, 10, 20))
print(apply_operation(multiply, 10, 20))
print(apply_operation(subtract, 10, 20))


# Exercise 31:
# Create lambda functions for:
# 1. Squaring a number
# 2. Checking whether a number is even
# 3. Multiplying two numbers
#
# Store each lambda in a variable and test them.
#
# Rewrite at least one lambda as a normal def function.
# Compare readability.

square: Callable[[int],int] = lambda x: x**2
is_even: Callable[[int],bool] =lambda x: x%2==0
multiply: Callable[[int, int],int] = lambda x,y: x*y

print(square(4))
print(is_even(2))
print(multiply(2,3))


