arr = [1, 2, 3, 4, 5]
k= 9
prefix=0
seen = set()
for num in arr:
    prefix += num
    if prefix== k or prefix-k in seen:
        print("Subarray with sum", k, "exists.")
        break
    seen.add(prefix)

    #dry run approach:
    # prefix = 1, seen = {1}
    # prefix = 3, seen = {1, 3}
    # prefix = 6, seen = {1, 3, 6}
    # prefix = 10, seen = {1, 3, 6, 10}
    # prefix - k = 10 - 9 = 1, which is in seen
    # Subarray with sum 9 exists.