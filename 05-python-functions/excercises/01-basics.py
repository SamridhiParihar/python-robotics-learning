# Exercise 1:
# Create a function called greet() that prints "Hello, Python!".
# Call the function three times.

def greet () -> None :
    print ("Hello Python")

greet()
greet()
greet()

# Exercise 2:
# Create a function greet_user(name).
# The function should print "Hello, <name>!".
# Call it with at least three different names.

def greet_user(name: str) -> None:
    print (f"Hello, {name}")

greet_user("Samridhi")
greet_user("Parihar")
greet_user("Sam")

# Exercise 3:
# Create a function introduce(name, age, profession).
# Print the name, age, and profession in a readable format.
# Do not hardcode these values inside the function.
# Call the function with at least three different sets of values.
def introduce (name: str, age: int , profession: str) -> None :
    print(f"Name: {name}\nAge: {age}\nProfession: {profession}")
    

introduce("Samridhi Parihar",24,"RA")
introduce("Sam Parihar", 23 , "SDE")
introduce("Sam",22, "Student")


