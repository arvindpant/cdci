"""
Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates

Expected Output:
[47, 52, 44, 53, 54]
"""

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

output_list = []

for value in speed.values():
    if value not in output_list:
        output_list.append(value)

print(output_list)