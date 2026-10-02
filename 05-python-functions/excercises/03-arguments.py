# Exercise 8:
# Create greet(name="Guest").
# Calling greet() should print "Hello Guest".
# Calling greet("Sam") should print "Hello Sam".
# Test both cases.

def greet(name: str ="Guest") -> None:
    print(f"Hello {name}!")

greet("Samridhi")
greet()

# Exercise 9:
# Create calculate_price(price, tax_rate=0.18).
# The default tax rate should be 18%.
# Return the final price after applying tax.

def calculate_price(price: int, tax_rate: float=0.18) -> float:
    '''return the final price after applying the tax'''
    return (price*(1+tax_rate))

print(calculate_price(2000))
print(calculate_price(2000,0.30))


# Exercise 10:
# Create create_profile(name, age, city).
#
# Call it using positional arguments.
# Then call it using keyword arguments.
# Change the order of the keyword arguments.
# Verify that the function still receives the correct values.

def create_profile(name: str, age: int, city: str) -> None:
    '''printing the profile of a person with given name , age and city '''
    print(f"Name: {name}\nAge: {age}\nCity: {city}")

create_profile("Sam", 24, "Delhi")
create_profile(
    city="Delhi",
    name="Sam",
    age=24
)

create_profile(24, "Sam", "Delhi")


# Exercise 11:
# Create calculate_bill(item, price, quantity=1, discount=0).
#
# Calculate:
# subtotal = price * quantity
# discount_amount = subtotal * discount
# final_amount = subtotal - discount_amount
#
# Return the final amount.
#
# Test the function using:
# - only required arguments
# - positional optional arguments
# - keyword optional arguments
# - different discount values

def calculate_bill(item: str, price: int, quantity: int=1 , discount: float=0) -> float:
    '''return the final amount after discount'''
    subtotal: float = price*quantity
    discount_amount: float = subtotal*discount
    return subtotal - discount_amount

print(calculate_bill("Laptop", 50000))
print(calculate_bill("Laptop", 50000, 2))
print(calculate_bill("Laptop", 50000, quantity=2, discount=0.10))

# Exercise 11:
# Create calculate_bill(item, price, quantity=1, discount=0).
#
# Calculate:
# subtotal = price * quantity
# discount_amount = subtotal * discount
# final_amount = subtotal - discount_amount
#
# Return the final amount.
#
# Test the function using:
# - only required arguments
# - positional optional arguments
# - keyword optional arguments
# - different discount values