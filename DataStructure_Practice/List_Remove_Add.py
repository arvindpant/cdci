"""
Exercise 2: Remove and add item in a list
List After removing element at index 4  [34, 54, 67, 89, 43, 94]
List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
"""
list1 = [54, 44, 27, 79, 91, 41]

list1.pop(4)
print(list1)

list1.insert(2,11)
print(list1)

list1.append(11)
print(list1)
