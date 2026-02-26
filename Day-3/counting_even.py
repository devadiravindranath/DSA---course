
# counting even numbers from 1 to n
"""def count_even(n):
    count = 0
    for i in range(1,n+1):
        if i % 2==0:
            count +=1
    return count

def main():
    n=int(input("enter the number: "))
    print("Even count: ",count_even(n))
main()"""

#counting odd numbers 1 to n

def count_odd(n):
    count = 0
    for i in range(1,n+1):
        if i % 2==1:
            count +=1
    return count

def main():
    n=int(input("enter the number: "))
    print("Odd count: ",count_odd(n))
main()


