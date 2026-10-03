# Exercise 1 — Safe Integer Conversion
#
# Write a function:
#     safe_int(value)
#
# Requirements:
# - Try to convert value into an integer.
# - If conversion succeeds, return the integer.
# - If conversion fails because of an invalid value, return None.
# - Catch only the specific exception that is expected from integer conversion.
#
# Examples:
# safe_int("42")       -> 42
# safe_int("-10")      -> -10
# safe_int("hello")    -> None
# safe_int("12.5")     -> None
#
# Do not use a bare `except:`.


# Your solution here


def safe_int (value: str) -> int | None :
    try: 
        return int(value)
    except ValueError :
        return None

print(safe_int("42"))
print(safe_int("-42"))
print(safe_int("42.5"))
print(safe_int("Hello"))


# Exercise 2 — Safe Division
#
# Write a function:
#     safe_divide(a, b)
#
# Requirements:
# - Return a / b when the division succeeds.
# - Handle division by zero.
# - Return None when b is zero.
# - Catch only the exception relevant to division by zero.
#
# Examples:
# safe_divide(10, 2) -> 5.0
# safe_divide(10, 0) -> None
#
# Think about:
# - What operation can fail?
# - Which exception represents that failure?
#
#
# Your solution here

def safe_divide(a: int, b: int) -> float | None :
    try : 
        return a/b
    except ZeroDivisionError :
        return None


# Exercise 3 — Calculator
#
# Write a function:
#     calculate(a, b, operation)
#
# Supported operations:
# - "add"
# - "subtract"
# - "multiply"
# - "divide"
#
# Examples:
# calculate(10, 5, "add")      -> 15
# calculate(10, 5, "subtract") -> 5
# calculate(10, 5, "multiply") -> 50
# calculate(10, 5, "divide")   -> 2.0
#
# Requirements:
# - Handle division by zero.
# - If the operation is unsupported, raise ValueError.
# - The ValueError should contain a useful message.
#
# Think carefully about which errors should be handled
# inside the function and which should be raised to the caller.
#
#
# Your solution here

def calculate(a: int, b: int , operation: str) -> float | int | None | Exception:
    if operation == "add":
        return a+b
    elif operation == "subtract":
        return a-b
    elif operation == "multiply":
        return a*b
    elif operation == "division":
        try:
            return a/b
        except ZeroDivisionError:
            print("can't divide by zero that is undefined")
    else :
        raise ValueError(f"provided operation i.e, {operation} is not supported. Supported options are 'add', 'subtract', 'multiply', or 'divide'")
    
# print(calculate(4,5,"power"))

# Exercise 4 — Dictionary Lookup
#
# Write:
#     get_user(users, username)
#
# Example data:
#
# users = {
#     "sam": {"age": 24},
#     "rahul": {"age": 25}
# }
#
# Requirements:
# - Return the user's dictionary if the username exists.
# - If the username does not exist, handle KeyError.
# - Return None when the user does not exist.
#
# Important:
# - Solve this using the EAFP approach.
# - Try the dictionary access and handle the failure.
# - Do not use `except Exception`.
#
# Examples:
# get_user(users, "sam")  -> {"age": 24}
# get_user(users, "john") -> None
#
#
# Your solution here
users = {
    "sam": {"age": 24},
    "rahul": {"age": 25}
}
def get_user(users: dict , username: str) -> dict | None:
    try :
        return users[username]
    except KeyError :
        print (f"give username : {username} doesn't exist in the dictionary !")
        return None 
print("......")
print(get_user(users, "sam"))
print(get_user(users, "john"))


# Exercise 5 — Parse and Process
#
# Write:
#     process_number(value)
#
# Requirements:
# 1. Convert value to an integer.
# 2. Multiply the integer by 10.
# 3. If conversion fails, print:
#       "Invalid number"
# 4. If conversion succeeds:
#       - print "Processing successful"
#       - return the calculated result
# 5. Use the `else` block appropriately.
#
# Examples:
#
# process_number("5")
# -> prints "Processing successful"
# -> returns 50
#
# process_number("abc")
# -> prints "Invalid number"
#
# Focus on understanding why the successful processing
# belongs in `else` rather than inside the `except`.
#
#
# Your solution here

