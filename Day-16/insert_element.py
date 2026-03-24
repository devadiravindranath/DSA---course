"""Start from second element
Store it as key
Compare with previous elements
Shift all greater elements to right
Insert key at correct position
Repeat till end"""

# inserting element in sorted array

"""def insert_into_sorted(arr, x):
    arr.append(0)
    i = len(arr) -2
    while i >=0 and arr[i] >x:
        arr[i+1] = arr[i]
        i -=1
    arr[i+1] = x
    return arr
arr = [1, 3, 5, 7]
x = 4
print(insert_into_sorted(arr, x))"""

n = 24

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")