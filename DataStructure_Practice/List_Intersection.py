"""
Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
Excepted result
Intersection is  {57, 83, 29}
First Set after removing common element  {65, 42, 78, 23}
"""

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

common_elements = first_set.intersection(second_set)
print("Intersection is ", common_elements)

for item in common_elements:
    first_set.remove(item)
print("First Set after removing common element ",first_set)