#LONGEST CONSECUTIVE SEQUENCE

#THE PURPOSE OF LONGEST CONSECUTIVE SEQUENCE IS:
#TO FIND THE LENGTH OF THE LONGEST GROUP OF NUMBERS
#THAT APPEAR CONSECUTIVELY (DIFFERENCE OF 1).

#PROCESS:
#CONVERT ARRAY INTO A SET FOR FAST LOOKUPS.
#TRAVERSE EACH NUMBER IN THE SET.
#CHECK WHETHER CURRENT NUMBER IS THE START OF A SEQUENCE.
#A NUMBER IS STARTING POINT IF:
#(NUMBER - 1) IS NOT PRESENT IN THE SET.
#IF IT IS A STARTING POINT:
#KEEP CHECKING NUMBER+1, NUMBER+2, NUMBER+3...
#COUNT THE LENGTH OF THAT CONSECUTIVE SEQUENCE.
#UPDATE MAXIMUM LENGTH FOUND SO FAR.
#CONTINUE UNTIL ALL NUMBERS ARE PROCESSED.
#RETURN MAXIMUM LENGTH.

#CONDITION:
#CURRENT NUMBER IS A STARTING POINT IF:
#(NUMBER - 1) NOT IN SET

#IMPORTANT RULES:
#USE SET FOR O(1) LOOKUP.
#ONLY START COUNTING FROM TRUE STARTING POINTS.
#AVOID RECOUNTING SAME SEQUENCE MULTIPLE TIMES.
#TRACK LONGEST LENGTH THROUGHOUT TRAVERSAL.

#WHY THIS WORKS:
#EVERY CONSECUTIVE SEQUENCE HAS EXACTLY ONE STARTING POINT.
#BY STARTING ONLY THERE, EACH SEQUENCE IS PROCESSED ONCE.
#THIS ELIMINATES REDUNDANT WORK AND GIVES O(N) TIME.

#EDGE CASES:
#EMPTY ARRAY -> ANSWER IS 0
#SINGLE ELEMENT -> ANSWER IS 1
#ALL DUPLICATES -> ANSWER IS 1
#NO CONSECUTIVE NUMBERS -> ANSWER IS 1
#ALREADY CONSECUTIVE ARRAY -> ANSWER IS ARRAY LENGTH
#NEGATIVE NUMBERS -> WORKS NORMALLY
#MIXED POSITIVE AND NEGATIVE -> WORKS NORMALLY

#FINAL IDEA:
#FIND ONLY THE NUMBERS THAT CAN START A CONSECUTIVE SEQUENCE,
#EXPAND FORWARD UNTIL THE SEQUENCE BREAKS,
#AND KEEP TRACK OF THE LONGEST LENGTH FOUND.

#USING BRUTE FORCE APPROACH
def longest_consecutive(nums):
    #EDGE CASE: 
    if not nums:
        return 0
    longest=0
    for num in nums:
        current=num
        length=1
        while current+1 in nums:
            current +=1
            length+=1
        longest=max(longest,length)
    return longest
nums=[1,100,2,4,5,3]
print(longest_consecutive(nums))

#SORTING APPROACH
def longest_consecutive(nums):
    #EDGE CASE:
    if not nums:
        return 0
    nums.sort()
    longest=1
    current_length=1
    for i in range(1,len(nums)):
        #SKIP DUPLICATES
        if nums[i]==nums[i-1]:
            continue
        #CONSECUTIVE NUMBERS
        elif nums[i]==nums[i-1]+1:
            current_length+=1
        #SUBSEQUENCE BROKEN
        else:
            longest=max(longest,current_length)
            current_length=1
    return max(longest,current_length)
nums=[1,200,45,3,23,1,4,2]
print(longest_consecutive(nums))

#OPTIMAL METHOD USING HASH SET
def longest_sequence(nums):
    #EDGE CASE:
    if not nums:
        return 0
    num_set=set(nums)
    longest=0
    for num in num_set:
        #START OF SEQUENCE
        if num-1 not in num_set:
            current=num
            length=1
            while current+1 in num_set:
                current+=1
                length+=1
            longest=max(longest,length)
    return longest
nums=[1,200,3,400,24,4,23,5,2]
print(longest_sequence(nums))