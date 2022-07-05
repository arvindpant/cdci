"""
Find a pair with the given sum in an array
Input:
nums = [8, 7, 2, 5, 3, 1]
target = 10
Output:
Pair found (8, 2)
or
Pair found (7, 3)

Input:
nums = [5, 2, 6, 8, 1, 9]
target = 12
Output: Pair not found
"""


def findPair(A, target):

    # dictionary to store pairs
    dic = dict()

    # check whether pair exists in dictionary
    for i, e in enumerate(A):
        if target - e in dic:
            print(nums[dic.get(target-e)], nums[i])

        # store index of the element in the dictionary
        dic[e] = i


if __name__ == '__main__':
    nums = [8, 7, 2, 5, 3, 1]
    target = 10

    findPair(nums, target)
