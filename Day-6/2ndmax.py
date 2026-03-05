def find_sec(arr):
    first = arr[0]
    second = arr[0]

    for num in arr:
        if num > first:
            second = first
            first = num

        elif num > second and num !=first:
            second = num

    return second

def main():
    arr = [5,85,6,6,46,5,6]
    print('second highest number: ',find_sec(arr))

main()
    
