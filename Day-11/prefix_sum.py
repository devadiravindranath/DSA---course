# # prefix sum is a technique used in computer science to efficiently calculate the sum of elements in a subarray. It involves creating an array where each element at index i contains the sum of all elements from the original array up to index i. This allows for constant time complexity when calculating the sum of any subarray, as it can be done by subtracting the prefix sum at the starting index from the prefix sum at the ending index.Here is an implementation of the prefix sum technique in Python.
# prefix[0] = 2+4 = 6
# prefix[1] = prefix 2+4+6 = 12
# prefix[2] = prefix[2+4+6+8] = 20
# prefix[3] = prefix[2+4+6+8+10] = 30

# # formula: prefix[i] = prefix[i-1] + arr[i]
# to find the sum of a subarray from index l to r, we can use the formula: sum = prefix[r] - prefix[l-1]
# building the prefix sum array
arr = [1,2,3,4,5]

prefix = [0] * len(arr)
prefix[0] = arr[0]
for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

print("Prefix Sum Array:", prefix)
# dry run approach:
# prefix[0] = 1
# prefix[1] = prefix[0] + arr[1] = 1 + 2 = 3
# prefix[2] = prefix[1] + arr[2] = 3 + 3 = 6
# prefix[3] = prefix[2] + arr[3] = 6 + 4 = 10
# prefix[4] = prefix[3] + arr[4] = 10 + 5 = 15      