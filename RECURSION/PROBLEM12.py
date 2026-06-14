#SUBSETS II (POWER SET WITH DUPLICATES)
#THE PURPOSE OF SUBSETS II IS:
#TO GENERATE ALL UNIQUE SUBSETS
#OF THE GIVEN ARRAY.
#THE ARRAY MAY CONTAIN
#DUPLICATE ELEMENTS.
#DUPLICATE SUBSETS
#MUST BE AVOIDED.
#PROCESS:
#SORT THE ARRAY FIRST.
#START WITH AN EMPTY SUBSET.
#FOR EACH ELEMENT:
#DECIDE WHETHER TO
#INCLUDE IT IN THE SUBSET.
#USE BACKTRACKING TO
#GENERATE ALL POSSIBILITIES.
#SKIP DUPLICATE ELEMENTS
#AT THE SAME RECURSION LEVEL.
#CONDITION:
#IF CURRENT ELEMENT IS SAME
#AS PREVIOUS ELEMENT
#AND WE ARE AT THE SAME LEVEL,
#SKIP IT TO AVOID
#DUPLICATE SUBSETS.
#IMPORTANT RULES:
#SORT THE ARRAY FIRST.
#EVERY SUBSET IS VALID.
#ADD CURRENT SUBSET
#TO RESULT.
#SKIP DUPLICATES USING:
#IF i > start AND
#nums[i] == nums[i-1]
#BASE CASE:
#NO EXPLICIT BASE CASE NEEDED.
#EVERY RECURSIVE CALL
#ADDS CURRENT SUBSET
#TO RESULT.
#WHY THIS WORKS:
#SORTING BRINGS DUPLICATES
#TOGETHER.
#SKIPPING DUPLICATES
#AT THE SAME LEVEL
#PREVENTS REPEATED SUBSETS.
#ALL UNIQUE SUBSETS
#ARE GENERATED.
#TIME COMPLEXITY:
#O(n * 2^n)
#SPACE COMPLEXITY:
#O(n) RECURSION STACK
#O(n * 2^n) OUTPUT SPACE
#FINAL IDEA:
#SORT ARRAY.
#GENERATE SUBSETS
#USING BACKTRACKING.
#SKIP DUPLICATES
#AT THE SAME LEVEL.
#STORE ONLY UNIQUE SUBSETS.

#BRUTE FORCE APPROACH
def subsetsWithDup(nums):
    result=set()
    n=len(nums)
    #BACKTRACK FUNCTION
    def backtrack(index,subset):
        #BASE CASE
        if index==n:
            result.add(tuple(subset))
            return
        #INCLUDE CURRENT ELEMENT
        subset.append(nums[index])
        backtrack(index+1,subset)
        #EXCLUDE CURRENT ELEMENT
        subset.pop()
        backtrack(index+1,subset)
    backtrack(0,[])
    answer=[]
    for subset in result:
        answer.append(list(subset))
    return answer
nums=[1,2,2]
print(subsetsWithDup(nums))

#BETTER METHOD OPTIMAL SOLUTION
def subsetWithDup(nums):
    nums.sort()
    result=[]
    #BACKTRACK FUNCTION
    def backtrack(start,subset):
        #EVERY SUBSET IS VALID 
        result.append(subset[:])
        for i in range(start,len(nums)):
            #SKIP DUPLICATE ELEMENTS
            if i > start and nums[i]==nums[i-1]:
                continue
            subset.append(nums[i])
            backtrack(i+1,subset)
            subset.pop()
    backtrack(0,[])
    return result
nums=[1,2,2]
print(subsetsWithDup(nums))