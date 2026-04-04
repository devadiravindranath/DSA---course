""" idea
- divide array into two halves
- recursively sort each half
- merge sorted halves
-key concept:always splits -->then merges in sorted order 
"""
def merge_sort(arr):
    if len(arr) > 1:
        
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # divide
        merge_sort(left)
        merge_sort(right)

        # merge
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Example
list1 = [50, 20, 60, 10, 30, 40]

merge_sort(list1)

print("Sorted List:", list1)