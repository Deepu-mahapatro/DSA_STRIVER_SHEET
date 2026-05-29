#REARRANGE ARRAY ELEMENTS BY SIGN

#THE PURPOSE OF REARRANGE ARRAY BY SIGN IS:
#TO PLACE POSITIVE AND NEGATIVE NUMBERS ALTERNATELY.
#POSITIVE NUMBERS OCCUPY EVEN INDICES.
#NEGATIVE NUMBERS OCCUPY ODD INDICES.

#PROCESS:
#TRAVERSE THE ARRAY ONCE.
#KEEP A POSITIVE POINTER AT INDEX 0.
#KEEP A NEGATIVE POINTER AT INDEX 1.
#IF CURRENT NUMBER IS POSITIVE:
#PLACE IT AT POSITIVE POINTER.
#MOVE POSITIVE POINTER BY 2.
#IF CURRENT NUMBER IS NEGATIVE:
#PLACE IT AT NEGATIVE POINTER.
#MOVE NEGATIVE POINTER BY 2.
#CONTINUE UNTIL ALL ELEMENTS ARE PROCESSED.

#CONDITION:
#EVEN INDICES STORE POSITIVE NUMBERS.
#ODD INDICES STORE NEGATIVE NUMBERS.

#IMPORTANT RULES:
#POSITIVE COMES FIRST.
#ALTERNATE POSITIVE AND NEGATIVE.
#MAINTAIN RELATIVE ORDER OF POSITIVES.
#MAINTAIN RELATIVE ORDER OF NEGATIVES.

#WHY THIS WORKS:
#EVERY EVEN POSITION IS RESERVED FOR POSITIVES.
#EVERY ODD POSITION IS RESERVED FOR NEGATIVES.
#EACH NUMBER DIRECTLY GOES TO ITS CORRECT POSITION.
#RELATIVE ORDER IS PRESERVED AUTOMATICALLY.

#EDGE CASES:
#ARRAY SIZE = 2
#ALREADY ALTERNATING ARRAY
#LARGE POSITIVE/NEGATIVE VALUES
#ZERO PRESENT (CHECK CONSTRAINTS)
#UNEQUAL POSITIVE AND NEGATIVE COUNTS
#ALL POSITIVES OR ALL NEGATIVES (IF ALLOWED)

#FINAL IDEA:
#RESERVE EVEN INDICES FOR POSITIVE NUMBERS
#AND ODD INDICES FOR NEGATIVE NUMBERS,
#THEN PLACE EACH ELEMENT DIRECTLY INTO ITS
#CORRECT POSITION WHILE PRESERVING ORDER.

#MAIN LOGIC: TO ARRANGE ONE POS AND ONE NEG
#IF POS FINISH APPEND THE NEG
#IF NEG FINISH APPEND THE POS

#USING BRUTE FORCE APPROACH(WHEN POS AND NEG ARE EQUAL)
def rearrange(nums):
    pos=[]
    neg=[]
    for num in nums:
        if num>0:
            pos.append(num)
        else:
            neg.append(num)
    result=[]
    for i in range(len(pos)):
        result.append(pos[i])
        result.append(neg[i])
    return result
nums=[1,-2,3,-4,-6,3]
print(rearrange(nums))

#USING TWO POINTER APPROACH(WORK WHEN POS AND NEG ARE SAME )
def rearrange(nums):
    n=len(nums)
    result=[0]*n
    pos_index=0
    neg_index=1
    for num in nums:
        if num>0:
            result[pos_index]=num
            pos_index+=2
        else:
            result[neg_index]=num
            neg_index+=2
    return result
nums=[1,-1,3,-4,5,-6]
print(rearrange(nums))

#HANDLE UNEQUAL POSITIVE AND NEGATIVE COUNTS
def rearrange(nums):
    pos=[]
    neg=[]
    for num in nums:
        if num>0:
            pos.append(num)
        else:
            neg.append(num)
    result=[]
    i=0
    j=0
    while i<len(pos) and j<len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i+=1
        j+=1
    while i<len(pos):
        result.append(pos[i])
        i+=1
    while j<len(neg):
        result.append(neg[j])
        j+=1
    return result
nums=[1,-2,3,-4,5]
print(rearrange(nums))