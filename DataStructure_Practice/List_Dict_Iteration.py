"""
Exercise 8: Iterate a given list and check if a given element exists
as a key’s value in a dictionary. If not, delete it from the list

Expected Output:
After removing unwanted elements from list [47, 69, 76, 97]
"""

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

roll_number_list = [roll for roll in roll_number if roll in sample_dict.values()]

print("After removing unwanted elements from list ",roll_number_list)

