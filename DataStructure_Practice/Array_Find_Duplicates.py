"""
Find the duplicate element in a limited range array
"""


def find_duplicates(A):
    dup_indicator = [False] * (len(A) + 1)
    print(dup_indicator)
    for num in A:
        dup_indicator[num]
        if dup_indicator[num]:
            return num
        dup_indicator[num] = True
    return -1

def findDuplicate(nums):
    actual_sum = sum(nums)
    expected_sum = len(nums) * (len(nums) - 1) // 2

    return actual_sum - expected_sum

if __name__ == '__main__':
    # input list contains `n` numbers between 1 and `n-1`
    # with one duplicate, where `n = len(nums)`
    nums = [1, 2, 3, 4, 5,6]
    print(findDuplicate(nums))
