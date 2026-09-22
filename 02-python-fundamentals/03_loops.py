# take a number and print mul table using for loop upto 10
def print_mul_table (num: int) -> None:
    print(f"\nMultiplication table of {num} is : ")
    for i in range (1,11,1):
        print(f"{num} * {i} = {num*i}")
    

num: int = int(input("enter a number please : "))

print_mul_table(num)

# calculate sum of number from 1 to n (1+2....n)
def sum_of_numbers(num: int) -> int : 
    sum: int = 0
    for i in range(1,num+1,1):
        sum+= i

    return sum

print()
num2: int = int(input("enter the number for sum : "))
print(f"the sum of numbers from 1 to {num2} is : {sum_of_numbers(num2)}")


# calculate the number of digits 

def count_digits (num: int) -> int :
    if num == 0 : 
        return 1
    
    num = abs(num)
    digit = 0

    while num :
        digit+=1
        num//=10
        print(digit)
    return digit

print()
num3: int = int(input("enter the number for digit count : "))

print (f"the digit count for {num3} is {count_digits(num3)}")