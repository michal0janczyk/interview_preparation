def missingNumber(nums):



if __name__ == "__main__":
    # Example 1:
    # Input: nums = [3,0,1]
    # Output: 2
    print("Pass" if (missingNumber([3, 0, 1]) == 2) else "Fail")

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
