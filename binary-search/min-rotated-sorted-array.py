# You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

# Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

# A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?


# Test case with negative numbers too
nums = [-3, -2, -1, 0, 1, 2, 3]

# Test case with only positive numbers
nums = [1, 2, 3, 4, 5, 6]


nums = [3, 4, 5, 6, 1, 2]
##################
nums = [6, 1, 2, 3, 4, 5]
nums = [-2, -1, 0, 1, 2, 3, -3]


def findMin(nums):
    # Initialize the left and right pointers
    left, right = 0, len(nums) - 1

    # Perform binary search
    while left < right:
        # Calculate the middle index
        mid = left + (right - left) // 2

        # Check if the middle element is less than the right element
        if nums[mid] < nums[right]:
            # If true, the minimum element is in the left half
            right = mid
        else:
            # If false, the minimum element is in the right half
            left = mid + 1

    # Return the minimum element
    return nums[left]