def process_number(value: str) -> int | None:
    try : 
        num: int = int(value)
    except ValueError :
        print ("Invalid number")
    else :
        print("Processing successful")
        return num*10

# Exercise 6 — Guaranteed Cleanup
#
# Write:
#     process_file(filename)
#
# Requirements:
# - Open the specified file.
# - Read its contents.
# - Handle FileNotFoundError.
# - Print an appropriate error message if the file doesn't exist.
# - Use a finally block.
# - Ensure your cleanup code runs whether the operation succeeds
#   or fails.
#
# For this exercise, use explicit open() and close()
# so that you can practice finally.
#
# Do NOT use `with` yet.
#
#
# Your solution here

def process_file(filename):
    file = None
    try:
        file = open(filename, "r", encoding="utf-8")
        contents = file.read()
        print("File read successfully.")
        return contents
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
        
    finally:
        if file is not None:
            file.close()
            print("Cleanup: File stream explicitly closed safely.")



# Exercise 7 — Validate Age
#
# Write:
#     validate_age(age)
#
# Rules:
# - Age must be an integer.
# - Age cannot be negative.
# - Age cannot be greater than 120.
# - If valid, return the age.
# - If invalid, raise ValueError.
#
# Examples:
# validate_age(24)  -> 24
# validate_age(-5)  -> raises ValueError
# validate_age(150) -> raises ValueError
#
# Include useful error messages.
#
# Think about:
# - When should a function return a value?
# - When should it raise an exception?
#
#
# Your solution here

def validate_age(age: int) -> int :
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer. Received: {type(age).__name__}")
        
    if age < 0:
        raise ValueError(f"Invalid age: {age}. Age cannot be negative.")
    if age > 120:
        raise ValueError(f"Invalid age: {age}. Age cannot be greater than 120.")
            
    return age


# Exercise 8 — Raise and Catch
#
# Reuse validate_age(age) from Exercise 7.
#
# Create:
#     register_user(name, age)
#
# Requirements:
# - Call validate_age(age).
# - If validation succeeds, print:
#       "User <name> registered successfully"
# - If validate_age() raises ValueError:
#       - catch the exception
#       - print the exception message
#
# The important concept:
#
# register_user()
#       ↓
# validate_age()
#       ↓
# raises ValueError
#       ↓
# register_user() catches it
#
#
# Your solution here

def register_user(name: str, age: int) -> None : 
    try : 
        validate_age(age)
    except (TypeError, ValueError) as error:
        print (error)
    else :
        print (f"{name} got registered successfully")


# Exercise 9 — Exception Propagation
#
# Create three functions:
#
#     database()
#     service()
#     controller()
#
# Flow:
#
# controller()
#     ↓
# service()
#     ↓
# database()
#
# Requirements:
# - database() should raise:
#       ConnectionError("Database unavailable")
#
# - Do NOT catch the exception inside database().
# - Do NOT catch the exception inside service().
# - Catch the exception only inside controller().
#
# Expected flow:
#
# database()
#     raises
#         ↓
# service()
#         ↓
# controller()
#         ↓
# catches ConnectionError
#
# Print an appropriate message when controller()
# catches the exception.
#
#
# Your solution here

def database():
    raise ConnectionError("Not able to connect to db due to network issue !")

def service():
    database()

def controller():
    try :
        service()
    except ConnectionError as error:
        print("DB connection failure ")
        print (error)


# Exercise 10 — Re-raise an Exception
#
# Create:
#     database()
#     service()
#     controller()
#
# Flow:
#
# database()
#     ↓
# raises ConnectionError
#     ↓
# service()
#     ↓
# logs/prints the error
#     ↓
# re-raises the same exception
#     ↓
# controller()
#     ↓
# handles the exception
#
# Requirements:
# - database() raises ConnectionError.
# - service() catches ConnectionError.
# - service() prints/logs that the database failed.
# - service() must then re-raise the exception.
# - controller() catches the propagated exception.
#
# Important:
# - Use `raise` to re-raise the current exception.
# - Do not silently swallow the exception.
#
#
# Your solution here

