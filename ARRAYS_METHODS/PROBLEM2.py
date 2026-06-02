# MAX CONSECUTIVE ONES III
# THE PURPOSE OF MAX CONSECUTIVE ONES III IS:
# TO FIND THE MAXIMUM LENGTH OF A CONTINUOUS SUBARRAY
# THAT CAN BECOME ALL 1s AFTER FLIPPING AT MOST k ZEROS.
# PROCESS:
# USE A SLIDING WINDOW.
# EXPAND WINDOW BY MOVING RIGHT POINTER.
# COUNT HOW MANY ZEROS EXIST INSIDE THE WINDOW.
# AS LONG AS ZERO COUNT IS LESS THAN OR EQUAL TO k:
# WINDOW IS VALID.
# IF ZERO COUNT BECOMES GREATER THAN k:
# SHRINK WINDOW FROM THE LEFT.
# REMOVE ELEMENTS UNTIL WINDOW BECOMES VALID AGAIN.
# UPDATE MAXIMUM WINDOW LENGTH FOR EVERY VALID WINDOW.
# RESULT BECOMES THE LONGEST POSSIBLE SUB ARRAY OF 1s.
# CONDITION:
# NUMBER OF ZEROS INSIDE THE WINDOW MUST NOT EXCEED k.
# zero_count <= k
# IMPORTANT RULES:
# WINDOW REPRESENTS A CONTINUOUS SUB ARRAY.
# ZEROS ARE NOT ACTUALLY FLIPPED.
# WE ONLY CHECK IF THEY CAN BE FLIPPED.
# EVERY ZERO INSIDE WINDOW USES ONE AVAILABLE FLIP.
# IF ZERO COUNT EXCEEDS k:
# WINDOW BECOMES INVALID.
# USE WHILE, NOT IF, TO SHRINK WINDOW.
# MULTIPLE REMOVALS MAY BE REQUIRED.
# WHY THIS WORKS:
# EVERY VALID WINDOW CONTAINS AT MOST k ZEROS.
# THOSE ZEROS CAN BE IMAGINED AS FLIPPED TO 1s.
# EXPANDING HELPS FIND LARGER VALID WINDOWS.
# SHRINKING REMOVES EXTRA ZEROS WHEN LIMIT IS EXCEEDED.
# EACH ELEMENT ENTERS AND LEAVES WINDOW ONLY ONCE.
# THIS GIVES AN O(n) SOLUTION.
# WHAT DOES zero_count REPRESENT?
# NUMBER OF ZEROS CURRENTLY INSIDE THE WINDOW.
# WHAT DOES k REPRESENT?
# MAXIMUM NUMBER OF ZEROS WE ARE ALLOWED TO FLIP.
# VALID WINDOW:
# zero_count <= k
# INVALID WINDOW:
# zero_count > k
# EDGE CASES:
# EMPTY ARRAY -> ANSWER = 0
# ALL 1s -> ANSWER = LENGTH OF ARRAY
# ALL 0s AND k >= LENGTH -> ANSWER = LENGTH OF ARRAY
# k = 0 -> FIND LONGEST EXISTING STREAK OF 1s
# SINGLE ELEMENT 1 -> ANSWER = 1
# SINGLE ELEMENT 0 AND k = 1 -> ANSWER = 1
# MULTIPLE EXTRA ZEROS MAY REQUIRE MULTIPLE SHRINKS
# FINAL IDEA:
# KEEP A WINDOW CONTAINING AT MOST k ZEROS.
# EXPAND WINDOW TO INCLUDE MORE ELEMENTS.
# SHRINK WINDOW WHEN TOO MANY ZEROS APPEAR.
# TRACK THE LARGEST VALID WINDOW LENGTH.
# THAT LENGTH IS THE ANSWER.

#USING BRUTE FORCE APPROACH
def longest_ones(nums,k):
    max_length=0
    n=len(nums)
    #STARTING POINT OF ARRAY
    for start in range(n):
        zero_count=0
        #ENDING POINT OF ARRAY
        for end in range(start,n):
            #COUNT ZEROS
            if nums[end]==0:
                zero_count+=1
            #VALID WINDOW
            if zero_count<=k:
                max_length=max(max_length,end-start+1)
    return max_length
nums=[1,1,0,1,0]
k=1
print(longest_ones(nums,k))

#USING SLIDING WINDOW METHOD
def longest_ones(nums,k):
    max_length=0
    n=len(nums)
    left=0
    zero_count=0
    for right in range(n):
        #COUNT ZEROS
        if nums[right]==0:
            zero_count+=1
        #VALID WINDOW
        while zero_count>k:
            if nums[left]==0:
                zero_count-=1
            left+=1
        max_length=max(max_length,right-left+1)
    return max_length
nums=[1,1,0,1,0]
k=1
print(longest_ones(nums,k))

#BRUTE FORCE METHOD 2
def longest_ones(nums,k):
    max_length=0
    n=len(nums)
    for start in range(n):
        zero_count=0
        for end in range(start,n):
            #COUNT ZEROS
            if nums[end]==0:
                zero_count+=1
            #VALID WINDOW
            if zero_count>k:
                break
            max_length=max(max_length,end-start+1)
    return max_length
nums=[1,1,0,1,0]
k=1
print(longest_ones(nums,k))