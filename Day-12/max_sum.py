def max_sum_subarray(arr,k):
    window_Sum=0
    max_Sum=0
    for i in range(len(arr)):
        window_Sum+=arr[i]
        if i >= k-1:
            max_Sum=max(max_Sum,window_Sum)
            window_Sum-=arr[i-k+1]
    return max_Sum
def main():
    arr=[2,1,5,1,3,2]
    k=3
    result = max_sum_subarray(arr,k)
    print("max sum of subarray of size k:", result)
main()
#each line explains the code:
#1. Define a function named max_sum that takes two parameters: arr (the input array) and k (the size of the subarrays).
#2. Initialize a variable window_sum to 0, which will be used to keep track of the sum of the current window of size k.
#3. Initialize a variable max_sum to 0, which will be used to keep track of the maximum sum found among all subarrays of size k.
#4. Start a loop that iterates through the indices of the input array arr.      
#5. Inside the loop, add the current element arr[i] to window_sum, which updates the sum of the current window.
#6. Check if the current index i is greater than or equal to k-1. This condition ensures that we have enough elements to form a complete window of size k.
#7. If the condition is true, update max_sum to be the maximum of the current max_sum and the current window_sum. This step checks if the current window has a larger sum than the previously recorded maximum.
#8. After updating max_sum, subtract the element that is sliding out of the window (arr[i-(k-1)]) from window_sum. This step prepares window_sum for the next iteration by removing the contribution of the element that is no longer in the current window.
#9. After the loop completes, return the max_sum variable, which now contains the maximum sum of any subarray of size k in the input array.
#10. Define a main function to demonstrate the usage of the max_sum function.   
#11. Inside the main function, create an example array arr and set the value of k to 3.
#12. Call the max_sum function with the example array and k, and print the result to the console, indicating the maximum sum of subarrays of size k in the input array
#dry run:
#1. The function max_sum is defined, and it takes two parameters: arr and k
#2. The variable window_sum is initialized to 0, and max_sum is also initialized to 0.
#3. The loop starts iterating through the indices of the array arr, which has 6 elements (2, 1, 5, 1, 3, 2).
#4. When i = 0, window_sum is updated to 2 (0 + 2). The condition i >= k-1 (0 >= 2) is false, so max_sum remains 0.
#5. When i = 1, window_sum is updated to 3 (2 + 1). The condition i >= k-1 (1 >= 2) is false, so max_sum remains 0.
#6. When i = 2, window_sum is updated to 8 (3 + 5). The condition i >= k-1 (2 >= 2) is true, so max_sum is updated to 8 (max(0, 8)). Then, window_sum is updated to 6 (8 - 2) by subtracting the element that is sliding out of the window.
#7. When i = 3, window_sum is updated to 7 (6 + 1). The condition i >= k-1 (3 >= 2) is true, so max_sum remains 8 (max(8, 7)). Then, window_sum is updated to 5 (7 - 1) by subtracting the element that is sliding out of the window.
#8. When i = 4, window_sum is updated to 8 (5 + 3). The condition i >= k-1 (4 >= 2) is true, so max_sum remains 8 (max(8, 8)). Then, window_sum is updated to 7 (8 - 5) by subtracting the element that is sliding out of the window.
#9. When i = 5, window_sum is updated to 9 (7 + 2). The condition i >= k-1 (5 >= 2) is true, so max_sum is updated to 9 (max(8, 9)). Then, window_sum is updated to 6 (9 - 1) by subtracting the element that is sliding out of the window.
#10. After the loop completes, the max_sum variable has a value of 9, which is returned by the function.
#11. The main function is defined, and it creates an example array arr with the values [2, 1, 5, 1, 3, 2] and sets k to 3.
#12. The max_sum function is called with the example array and k, and the result (9) is printed to the console, indicating that the maximum sum of any subarray of size 3 in the input array is 9.  
    