def database():
    raise ConnectionError("Not able to connect to db due to network issue !")

def service():
    try : 
        database()
    except ConnectionError :
        print("Database connection failed !")
        raise 

def controller():
    try :
        service()
    except ConnectionError as error:
        print("DB connection failure ")
        print (error)


# Exercise 11 — Custom Exception: User Not Found
#
# Create a custom exception:
#
#     UserNotFoundError
#
# It should inherit from Exception.
#
# Then create:
#
#     find_user(users, username)
#
# Requirements:
# - Return the user if the username exists.
# - If the username does not exist:
#       raise UserNotFoundError
# - Include a useful error message.
#
# Example:
#
# users = {
#     "sam": {"age": 24},
#     "rahul": {"age": 25}
# }
#
# find_user(users, "sam")
# -> returns the user
#
# find_user(users, "john")
# -> raises UserNotFoundError
#
#
# Your solution here

class UserNotFoundError(Exception):
    def __init__(self, username, message="User not found"):
        self.username = username
        self.message = f"{message}: '{username}'"
        super().__init__(self.message)

def find_user(users, username):
    user: dict = users.get(username)
    if user is None :
        raise UserNotFoundError(username, "the user doesn't not exist")
    return user

# Exercise 12 — Custom Exception Hierarchy
#
# Create the following hierarchy:
#
# ApplicationError(Exception)
#     |
#     └── UserError(ApplicationError)
#             |
#             ├── UserNotFoundError(UserError)
#             |
#             └── InvalidUserError(UserError)
#
# Then:
#
# 1. Create a function that can raise UserNotFoundError.
# 2. Create a function that can raise InvalidUserError.
# 3. Catch UserError in the caller.
#
# Demonstrate that catching UserError also catches:
# - UserNotFoundError
# - InvalidUserError
#
# The goal is to understand exception inheritance.
#
#
# Your solution here


class ApplicationError(Exception):
    """Base exception for all application-specific errors."""
    pass

class UserError(ApplicationError):
    """Base exception for all user-related validation or lookup errors."""
    pass

class UserNotFoundError(UserError):
    """Raised when a specified user does not exist."""
    pass

class InvalidUserError(UserError):
    """Raised when user data fails validation rules (e.g., empty username)."""
    pass



DATABASE = {"sam": {"age": 24}}

def find_user(username: str) -> dict:
    """Raises UserNotFoundError if the username isn't in the database."""
    if username not in DATABASE:
        raise UserNotFoundError(f"Database lookup failed: '{username}' not found.")
    return DATABASE[username]

def create_user(username: str, age: int) -> None:
    """Raises InvalidUserError if data constraints are violated."""
    if not username or len(username) < 3:
        raise InvalidUserError("Username must be at least 3 characters long.")
    if age < 0:
        raise InvalidUserError("Age cannot be negative.")
    DATABASE[username] = {"age": age}



print("--- Test Case 1: Triggering UserNotFoundError ---")
try:
    find_user("john")  # This user doesn't exist
except UserError as e:
    print(f"Caught a UserError subclass successfully!")
    print(f"Actual Exception Type: {type(e).__name__}")
    print(f"Error Message: {e}\n")


print("--- Test Case 2: Triggering InvalidUserError ---")
try:
    create_user("ab", 25)  # Username is too short
except UserError as e:
    print(f"Caught a UserError subclass successfully!")
    print(f"Actual Exception Type: {type(e).__name__}")
    print(f"Error Message: {e}\n")



# Exercise 13 — Exception Chaining
#
# Create a custom exception:
#
#     ConfigurationError
#
# Create:
#
#     load_config(filename)
#
# Requirements:
# - Try to open the configuration file.
# - If FileNotFoundError occurs:
#       - catch it
#       - raise ConfigurationError
#       - preserve the original exception using `from`
#
# Conceptually:
#
# FileNotFoundError
#       ↓
# ConfigurationError
#
# The caller should see ConfigurationError,
# but the original FileNotFoundError should remain
# available as the cause.
#
# Use:
#
#     raise ... from error
#
#
# Your solution here
class ConfigurationError(Exception):
    """Raised when the configuration cannot be loaded or parsed."""
    pass


