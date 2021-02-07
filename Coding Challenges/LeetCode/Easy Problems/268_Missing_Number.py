def missingNumber(nums):
    nums.sort()

    # Ensure that n is at the last index
    if nums[-1] != len(nums):
        return len(nums)
    # Ensure that 0 is at the first index
    elif nums[0] != 0:
        return 0

    # If we get here, then the missing number is on the range (0, n)
    for i in range(1, len(nums)):
        expected_num = nums[i - 1] + 1
        if nums[i] != expected_num:
            return expected_num


def missingNumberSet(nums):
    num_set = set(nums)
    n = len(nums) + 1
    for number in range(n):
        if number not in num_set:
            return number


def missingNumberBit(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        print(i, num)
        missing ^= i ^ num
        print(missing)
    return missing


def missingNumberGauss(self, nums):
    expected_sum = len(nums) * (len(nums) + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


if __name__ == "__main__":
    # Example 1:
    # Input: nums = [3,0,1]
    # Output: 2
    print("Pass" if (missingNumberBit([3, 0, 1]) == 2) else "Fail")

    # Example 2:
    # Input: nums = [0,1]
    # Output: 2
    print("Pass" if (missingNumber([0, 1]) == 2) else "Fail")

    # Example 3:
    # Input: nums = [9,6,4,2,3,5,7,0,1]
    # Output: 8
    print(
        "Pass" if (missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8) else "Fail"
    )

    # Example 4:
    # Input: nums = [0]
    # Output: 1
    print("Pass" if (missingNumber([0]) == 1) else "Fail")
