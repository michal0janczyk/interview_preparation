def findDisappearedNumbers(nums):
    for i in range(0, len(nums)):
        temp = abs(nums[i]) - 1
        if nums[temp] > 0:
            nums[temp] *= -1
    res = []
    for i, n in enumerate(nums):
        if n > 0:
            res.append(i + 1)

    return res


if __name__ == "__main__":
    # Example 1:
    # Input: nums = [4,3,2,7,8,2,3,1]
    # Output:[5,6]
    print(
        "Pass"
        if (findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6])
        else "Fail"
    )

    # Example 2:
    # Input: nums = [1,1]
    # Output:[2]
    print("Pass" if (findDisappearedNumbers([1, 1]) == [2]) else "Fail")
