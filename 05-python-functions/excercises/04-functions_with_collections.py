# Exercise 12:
# Create calculate_sum(numbers).
# Return the sum of all numbers in the list.
# Do NOT use the built-in sum() function.
# Use a loop.
# Test with:
# - normal list
# - empty list
# - negative numbers

def calculate_sum(numbers: list[int]) -> int:
    '''return the sum of all the numbers in the list'''
    sum = 0
    for num in numbers:
        sum+=num
    return sum

print(calculate_sum([1,2,3,4,5]))
print(calculate_sum([]))
print(calculate_sum([-1,-2,-3,-4,5]))



# Exercise 13:
# Create find_max(numbers).
# Return the largest value from the list.
# Do NOT use max().
# Decide how your function should behave for an empty list.
# Test normal, negative, duplicate, and single-element lists.

def find_max(numbers: list[int]) -> int:
    '''Return the largest number in the list. Raise ValueError if empty.'''
    # 1. Check if the list is empty
    if not numbers:
        raise ValueError("find_max() arg is an empty sequence")
    
    # 2. Logic to find the maximum
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
            
    return max_num

print(find_max([1,2,3,4,5]))
# print(find_max([]))
print(find_max([-1,-2,-3,-4,5]))
print(find_max([1,1,1,1]))
print(find_max([5]))



# Exercise 14:
# Create count_even(numbers).
# Return how many even numbers are present in the list.
# Do not modify the original list.
# Test with:
# - normal values
# - no even values
# - all even values
# - an empty list

def count_even(numbers: list[int]) -> int:
    '''Return the no of even numbers in the given list.'''
    even_count: int = 0
    for num in numbers:
        if num%2 ==0 :
            even_count+=1
    return even_count

print()
print(count_even([1,2,3,4,5,6,7,8,9,10]))
print(count_even([1,3,5,7]))
print(count_even([]))
print(count_even([2,4,6,8]))


# Exercise 15:
# Create get_positive_numbers(numbers).
# Return a NEW list containing only positive numbers.
# Do not modify the original list.
# Test with positive, negative, zero, and empty-list cases.

def get_positive_numbers(numbers: list[int]) -> list[int]:
    '''Return a new list containing only positive numbers'''
    positive_list: list[int] = []  # Correctly initialized as a list
    for num in numbers:
        if num > 0:  # Zero is not positive, so strict '>' is correct
            positive_list.append(num)
    return positive_list

print(get_positive_numbers([1, -2, 3, 0, -4, 5])) 
print(get_positive_numbers([0]))                  
print(get_positive_numbers([]))                 


# Exercise 16:
# Create count_words(words).
# Return a dictionary containing the frequency of every word.
#
# Example:
# ["python", "java", "python", "cpp", "java", "python"]
#
# should produce:
# {"python": 3, "java": 2, "cpp": 1}
#
# Handle an empty list.
def count_words(words: list[str]) -> dict[str, int]:
    '''Return a dictionary containing the frequency of every word'''
    word_counts: dict[str, int] = {}
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    return word_counts

print(count_words(["python", "java", "python", "cpp", "java", "python"]))
print(count_words([]))


