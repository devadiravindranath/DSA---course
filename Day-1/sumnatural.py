# sum of first n numbers

def calculate_sum(n):
    total = 0
    
    for i in range(1,n+1):
        total=total+i
    return total
def main():
    n=int(input("enter no:"))
    print("sum:",calculate_sum(n))
    

main()
    
