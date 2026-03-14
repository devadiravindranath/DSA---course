arr = [1,2,3,4,5]
seen = set()

duplicate = False
for num in arr:
    if num in seen:
        duplicate = True
        break
    seen.add(num)

if duplicate :
    print("duplicate present")
else:
    print("no duplicates")