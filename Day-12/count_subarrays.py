def count_subarrays(arr,k):
    count = 0
    for i in range(len(arr)):
        if i>=k-1:
            count += 1
    return count
def main():
    arr = [1,2,3,4,5]
    k =2
    print("subarrays count:", count_subarrays(arr,k))
main()

#each line explains the code:
#1. Define a function named count_subarrays that takes two parameters: arr (the input array) and k (the size of the subarrays).
#2. Initialize a variable count to 0, which will be used to keep track of the number of subarrays of size k.
#3. Start a loop that iterates through the indices of the input array arr.  
#4. Inside the loop, check if the current index i is greater than or equal to k-1. This condition ensures that we have enough elements to form a subarray of size k.
#5. If the condition is true, increment the count variable by 1, indicating that we have found a valid subarray of size k.
#6. After the loop completes, return the count variable, which now contains the total number of subarrays of size k in the input array.
#7. Define a main function to demonstrate the usage of the count_subarrays function.    
#8. Inside the main function, create an example array arr and set the value of k to 2.
#9. Call the count_subarrays function with the example array and k, and print the result to the console.

#dry run:
#1. The function count_subarrays is defined, and it takes two parameters: arr and k.
#2. The variable count is initialized to 0. 
#3. The loop starts iterating through the indices of the array arr, which has 5 elements (1, 2, 3, 4, 5).
#4. When i = 0, the condition i >= k-1 (0 >= 1) is false, so count remains 0.
#5. When i = 1, the condition i >= k-1 (1 >= 1) is true, so count is incremented to 1.
#6. When i = 2, the condition i >= k-1 (2 >= 1) is true, so count is incremented to 2.
#7. When i = 3, the condition i >= k-1 (3 >= 1) is true, so count is incremented to 3.
#8. When i = 4, the condition i >= k-1 (4 >= 1) is true, so count is incremented to 4.
#9. After the loop completes, the count variable has a value of 4, which is returned by the function.
#10. The main function is defined, and it creates an example array arr with the values [1, 2, 3, 4, 5] and sets k to 2.
#11. The count_subarrays function is called with the example array and k, and the result (4) is printed to the console, indicating that there are 4 subarrays of size 2 in the input array.