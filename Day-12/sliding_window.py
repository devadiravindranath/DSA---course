# sliding window approach for finding the maximum sum of a contiguous subarray of size k
def max_sum_subarray(arr, k):
    max_sum = 0
    window_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if i >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[i - k + 1]
    return max_sum
# Example usage
arr = [1, 2, 3, 4, 5]
k = 2
print(max_sum_subarray(arr, k)) 

#dry run:# arr = [1, 2, 3, 4, 5], k = 2
# i = 0: window_sum = 1, max_sum = 0    
# i = 1: window_sum = 3, max_sum = 3    
# i = 2: window_sum = 5, max_sum = 5    
# i = 3: window_sum = 7, max_sum = 7    
# i = 4: window_sum = 9, max_sum = 9    

#steps to find the maximum sum of a contiguous subarray of size k:
#1. Initialize max_sum and window_sum to 0. 
#2. Iterate through the array using a for loop.
#3. Add the current element to window_sum.
#4. If the current index is greater than or equal to k - 1, update max_sum if window_sum is greater than max_sum, and subtract the element that is sliding out of the window from window_sum.
#5. Return max_sum after the loop completes.    