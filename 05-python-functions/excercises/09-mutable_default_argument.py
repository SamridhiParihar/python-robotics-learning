# Exercise 32:
# Given:
#
# def add_item(item, items=[]):
#     items.append(item)
#     return items
#
# Call:
# print(add_item("A"))
# print(add_item("B"))
# print(add_item("C"))
#
# Observe the unexpected behavior.
#
# Explain why it happens.
#
# Then fix the function using None as the default value.

def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("A"))
print(add_item("B"))
print(add_item("C"))

# it actully will add in the same list ?
# In Python, default arguments are evaluated only once when the function is first defined, not every time the function is called.


def add_item(item: str, items: list[str] | None = None) -> list[str]:
    '''Safely add an item to a list without sharing state across calls'''
    if items is None:
        items = [] # Creates a fresh list object unique to this call
        
    items.append(item)
    return items

print(add_item("A"))  # Output: ['A']
print(add_item("B"))  # Output: ['B'] (Fresh list!)
print(add_item("C"))  # Output: ['C']

my_custom_list = ["X", "Y"]
print(add_item("Z", my_custom_list))  
