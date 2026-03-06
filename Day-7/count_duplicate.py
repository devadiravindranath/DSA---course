def count_duplicates(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                count +=1
            
    return count
def main():
     arr = [2, 11, 7, 7, 2, 11, 15]
     print("duplicates:" ,count_duplicates(arr))
main()
