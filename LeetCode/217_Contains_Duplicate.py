def containsDuplicate(nums):
    num_values = dict()
    # counter = 0
    for i in range(0, len(nums)):
        # print("Counter: ", counter)
        # print(nums[i])
        # print(num_values.values())
        # print(num_values.keys())
        if nums[i] in num_values:
            # print("Found: ", nums[i])
            return True
        else:
            # print("Added: ", nums[i])
            num_values[nums[i]] = 1
        # counter += 1
    return False


if __name__ == "__main__":
    # Example 1:
    # Input: [1,2,3,1]
    # Output: true
    print("Pass" if (containsDuplicate([1, 2, 3, 1]) == True) else "Fail")

    # Example 2:
    # Input: [1,2,3,4]
    # Output: false
    print("Pass" if (containsDuplicate([1, 2, 3, 4]) == False) else "Fail")

    # Example 3:
    # Input: [1,1,1,3,3,4,3,2,4,2]
    # Output: true
    print(
        "Pass"
        if (containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True)
        else "Fail"
    )

    # Example 1:
    # Input: [3,3]
    # Output: true
    print("Pass" if (containsDuplicate([3, 3]) == True) else "Fail")
