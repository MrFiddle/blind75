import heapq


def frequencySort(str):
    sortedString = ""
    fqMap = {}
    for c in str:
        if c not in fqMap:
            fqMap[c] = 1
        else:
            fqMap[c] = fqMap[c] + 1

    heap = []

    for character, frequency in fqMap.items():
        heapq.heappush(heap, (-frequency, character))

    for i in range(len(heap)):

        character = heapq.heappop(heap)
        sortedString = sortedString + (abs(character[0]) * character[1])

    return sortedString


str = "Aabb"
print(frequencySort(str))
