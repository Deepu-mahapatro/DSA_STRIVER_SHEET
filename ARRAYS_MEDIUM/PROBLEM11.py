# MAJORITY ELEMENT-I
# THE PURPOSE OF MAJORITY ELEMENT IS:
# TO FIND THE ELEMENT THAT APPEARS
# MORE THAN N/2 TIMES IN THE ARRAY.
# DEFINITION:
# MAJORITY ELEMENT FREQUENCY > N/2
# EXAMPLE:
# [2,2,1,1,1,2,2]
# 2 APPEARS 4 TIMES
# ARRAY SIZE = 7
# 4 > 7/2
# ANSWER = 2
# KEY OBSERVATION:
# THERE CAN BE ONLY ONE MAJORITY ELEMENT.
# TWO DIFFERENT ELEMENTS CANNOT BOTH
# APPEAR MORE THAN N/2 TIMES.
# PROCESS (BRUTE FORCE):
# CHECK EVERY ELEMENT.
# COUNT ITS FREQUENCY.
# IF FREQUENCY > N/2
# RETURN THAT ELEMENT.
# PROCESS (HASH MAP):
# STORE FREQUENCY OF EACH ELEMENT.
# TRAVERSE FREQUENCY MAP.
# FIND ELEMENT WITH COUNT > N/2.
# RETURN THAT ELEMENT.
# PROCESS (SORTING):
# SORT THE ARRAY.
# MAJORITY ELEMENT MUST OCCUPY
# THE MIDDLE POSITION.
# RETURN nums[n//2].
# PROCESS (BOYER MOORE):
# KEEP A CANDIDATE.
# KEEP A COUNT.
# SAME ELEMENT -> INCREASE COUNT.
# DIFFERENT ELEMENT -> DECREASE COUNT.
# WHEN COUNT BECOMES 0:
# PICK NEW CANDIDATE.
# FINAL CANDIDATE IS MAJORITY ELEMENT.
# WHY BOYER MOORE WORKS:
# MAJORITY ELEMENT APPEARS MORE THAN
# ALL OTHER ELEMENTS COMBINED.
# DIFFERENT ELEMENTS CANCEL EACH OTHER.
# MAJORITY ELEMENT ALWAYS SURVIVES.
# CANCELLATION EXAMPLE:
# [2,2,1,1,1,2,2]
# 2 CANCELS 1
# 2 CANCELS 1
# 2 CANCELS 1
# REMAINING ELEMENT = 2
# IMPORTANT RULES:
# MAJORITY ELEMENT COUNT > N/2
# ONLY ONE MAJORITY ELEMENT CAN EXIST
# MAJORITY ELEMENT ALWAYS SURVIVES CANCELLATION
# EDGE CASES:
# ARRAY SIZE = 1
# ALL ELEMENTS SAME
# MAJORITY AT START
# MAJORITY AT END
# NEGATIVE NUMBERS
# LARGE INPUT SIZE
# EMPTY ARRAY (IF ALLOWED)
# COMPLEXITIES:
# BRUTE FORCE
# TIME  : O(N²)
# SPACE : O(1)
# HASH MAP
# TIME  : O(N)
# SPACE : O(N)
# SORTING
# TIME  : O(N LOG N)
# SPACE : O(1) OR O(N)
# BOYER MOORE
# TIME  : O(N)
# SPACE : O(1)
# FINAL IDEA:
# MAJORITY ELEMENT APPEARS MORE THAN N/2 TIMES.
# USE BOYER MOORE VOTING ALGORITHM
# TO CANCEL NON-MAJORITY ELEMENTS.
# THE SURVIVING CANDIDATE IS THE ANSWER.

#BRUTE FORCE APPROACH
def majority_element(nums):
    #EDGE CASE
    if not nums:
        return []
    n=len(nums)
    #CHECK EVERY ELEMENT 
    for num in nums:
        count=0
        #COUNT FREQUENCY
        for element in nums:
            if element==num:
                count+=1
        #MAJORITY ELEMENT FOUND
        if count>n//2:
            return num
nums=[3,3,2]
print(majority_element(nums))

#USING HASH MAP FREQUENCY COUNT METHOD
def majority_element(nums):
    #EDGE CASE 
    if not nums:
        return []
    n=len(nums)
    freq={}
    #BUILD FREQUENCY MAP
    for num in nums:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    #FIND MAJORITY ELEMENT
    for num,count in freq.items():
        if count>n//2:
            return num
nums=[3,2,3]
print(majority_element(nums))

#USING SORTING METHOD
def majority_element(nums):
    #EDGE CASE 
    if not nums:
        return []
    nums.sort()
    #MIDDLE ELEMENT
    return nums[len(nums)//2]
nums=[3,2,3]
print(majority_element(nums))

#USING DEFAULTDICT METHOD
from collections import defaultdict
def majority_element(nums):
    #EDGE CASE
    if not nums:
        return []
    n=len(nums)
    freq=defaultdict(int)
    #COUNT FREQUENCY
    for num in nums:
        freq[num]+=1
    #FIND MAJORITY ELEMENT
    for num,count in freq.items():
        if count>n//2:
            return num
nums=[3,2,3]
print(majority_element(nums))  


#BOYER MOORE VOTING ALGORITHM METHOD
def majority_element(nums):
    #EDGE CASE
    if not nums:
        return []
    candidate=0
    count=0
    #NO ACTIVE CANDIDATE
    for num in nums:
        if count==0:
            candidate=num
        #SAME AS CANDIDATE
        if num==candidate:
            count+=1
        #DIFFERENT ELEMENT
        else:
            count-=1
    return candidate
nums=[3,2,3]
print(majority_element(nums))