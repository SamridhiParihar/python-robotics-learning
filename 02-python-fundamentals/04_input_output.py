# for given input predict the output and then compare it with the original output
# for code reading and reviewing purposes 

x = 10
y = "10"

print(x == y)
print(x is y)

if x:
    print("X")

if y:
    print("Y")

# expected answer: 
'''
    False
    False
    X
    Y
'''


# Review the code below : 
age=int(input("Enter age: "))
if age>=18:
 print("Adult")
else:
 print("Minor")

'''
    use methods to calcuate such decisions 
    use edge cases like age too big or less than 0
    
'''