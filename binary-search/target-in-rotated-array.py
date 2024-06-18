# Input: nums = [3,4,5,6,1,2], target = 1
# Output: 4

# Input: nums = [3,5,6,0,1,2], target = 4
# Output: -1

def search(nums, target):
    l, r = 0, len(nums) - 1
    res = -1

    while l < r:
        middle = l + (r - l) // 2
        if target == nums[middle]:
            res = middle
            break
        if target < nums[r]:
            l = middle + 1
        else:
            r = middle

    return res


def search(nums, target):
    l, r = 0, len(nums) - 1  # Initialize left and right pointers

    while l <= r:  # Continue until the search space is exhausted
        middle = l + (r - l) // 2  # Find the middle index
        if nums[middle] == target:  # If the middle element is the target
            return middle  # Return the index of the target

        # Determine if the left half is sorted
        if nums[l] <= nums[middle]:
            # Check if the target is in the range of the left half
            if nums[l] <= target < nums[middle]:
                r = middle - 1  # Move the right pointer to narrow down the search
            else:
                l = middle + 1  # Move the left pointer to narrow down the search
        # Determine if the right half is sorted
        else:
            # Check if the target is in the range of the right half
            if nums[middle] < target <= nums[r]:
                l = middle + 1  # Move the left pointer to narrow down the search
            else:
                r = middle - 1  # Move the right pointer to narrow down the search

    return -1  # Return -1 if the target is not found


nums = [2, 3, 4, 5, 6, 0, 1]
target = 0
# Expected output: 4

print(search(nums, target))
