def first_occurence(arr,target):
    low = 0
    high = len(arr)-1
    result = -1

    while low <= high:
        mid = (low + high)//2
        
        if arr[mid] == target:
            result = mid
            high = mid - 1  

        elif target < arr[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return result


arr = [10,20,20,30]
target = 20
print("element found at index:", first_occurence(arr,target))