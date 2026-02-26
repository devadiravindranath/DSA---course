def count_positive(numbers):
    count=0
    for num in numbers:
        if num>0:
            count +=1
    return count

def main():
    numbers = [1,2,-6,4]
    print("positive numbers: ",count_positive (numbers))

main()
