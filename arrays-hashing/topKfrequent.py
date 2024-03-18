from collections import defaultdict

def topKFrequent(nums, k):

    nums_map = defaultdict(list)

    for i in range (len(nums)):
        nums_map[nums[i]].append(nums[i])

    sorted_keys = sorted(nums_map, key=lambda x: len(nums_map[x]), reverse=True)
    longest_lists_keys = sorted_keys[:k]
    return longest_lists_keys


nums = [1,1,1,2,2,2,2,3]
k = 1

print(topKFrequent(nums, k))