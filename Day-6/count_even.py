def count_even(arr):
    count = 0

    for num in arr:
        if num % 2 ==0 :
            count += 1
    return count

def main():
    arr = [5,85,6,6,46,5,6]
    print('count of evena: ',count_even(arr))

main()
    
