def sum_subarrays(arr,k):
    window_sum = 0
    result = []
    for i in range(len(arr)):
        window_sum += arr[i]
        if i >= k-1:
            result.append(window_sum/k)
            window_sum -= arr[i-(k-1)]

    return result

def main():
    arr= [1,2,3,4,5]
    k=3
    print("average subarray :",sum_subarrays(arr,k))

main()