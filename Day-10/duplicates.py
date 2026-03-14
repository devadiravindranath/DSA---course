#duplicate elements : are the values taht appear more than once
#dictinct element : are the value appear apear once
# approache using using hashing dictionary
#steps: 1)create an empty dictionary
        #2)count freq of each number
        #3)if frequency == 1 --> dictinct
        #4)if freq > 1 -->duplicate
# arr = [1,2,2,3,4,4,]
# freq = {}
# for num in arr:
#     if num in freq:
#         freq[num]=1
#     else:
#         freq[num]=1
# print(freq)
arr=[1,2,2,3,4,4,5]
distinct=set(arr)
print(distinct)