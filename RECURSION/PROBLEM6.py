#COMBINATION SUM
# PURPOSE:
# FIND ALL COMBINATIONS
# WHOSE SUM EQUALS TARGET
# CORE IDEA:
# BUILD COMBINATION
# RECURSIVELY
# CHOOSE A NUMBER
# REDUCE TARGET
# REUSE SAME NUMBER
# IF NEEDED
# STORE COMBINATION
# WHEN TARGET = 0
# EDGE CASES:
# TARGET == 0
# -> STORE ANSWER
# TARGET < 0
# -> INVALID PATH
# NO SOLUTION
# -> RETURN []
# SINGLE NUMBER
# EQUALS TARGET
# -> VALID ANSWER
# NUMBER CAN BE
# USED MULTIPLE TIMES
# RECURSIVE STEP:
# TAKE CURRENT NUMBER
# STAY ON SAME INDEX
# REDUCE TARGET
# OR SKIP NUMBER
# MOVE TO NEXT INDEX
# KEY OBSERVATION:
# TAKE ->
# SAME INDEX
# SKIP ->
# NEXT INDEX
# TARGET = 0
# MEANS VALID ANSWER
# TARGET < 0
# MEANS STOP
# INDEX PREVENTS
# DUPLICATE COMBINATIONS
# CONCLUSION:
# BUILD ONE NUMBER
# AT A TIME
# TAKE OR SKIP
# BACKTRACK
# WHEN NEEDED
# STORE EVERY
# VALID COMBINATION
# TIME COMPLEXITY:
# EXPONENTIAL
# SPACE COMPLEXITY:
# O(TARGET)


#TAKE AND SKIP RECURSION
def combinationSum(candidates,target):
    #STORE RESULT
    result=[]
    #START BACKTRACK
    def backtrack(index,target,path):
        #BASE CASE
        #VALID COMBINATION FOUND
        if target==0:
            result.append(path[:])
            return
    #BASE CASE
    #IF TARGET NEGATIVE OR 
    # CHECKED ALL NUMBERS STOP IT
        if target < 0 or index==len(candidates):
            return
        #ADD CURRENT NUMBER TO PATH
        path.append(candidates[index])
        #BACKTRACK APPLIED
        backtrack(index,target-candidates[index],path)
        #REMOVE LAST NUMBER
        path.pop()
        #MOVE TO NEXT INDEX
        backtrack(index+1,target,path)
    #START RECURSION FROM INDEX0
    backtrack(0,target,[])
    #RETURN VALID ALL COMBINATIONS
    return result
candidates=[2,3]
target=6
print(combinationSum(candidates,target))
    
#USING FOR LOOP RECURSION
def combinationSum(candidates,target):
    result=[]
    def backtrack(start,target,path):
        if target==0:
            result.append(path[:])
            return
        if target<0:
            return
        for i in range(start,len(candidates)):
            path.append(candidates[i])
            backtrack(i,target-candidates[i],path)
            path.pop()
    backtrack(0,target,[])
    return result
candidates=[2,3]
target=6
print(combinationSum(candidates,target))

#PURE RECURSION STYLE
def combinationSum(candidates,target):
    def backtrack(start,target):
        if target==0:
            return [[]]
        if target<0:
            return []
        result=[]
        for i in range(start,len(candidates)):
            num=candidates[i]
            combinations=backtrack(i,target-num)
            for comb in combinations:
                result.append([num]+comb)
        return result
    return backtrack(0,target)
candidates=[2,3]
target=6
print(combinationSum(candidates,target))
            