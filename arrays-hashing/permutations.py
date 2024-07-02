from typing import List


def permute(nums):
    res = []  # Initialize the result list to store permutations

    # Base case: if there's only one element in nums, return it as the only permutation
    if len(nums) == 1:
        return [nums[:]]  # Return a copy of nums

    # Iterate over each element in nums
    for _ in range(len(nums)):
        n = nums.pop(0)  # Remove the first element
        perms = permute(
            nums
        )  # Recursive call to find permutations of the remaining elements

        # Append the removed element to each permutation of the remaining elements
        for perm in perms:
            perm.append(n)

        res.extend(perms)  # Add these new permutations to the result list
        nums.append(n)  # Restore the removed element back to nums

    return res  # Return the list of all permutations


print(permute([1, 2, 3]))
