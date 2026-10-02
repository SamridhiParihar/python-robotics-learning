# Exercise 19:
# Create a function test_scope().
# Inside it, create a variable called message.
# Print message inside the function.
#
# Then call test_scope().
#
# After that, try to print message outside the function.
# Observe and understand the error.

def test_scope():
    message = "hello"
    print(message)

test_scope()

# print(message)

# Exercise 20:
# Create a global variable message = "Hello".
#
# Create one function that reads and prints message.
#
# Create another function that tries to assign a new value to message.
#
# Observe the behavior.
# Understand the difference between reading and assigning global variables.


# Define the global variable
message = "Hello"

def read_message() -> None:
    '''Reads and prints the global variable'''
    # Python allows you to read global variables inside a function automatically
    print(f"Inside read_message(): {message}")

def try_modify_message() -> None:
    '''Tries to assign a new value to message'''
    # Python treats this as creating a NEW local variable named 'message'
    # It does NOT change the global 'message' outside the function
    message = "Goodbye" 
    print(f"Inside try_modify_message(): {message}")

# --- Test the Behavior ---
print("--- Initial State ---")
print(f"Global message starts as: {message}\n")

print("--- Step 1: Reading ---")
read_message()
print(f"Global message after read_message(): {message}\n")

print("--- Step 2: Assigning ---")
try_modify_message()
print(f"Global message after try_modify_message(): {message}")



# Exercise 21:
# Implement two versions of process():
#
# Version A:
# Use a global config dictionary.
#
# Version B:
# Pass config as a function parameter.
#
# Example config:
# {"mode": "fast"}
#
# Compare both implementations.
# Identify which version has an explicit dependency and why.

# --- Version A: Using a Global Config Dictionary ---
# The dependency is hidden (implicit) because it relies on this specific outer variable.
global_config = {"mode": "fast"}

def process_version_a() -> str:
    '''Process data using a global configuration'''
    # Reads directly from the global scope
    if global_config.get("mode") == "fast":
        return "Processing quickly (Global)!"
    return "Processing normally (Global)!"


# --- Version B: Passing Config as a Function Parameter ---
# The dependency is clearly declared (explicit) right in the function signature.
def process_version_b(config: dict[str, str]) -> str:
    '''Process data using a passed configuration dictionary'''
    if config.get("mode") == "fast":
        return "Processing quickly (Parameter)!"
    return "Processing normally (Parameter)!"


# --- Test the Behavior ---
local_config = {"mode": "fast"}

print(process_version_a())            
print(process_version_b(local_config))


# Exercise 22:
# Create add_item(numbers).
# The function should append 100 to the supplied list.
#
# Create a list outside the function.
# Pass it to add_item().
# Print the list before and after the function call.
#
# Explain why the original list changed.

def add_item(numbers: list[int]) -> None:
    '''Append 100 to the supplied list'''
    numbers.append(100)

# Create a list outside the function
my_list = [10, 20, 30]

# Print before, call the function, and print after
print(f"Before function call: {my_list}")

add_item(my_list)

print(f"After function call:  {my_list}")




# Exercise 23:
# Create add_item_in_place(numbers).
# It should modify the supplied list directly.
#
# Create add_item_copy(numbers).
# It should create a new list, add an item to the new list,
# and return the new list without modifying the original.
#
# Demonstrate the difference by printing:
# - original list
# - returned list
# before and after each function call.

def add_item_in_place(numbers: list[int]) -> None:
    '''Modifies the supplied list directly in memory'''
    numbers.append(100)

def add_item_copy(numbers: list[int]) -> list[int]:
    '''Creates a new list copy, modifies the copy, and returns it'''
    # We use .copy() or list(numbers) to create a new object at a new memory reference
    new_list = numbers.copy()
    new_list.append(200)
    return new_list

# --- 1. Testing add_item_copy() ---
list_a = [10, 20, 30]
print("--- Testing Copy Function ---")
print(f"Original list before call: {list_a}")

returned_a = add_item_copy(list_a)

print(f"Original list after call:  {list_a}  (Untouched!)")
print(f"Returned list from call:   {returned_a}")
print("-" * 30 + "\n")

# --- 2. Testing add_item_in_place() ---
list_b = [10, 20, 30]
print("--- Testing In-Place Function ---")
print(f"Original list before call: {list_b}")

returned_b = add_item_in_place(list_b)

print(f"Original list after call:  {list_b}  (Modified!)")
print(f"Returned list from call:   {returned_b}")


