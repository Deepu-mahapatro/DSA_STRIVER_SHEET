#TWO SUM PROBLEM
#YOU ARE GIVEN A ARRAY OF NUMBERS
#AND A TARGET OUR MAIN GOAL IS TO:
#BY  ADDING TWO NUMBERS IN THE ARRAY 
#THE SUM OF TWO NUMBERS MUST BE EQUAL TO TARGET

#USING BRUTE FORCE METHOD
def two_sum(num,target):
    n=len(num)
    #EDGE CASE: IF LESS THAN 2 ELEMENTS
    if n<2:
        return[]
    #CHECK EVERY POSSIBLE PAIR
    for i in range(n):
        for j in range(i+1,n):
            #PAIR FOUND
            if num[i]+num[j]==target:
                return [i,j]
    #IF NO SOLUTION FOUND
    return []
print(two_sum([1,2,3,4,5],7))

#USING HASHMAP METHOD
def two_sum(num,target):
    #DICTIONARY STORE 
    seen={}
    for i in range(len(num)):
        current=num[i]
        #FIND COMPLEMENT
        complement=target-current
        #EDGE CASE:
        #COMPLEMENTARY ALREADY EXISTS
        if complement in seen:
            return [seen[complement],i]
        #STORE THAT NUMBER
        seen[current]=i
    #EDGE CASE: NO PAIR FOUND
    return []
print(two_sum([1,2,3,4,5],7))

#USING TWO POINTER METHOD
def two_sum(num,target):
    left=0
    right=len(num)-1
    #EDGE CASE:
    if len(num)<2:
        return []
    while left<right:
        current_sum=num[left]+num[right]
        #PAIR FOUND
        if current_sum==target:
            return [left,right]
        #NEED BIGGER SUM
        elif current_sum < target:
            left+=1
        #NEED SMALLER SUM
        else:
            right-=1
    #NO PAIR FOUND
    return []
print(two_sum([1,2,3,4,5],7))
        