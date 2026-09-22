# take personal information from user and print it

name = input("enter your name please : ")

age = int(input("enter your age please : "))

city = input("enter your city please : ")

print(f"Hello, {name}. \nYou are {age} years old. \nYou live in {city}. ")



# Take two integers and print sum , difference , ...... Remainder 

var1 = int(input("Enter the first no : "))
var2 = int(input("Enter the second no : "))

print (f"sum is : {var1+var2}")
print (f"diff is : {var1-var2}")
print (f"prod is : {var1*var2}")
print (f"div is : {var1/var2}")
print (f"Integer div is : {var1//var2}")
print (f"Remainder is : {var1%var2}")