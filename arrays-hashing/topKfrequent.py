from collections import Counter
import heapq


def topKFrequent(nums, k):

    FqMap = {}

    for i in range(len(nums)):
        if nums[i] not in FqMap:
            FqMap[nums[i]] = 1
        else:
            FqMap[nums[i]] = FqMap[nums[i]] + 1

    topKElements = []

    for number, frequency in FqMap.items():
        heapq.heappush(topKElements, (frequency, number))

        if len(topKElements) > k:
            heapq.heappop(topKElements)

    return [tup[1] for tup in topKElements]


nums = [3, 2, 2, 2, 1, 1]
k = 2
print(topKFrequent(nums, k))
