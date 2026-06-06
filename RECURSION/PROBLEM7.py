#COMBINATION SUM II
# PURPOSE:
# FIND ALL UNIQUE
# COMBINATIONS
# WHOSE SUM EQUALS TARGET
# CORE IDEA:
# BUILD COMBINATION
# RECURSIVELY
# CHOOSE A NUMBER
# REDUCE TARGET
# EACH NUMBER CAN BE
# USED ONLY ONCE
# STORE COMBINATION
# WHEN TARGET = 0
# SORT ARRAY FIRST
# TO HANDLE DUPLICATES
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
# DUPLICATE NUMBERS
# IN INPUT ARRAY
# -> SKIP DUPLICATE
# COMBINATIONS
# RECURSIVE STEP:
# TAKE CURRENT NUMBER
# MOVE TO NEXT INDEX
# REDUCE TARGET
# OR SKIP NUMBER
# MOVE TO NEXT
# DISTINCT NUMBER
# KEY OBSERVATION:
# TAKE ->
# NEXT INDEX
# SKIP ->
# NEXT DISTINCT INDEX
# TARGET = 0
# MEANS VALID ANSWER
# TARGET < 0
# MEANS STOP
# SORTING HELPS
# DETECT DUPLICATES
# DUPLICATES ARE
# SKIPPED WHILE
# EXCLUDING ELEMENTS
# CONCLUSION:
# BUILD ONE NUMBER
# AT A TIME
# TAKE OR SKIP
# BACKTRACK
# WHEN NEEDED
# STORE EVERY
# UNIQUE VALID
# COMBINATION
# TIME COMPLEXITY:
# EXPONENTIAL
# SPACE COMPLEXITY:
# O(N)

#USING STANDARD BACKTRACKING METHOD
def combinationSum(candidates,target):
    candidates.sort()
    result=[]
    def backtrack(start,target,path):
        #VALID COMBINATION FOUND
        if target==0:
            result.append(path[:])
            return
        #EXPLORE ALL CHOICES FROM CURRENT POSITIONS
        for i in range(start,len(candidates)):
            #SKIP DUPLICATES AT SAME LEVEL
            if i>start and candidates[i]==candidates[i-1]:
                continue
            #PRUNING
            if candidates[i]>target:
                break
            path.append(candidates[i])
            #MOVE TO NEXT INDEX
            backtrack(i+1,target-candidates[i],path)
            #BACKTRACK
            path.pop()
    backtrack(0,target,[])
    return result
candidates=[10,1,2,7,6,1,5]
target=8
print(combinationSum(candidates,target))

#ANOTHER METHOD
def combinationSum(candidates,target):
    candidates.sort()
    result = []
    def dfs(index, target, path):
        if target == 0:
            result.append(path[:])
            return
        if index == len(candidates):
            return
        if target < 0:
            return
        # INCLUDE current element
        path.append(candidates[index])
        dfs(index + 1,
            target - candidates[index],
            path)
        path.pop()
        # EXCLUDE current element
        next_index = index + 1
        while (next_index < len(candidates)
                and candidates[next_index] == candidates[index]):
            next_index += 1
        dfs(next_index, target, path)
    dfs(0, target, [])
    return result
candidates=[10,1,1,2,5,6,7]
target=8
print(combinationSum(candidates,target))

#USING BACKTRACK FOR LOOP METHOD
def combinationSum2(candidates,target):
        candidates.sort()
        answer = []
        def solve(start, remaining, current):
            if remaining == 0:
                answer.append(current[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                current.append(candidates[i])
                solve(i + 1,
                      remaining - candidates[i],
                      current)
                current.pop()
        solve(0, target, [])
        return answer
candidates=[7,10,6,5,1,1,2]
target=8
print(combinationSum2(candidates,target))