arr = [1,1,2,2,3,4,5]

seen = set()
duplicates = set()

for i in arr:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print(duplicates)