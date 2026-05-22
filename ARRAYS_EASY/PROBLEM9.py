#NUMBER THAT APPEARS ONCE 
#HERE THE CONCEPT IF FOR GIVEN ARRAY
#FOR A ARRAY EVERY NUMBER APPEARS EXACTLY TWO TIMES
#ONLY ONE NUMBER APPEARS ONE TIME
#FIND THAT UNIQUE NUMBER

#BRUTE FORCE APPROACH
def single_number(arr):
    if len(arr)==0:
        return "EMPTY ARRAY"
    if len(arr)==1:
        return arr[0]
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        if count==1:
            return arr[i]
arr=[1,2,3,3,2]
print(single_number(arr))

#USING DICTIONARY AND HASH METHOD
def single_number(arr):
    if not arr:
        return "EMPTY ARRAY"
    if len(arr)==1:
        return arr[0]
    freq={}
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    for key in freq:
        if freq[key]==1:
            return key
    return "NO UNIQUE ELEMENTS"
arr=[1,2,3,3,2]
print(single_number(arr))

#USING XOR METHOD (BEST)
def single_number(arr):
    if not arr:
        return "EMPTY ARRAY"
    if len(arr)==1:
        return arr[0]
    result=0
    for num in arr:
        result^=num
    return result 
arr=[1,2,3,3,2]
print(single_number(arr))