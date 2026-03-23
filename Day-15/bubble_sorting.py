# 1-one of the simplest sorting algirithm
# 2-it works by repeatedly comparing adjacent elements and swapping them if they are in a wrong order

# how it works
# 1- compare 1st and 2nd element--> swap if needed
# 2- move to the next pair
# 3- after one full pair --> largest element reaches the end
# 4- repeat for remaining elements
 
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


arr = [9, 8, 7, 4, 5, 6]
print(bubble_sort(arr))