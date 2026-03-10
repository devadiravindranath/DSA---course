def two_sum_indices(arr,target):
    hashmap = {}
    for i,num in enumerate(arr):
        diff = target - num
        if diff in hashmap:
            return hashmap[diff],i
        hashmap[num]= i
    return None
def main():
    arr = [2,7,11,13]
    target = 24
    print("indexes:",two_sum_indices(arr,target))

main()
               
