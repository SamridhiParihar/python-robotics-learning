# basic list operations 

#1. Create a list containing five numbers.
# 
# Perform:
# - Print the first element.
# - Print the last element.
# - Add a number.
# - Remove a number.
# - Print the length.
# - Check whether a particular number exists.

numbers: list = [10, 20, 30, 40, 50]
print(f"first element is {numbers[0]}")
print (f"last element is {numbers[-1]}")
numbers.append(88)
numbers.remove(20)
print(f"the length of the list now is {len(numbers)}")

num: int = int(input("enter the number for which you wanna check the membership "))
if num in numbers:
    print(f"yes {num} exist in {numbers}")
else:
    print(f"sorry {num} doesn't exist in {numbers}")



# finding maximum , minimun manually 
numbers = [10, 45, 23, 67, 12, 89, 34]

maxi: int= numbers[0]
for num in numbers:
    if num > maxi:
        maxi = num 

print(f"the maximum number among the {numbers} is {maxi}")


# removing duplicate elements 
# i> by using set ( a unique set values )
# ii> by preserving the order ()

nums: list[int] = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_nums: set[int] = set(nums)
print(f"unique numbers are {unique_nums}")

seen: set[int] = set()
unique_odered: list[int] = []
for num in nums:
    if num not in seen:
        unique_odered.append(num)
        seen.add(num)

print(f"unique numbers after preserving the order are {unique_odered}")


# sudent dictionary and then perform :
# Print the name.
# Update the marks.
# Add a city.
# Check whether "email" exists.
# Use .get() to retrieve the email safely.

student = {
    "name" : "samridhi",
    "age" : 20,
    "marks": 98
}

print(f"student name is {student["name"]}")
student["marks"]=99
student["city"] = "Saharsa"
if "email" in student:
    print("email exists!")

email: str = student.get("email","does not exist")
print(email)



# student records 
students: list[dict] = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 92},
    {"name": "Charlie", "marks": 78},
    {"name": "David", "marks": 95}
]

# 1. Assume the first student in the list has the highest marks to start with
best_student = students[0]

# 2. Loop through every student in the list
for student in students:
    # If we find a student with more marks than our current best, update our variable
    if student["marks"] > best_student["marks"]:
        best_student = student

# Print the final result
print(f"The student with the highest marks is {best_student['name']} with {best_student['marks']} marks.")


best_student: dict = max(students, key=lambda student: student["marks"])

# Now you can print the whole dictionary, or pull specific parts out of it!
print(best_student)  
print(f"The top score is {best_student['marks']} by {best_student['name']}.")


# word frequency 
words = [
    "python",
    "java",
    "python",
    "cpp",
    "java",
    "python"
]
word_freq = {}
for word in words :
    if word not in word_freq:
        word_freq[word] = 1
    else :
        word_freq[word] = word_freq[word]+1

print(word_freq)


#sum of all values using loop 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

ans: int = 0
for lst in matrix:
    for num in lst :
        print(num , end=" ")
        ans+=num
    print()

print(f"the sum is {ans}")