def binary_search(arr, num, start, end):
    mid = int((start + end)/2)
    if arr[mid] == num:
        return mid
    elif arr[mid] < num:
        index = binary_search(arr, num, mid+1, end)
    elif arr[mid] > num:
        index = binary_search(arr, num, start, mid-1)
    return index

def rotate_binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while(low < high):
        mid = int((low+high)/2)
        if arr[mid] == target:
            return mid
        if arr[low] <= arr[mid]:
            if arr[low] <= target and arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target and arr[high] >= target:
                low = mid + 1
            else:
                high = mid -1
    return low if arr[low] == target else -1


arr = [1,2,3,4,5,6,7,8,9,10, 0]
# print(binary_search(arr, 6, 0, len(arr)-1))
print(rotate_binary_search(arr, 0))
