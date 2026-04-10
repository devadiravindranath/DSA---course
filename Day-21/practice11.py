# # # # def min_max(arr):
# # # #     min_val = arr[0]
# # # #     max_val = arr[0]

# # # #     for i in arr:
# # # #         if i < min_val:
# # # #             min_val = i

# # # #         if i > max_val:
# # # #             max_val = i
# # # #     print("maximum=",max_val)
# # # #     print("minimum=",min_val)

# # # # arr = [12,54,6,56,8,2]
# # # # min_max(arr)


# # # # #traversal of array=visiting each element of the array

# # # arr= [10,56,85,46,75,55]

# # # first = second = float('-inf')

# # # for num in arr:
# # #     if num > first:
# # #         second = first
# # #         first = num

# # #     elif num > second and num!=first:
# # #         second = num
# # # print("second largest = ",second)

# # matrix = [[1,2],[3,4]]

# # for i in range(len(matrix)):
# #     for j in range(len(matrix[0])):
# #         print(matrix[i][j])

# arr = [5, 3, 8, 2]
# key = 12

# for i in range(len(arr)):
#     if arr[i] == key:
#         print("found at index",i)
#         break

arr = [2, 5, 8, 12, 16, 23]
key = 2

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Found at index", mid)
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1