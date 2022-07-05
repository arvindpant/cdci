"""
Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
"""

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l1_even = [x for x in l1 if l1.index(x) % 2 != 0]
l2_odd = [x for x in l2 if l2.index(x) % 2 == 0]
print(l1_even + l2_odd)

"""
List slicing is easiest way of finding odd and even element from the list
"""
l1_even_another = l1[1::2]
l2_odd_another = l2[0::2]
print(l1_even_another + l2_odd_another)
