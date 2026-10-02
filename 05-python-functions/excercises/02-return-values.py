# Exercise 4:
# Create a function add(a, b) that returns the sum of a and b.
# Do NOT print inside the function.
# Store the returned value in a variable and print it outside the function.
# Test the function with multiple inputs.

def add(a: int , b: int) -> int:
    '''return the sum of two numbers'''
    return (a+b)

sum = add(4,5)
print(f"the sum of 4 and 5 is {sum}")


# Exercise 5:
# Create show_square(number) that PRINTS the square.
# Create return_square(number) that RETURNS the square.
#
# Call both functions like:
# result1 = show_square(5)
# result2 = return_square(5)
#
# Print result1 and result2.
# Observe and explain the difference between print and return.

def show_square(num: int) -> None:
    '''Print the square of the num provided'''
    print(num**2)

def return_square(num: int) -> int:
    '''Return the square of the num provided'''
    return num**2

res1 = show_square(4)
res2 = return_square(4)
print(f"the output for show_square method is: {res1}\nThe output for return_square method is: {res2}")


# Exercise 6:
# Create is_even(number).
# Return True if the number is even.
# Return False if the number is odd.
# Do not print inside the function.
# Test it with positive, negative, and zero values.

def is_even(num: int) -> bool:
    '''return if the given num is even or not'''
    return num%2==0

print(is_even(2))
print(is_even(3))
print(is_even(-2))
print(is_even(0))
print(is_even(-3))

# Exercise 7:
# Create find_largest(a, b, c).
# Return the largest of the three numbers.
# Do NOT use the built-in max() function.
# Test cases should include:
# - three different values
# - two equal values
# - all three equal
# - negative numbers

def find_largest(a: int, b: int, c: int) -> int:
    '''return the largest number among given three numbers'''
    if a>=b and a>=c :
        return a
    elif b>=a and b>=c:
        return b
    return c

print(find_largest(2,3,4))
print(find_largest(2,2,2))
print(find_largest(-2,-3,-4))
