arr = [1,2,3,4,5]

prefix = [0] * len(arr)
prefix[0] = arr[0]
for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

print("Prefix Sum Array:", prefix)

l =1
r = 3
if l == 0:
    print(prefix[r])
else:
    print(prefix[r] - prefix[l-1])

#dry run approach for left = 1 and right = 3:

# prefix[3] - prefix[0] = 10 - 1 = 9