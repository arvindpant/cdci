"""
Exercise 5: Create a Python set such that it shows the element from both lists in a pair
"""

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

"""
Use the zip() function. This function takes two or more iterables (like list, dict, string), 
aggregates them in a tuple, and returns it.
"""
pairs = ((item1,item2) for item1,item2 in zip(first_list,second_list) if item1*item1 == item2 )
print(set(pairs))
# OR
paired = zip(first_list,second_list)
print(set(paired))