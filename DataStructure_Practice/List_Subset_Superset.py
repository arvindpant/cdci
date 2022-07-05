"""
Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
Excepted Output:
First set is subset of second set - True
Second set is subset of First set -  False

First set is Super set of second set -  False
Second set is Super set of First set -  True

First Set  set()
Second Set  {67, 73, 43, 48, 83, 57, 29}
"""

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
print("First set is subset of Second set - ",first_set.issubset(second_set))
print("Second set is subset of First set - ",second_set.issubset(first_set))

print("First set is Super set of Second set - ",first_set.issuperset(second_set))
print("Second set is Super set of First set - ",second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()
if second_set.issubset(first_set):
    second_set.clear()
print("First Set ",first_set)
print("Second Set ",second_set)