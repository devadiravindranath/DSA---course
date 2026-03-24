def insertion_sort(arr):
    count=0
    for i in range(1,len(arr)):
        key = arr[i]
        j=i-1

        while j>=0 and arr[j] >key:
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = key
        count +=1
    return arr,count
arr = [9,4,2,7]
print(insertion_sort(arr))

# i = 3
#key = arr[3] = 7
# j = i-1 = 2