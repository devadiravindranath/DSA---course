"""def find_max(arr):
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum

def main():
    arr = [1,22,33,44]
    print("maximum number: ",find_max(arr))

main()"""

def find_min(arr):
    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
    return minimum

def main():
    arr = [1,22,33,44]
    print("minumum number: ",find_min(arr))

main()
