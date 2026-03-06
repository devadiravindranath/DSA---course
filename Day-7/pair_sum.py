def pair_sum(arr,target):
    for i in range(len(arr)):
        for j in range (i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False

def main():
    arr = [2,7,11,13]
    target= 24
    print("sol: ",pair_sum(arr,target))

main()

            