# -----------------------------------------------------------------------------
# 2. Implement the load_config function with Exception Chaining
# -----------------------------------------------------------------------------
def load_config(filename: str) -> str:
    """Attempts to read a config file and chains FileNotFoundError to ConfigurationError."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError as original_error:
        # Wrap the system-level error into an application-level error
        # 'from original_error' links the two exceptions together
        raise ConfigurationError(f"Failed to initialize settings from '{filename}'") from original_error


print("--- Triggering Chained Exception ---")
try:
    load_config("missing_settings.json")
except ConfigurationError as app_error:
    print(f"Caught Application Error: {app_error}")
    
    # Access the preserved cause using the __cause__ attribute
    system_error = app_error.__cause__
    print(f"Original Root Cause: {type(system_error).__name__} -> {system_error}\n")
    
    # Let's intentionally trigger the full traceback visualization
    print("--- Simulating Uncaught Full Traceback ---")
    raise app_error

# Exercise 14 — User Registration Validation
#
# Create:
#
#     register_user(name, email, age)
#
# Validation rules:
#
# - name must not be empty
# - email must contain "@"
# - age must be between 18 and 120
#
# Create custom exceptions:
#
#     InvalidUserError
#     InvalidEmailError
#     InvalidAgeError
#
# Requirements:
# - register_user() should raise the appropriate exception.
# - Do NOT catch the exceptions inside register_user().
# - Create a separate caller that handles the exceptions.
#
# Example:
#
# register_user("", "sam@example.com", 24)
# -> InvalidUserError
#
# register_user("Sam", "invalid-email", 24)
# -> InvalidEmailError
#
# register_user("Sam", "sam@example.com", 15)
# -> InvalidAgeError
#
# The goal is to separate:
#
# validation logic
#       from
# exception handling
#
#
# Your solution here


class InvalidUserError(Exception):
    """Raised when the username/name constraint is violated."""
    pass

class InvalidEmailError(Exception):
    """Raised when the email format constraint is violated."""
    pass

class InvalidAgeError(Exception):
    """Raised when the age constraint is violated."""
    pass


def register_user(name: str, email: str, age: int) -> dict:
    """Validates user details and returns a profile dict, or raises custom exceptions."""
    # Rule 1: Name must not be empty
    if not name or name.strip() == "":
        raise InvalidUserError("Registration failed: Name cannot be empty.")
        
    # Rule 2: Email must contain '@'
    if "@" not in email:
        raise InvalidEmailError(f"Registration failed: '{email}' is not a valid email address.")
        
    # Rule 3: Age must be between 18 and 120
    if not (18 <= age <= 120):
        raise InvalidAgeError(f"Registration failed: Age {age} must be between 18 and 120.")
        
    # If all rules pass
    return {"name": name, "email": email, "age": age}

def run_registration_pipeline(name: str, email: str, age: int) -> None:
    """Invokes the registration logic and safely handles potential exceptions."""
    print(f"Attempting to register: Name={repr(name)}, Email={repr(email)}, Age={age}")
    try:
        user_profile = register_user(name, email, age)
        print(f"🎉 Success! User registered: {user_profile}\n")
    except InvalidUserError as e:
        print(f"❌ User Error: {e}\n")
    except InvalidEmailError as e:
        print(f"❌ Email Error: {e}\n")
    except InvalidAgeError as e:
        print(f"❌ Age Error: {e}\n")


# Test Case 1: Empty Name
run_registration_pipeline("", "sam@example.com", 24)

# Test Case 2: Missing '@' in email
run_registration_pipeline("Sam", "invalid-email", 24)

# Test Case 3: Underage user
run_registration_pipeline("Sam", "sam@example.com", 15)

# Test Case 4: Overage user
run_registration_pipeline("Sam", "sam@example.com", 125)

# Test Case 5: Valid Registration
run_registration_pipeline("Sam", "sam@example.com", 24)
