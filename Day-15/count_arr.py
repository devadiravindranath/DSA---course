def bubble_sort(arr):
    n = len(arr)
    swap_count = 0

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                swap_count += 1

        if not swapped:
            break

    return swap_count


arr = [9, 8, 7, 4, 5, 6]
print(bubble_sort(arr))
