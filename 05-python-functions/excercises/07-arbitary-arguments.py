from typing import Any

# Exercise 24:
# Create add_all(*numbers).
# It should accept any number of positional arguments.
# Return their total.
# Do NOT use sum().
#
# Test with:
# add_all(1, 2)
# add_all(1, 2, 3)
# add_all(1, 2, 3, 4, 5)
# add_all()

def add_all(*numbers: int) -> int:
    '''return total of the given numbers'''
    total: int = 0
    for num in numbers:
        total+=num
    return total

add_all(1, 2)
add_all(1, 2, 3)
add_all(1, 2, 3, 4, 5)

# Exercise 24:
# Create add_all(*numbers).
# It should accept any number of positional arguments.
# Return their total.
# Do NOT use sum().
#
# Test with:
# add_all(1, 2)
# add_all(1, 2, 3)
# add_all(1, 2, 3, 4, 5)
# add_all()
def find_max(*numbers: int) -> int:
    '''Accept any number of positional arguments and return the largest without using max()'''
    # 1. Handle the zero-argument edge case
    if not numbers:
        raise ValueError("find_max() expected at least 1 argument, got 0")
    
    # 2. Initialize max_num with the first element in the tuple
    max_num = numbers[0]
    
    # 3. Loop through the rest of the arguments to find the largest
    for num in numbers:
        if num > max_num:
            max_num = num
            
    return max_num

# --- Required Exercise Tests ---
print(find_max(10, 20, 5))    
print(find_max(-1, -5, -2))   
print(find_max(100))          

# --- Testing the Zero Argument Edge Case ---
try:
    find_max()
except ValueError as e:
    print(f"Error caught: {e}")  # Output: Error caught: find_max() expected at least 1 argument, got 0



# Exercise 26:
# Create print_details(**details).
# The function should accept any number of keyword arguments.
# Iterate over details and print each key-value pair.
#
# Test it with:
# name, age, city, profession
# and then call it with a completely different set of fields.

def print_details(**details: Any ) -> None:
    '''The function should accept any number of keyword arguments. and print each key value pair'''
    for key,value in details.items():
        print(f"{key}: {value}")

print_details(
    name="Sam",
    age=24,
    city="Delhi",
    profession="Engineer"
)

# Exercise 27:
# Create configure(**settings).
# It should accept arbitrary configuration options.
# Return the settings dictionary.
#
# Test with:
# debug=True
# port=8080
# host="localhost"
#
# Then call it with different configuration fields.

def configure(**setting: Any) -> dict[str, Any]:
    '''It accept arbitrary configuration options and Return the settings dictionary.'''
    config: dict[str, Any] = {}
    for key, value in setting.items():
        config[key] = value

    return config

print (configure(
    debug=True,
    port=8080,
    host="localhost"
))


# Exercise 28:
# Create:
#   log(message, level="INFO", **metadata)
#
# Example:
# log(
#     "User logged in",
#     level="INFO",
#     user_id=123,
#     source="api"
# )
#
# Print a readable log message containing:
# - level
# - message
# - metadata
#
# Test with and without metadata.

def log(message: str, level: str = "INFO", **metadata: Any) -> None:
    '''Print a readable log message containing the given metadata'''
    print(f"Log level : {level}\nMessage: {message}")
    for key , value in metadata.items():
        print(f"{key}: {value}")


log(
    "User logged in",
    level="INFO",
    user_id=123,
    source="api"
)