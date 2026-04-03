def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]   # choosing first element as pivot
    
    left = []
    right = []
    
    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    
    return quick_sort(left) + [pivot] + quick_sort(right)


# Example
list1 = [50, 20, 60, 10, 30, 40]

sorted_list = quick_sort(list1)

print("Sorted List:", sorted_list)