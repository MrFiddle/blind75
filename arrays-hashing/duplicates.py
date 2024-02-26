nums = [1, 2, 3, 4]

def isThereAnyDuplicates(nums):

    # hashset = set()

    # for n in nums:
    #     if n in hashset:
    #         return True
    #     hashset.add(n)

    # return False

    hashset = set(nums)

    if len(hashset) != len(nums):
        return True
    else:
        return False

if isThereAnyDuplicates(nums):
    print("Duplicates found!")
else:
    print("All good :D")
