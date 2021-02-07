from collections import defaultdict


def singleNumber(nums):
    no_duplicate_list = []
    for i in nums:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
        else:
            no_duplicate_list.remove(i)
    return no_duplicate_list.pop()


def singleNumberDict(nums):
    hash_table = defaultdict(int)
    for i in nums:
        hash_table[i] += 1

    for i in hash_table:
        if hash_table[i] == 1:
            return i


def singleNumberMath(nums):
    return 2 * sum(set(nums)) - sum(nums)


def singleNumberBit(nums):
    a = 0
    for i in nums:
        a ^= i
    return a


if __name__ == "__main__":
    # Example 1:
    # Input: nums = [2,2,1]
    # Output: 1
    print("Pass" if (singleNumber([2, 2, 1]) == 1) else "Fail")

    # Example 2:
    # Input: nums = [4,1,2,1,2]
    # Output: 4
    print("Pass" if (singleNumber([4, 1, 2, 1, 2]) == 4) else "Fail")

    # Example 3:
    # Input: nums = [1]
    # Output: 1
    print("Pass" if (singleNumber([1]) == 1) else "Fail")
