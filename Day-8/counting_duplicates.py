#counting duplicates

def counting_duplicates(arr):
    seen = set()

    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

def main():
    arr = [1,0,3,4]
    print("Are dulicate found: ",counting_duplicates(arr))

main()


"""i=1
seen=(1)

i=2
seen =(1,1)
1 in 1 sooo it is a true"""
