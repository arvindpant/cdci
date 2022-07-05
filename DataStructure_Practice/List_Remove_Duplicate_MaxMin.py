"""
Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
Expected Output:
unique items [87, 45, 41, 65, 99]
tuple (87, 45, 41, 65, 99)
min: 41
max: 99
"""

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
print("unique items ",list(set(sample_list)))
print("tuple ",tuple(set(sample_list)))
print("min: ",min(sample_list))
print("max: ",max(sample_list))
