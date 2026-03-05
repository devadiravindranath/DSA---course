#arrays

#collection of elements
# storing in continous memory
#in pyhton ,we are defining array by using list

#sorting sum of array elements

def find_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

def main():
    arr = [1,2]
    print("sum: ",find_sum(arr))
main()
