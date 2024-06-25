def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
    
    return -1


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 12

result = binarySearch(arr, target)
print("Element found at index:", result)
