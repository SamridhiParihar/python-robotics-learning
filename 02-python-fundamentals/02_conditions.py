# Take the integer and determine whether it is odd or even 

def even_odd (var: int ) -> str : 
    if var % 2 == 0 :
        return "even"

    return "odd"

var: int = int(input("Enter the  no : "))

print (even_odd(var))


# Largest of the three no 

def largest_of_three(var1: int , var2: int , var3: int) -> int :
    if var1 > var2 and var1 > var3 : 
        return var1
    elif var2 > var1 and var2 > var3:
        return var2
    else : 
        return var3
    
var1 = int(input("Enter the first no : "))
var2 = int(input("Enter the second no : "))
var3 = int(input("Enter the first no : "))

print (f"the largest number among {var1}, {var2} and {var3} is : {largest_of_three(var1, var2, var3)}")




# grade calculator (your own custom logic)

def grade_calculator(marks: int) -> str:
    if marks > 100 or marks < 0 : 
        return "mark should be in range of 0-100"
    elif marks >= 90 :
        return "A"
    elif marks >= 80 and marks < 90:
        return "B"
    return "pass"

marks: int = int(input("Enter you marks please : "))

print(f"the grade you got for your marks({marks}/100) is : {grade_calculator(marks)} ")

