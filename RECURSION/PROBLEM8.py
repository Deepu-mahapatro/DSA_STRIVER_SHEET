# COMBINATION SUM III
# PURPOSE:
# FIND ALL UNIQUE
# COMBINATIONS OF
# EXACTLY K NUMBERS
# WHOSE SUM EQUALS N
# NUMBERS ALLOWED:
# ONLY 1 TO 9
# EACH NUMBER CAN BE
# USED ONLY ONCE
# CORE IDEA:
# BUILD COMBINATION
# RECURSIVELY
# CHOOSE A NUMBER
# ADD IT TO PATH
# REDUCE REMAINING
# SUM NEEDED
# MOVE TO NEXT NUMBER
# SO SAME NUMBER
# CANNOT BE REUSED
# STORE COMBINATION
# WHEN:
# LENGTH == K
# AND
# SUM == N
# EDGE CASES:
# K = 0
# -> RETURN []
# N <= 0
# -> NO VALID ANSWER
# K > 9
# -> IMPOSSIBLE
# ONLY 9 NUMBERS EXIST
# SUM EXCEEDS N
# -> INVALID PATH
# LENGTH EXCEEDS K
# -> INVALID PATH
# K = 1
# AND N BETWEEN
# 1 AND 9
# -> SINGLE ANSWER
# K = 9
# AND N = 45
# -> [1,2,3,4,5,6,7,8,9]
# RECURSIVE STEP:
# TAKE CURRENT NUMBER
# ADD TO PATH
# RECURSE WITH:
# NEXT NUMBER
# UPDATED SUM
# BACKTRACK
# REMOVE NUMBER
# TRY NEXT CHOICE
# KEY OBSERVATION:
# AFTER CHOOSING
# A NUMBER
# NEXT CALL STARTS
# FROM num + 1
# THIS ENSURES:
# EACH NUMBER IS
# USED ONLY ONCE
# NO DUPLICATE
# COMBINATIONS
# EXAMPLE:
# [1,2,4]
# IS ALLOWED
# [2,1,4]
# IS NEVER FORMED
# BECAUSE WE ALWAYS
# MOVE FORWARD
# VALID ANSWER:
# LENGTH == K
# AND
# SUM == N
# INVALID ANSWER:
# LENGTH > K
# OR
# SUM > N
# PRUNING:
# IF CURRENT SUM
# ALREADY EXCEEDS N
# STOP EXPLORING
# CONCLUSION:
# BUILD ONE NUMBER
# AT A TIME
# CHOOSE
# RECURSE
# BACKTRACK
# STORE EVERY
# VALID COMBINATION
# TIME COMPLEXITY:
# O(2^9)
# SPACE COMPLEXITY:
# O(K)
# RECURSION STACK
# + CURRENT PATH

#COMBINATION III
def combinationSum3(k,n):
    result=[]
    def backtrack(start,path,current_sum):
        #VALID COMBINATIONS FOUND
        if len(path)==k and current_sum==n:
            result.append(path[:])
            return
        #INVALID STATE 
        if len(path)>k and current_sum>n:
            return 
        #TRY EVERY POSSIBLE NUMBER
        for num in range(start,10):
            #CHOOSE 
            path.append(num)
            #EXPLORE 
            backtrack(num+1,path,current_sum+num)
            # UNDO CHOICE
            path.pop()
    backtrack(1,[],0)
    return result
print(combinationSum3(3,7))

#BACKTRACKING WITH OPTIMIZED WAY
def combinationSum3(k, n):
    result = []
    def backtrack(start, path, current_sum):
        # Required size reached
        if len(path) == k:
            if current_sum == n:
                result.append(path[:])
            return
        for num in range(start, 10):
            # Pruning
            if current_sum + num > n:
                break
            path.append(num)
            backtrack(num + 1,
                      path,
                      current_sum + num)
            path.pop()
    backtrack(1, [], 0)
    return result
print(combinationSum3(3,7))

#INCLUDE AND EXCLUDE RECURSION
def combinationSum3(k, n):
    result = []
    def dfs(num, path, current_sum):
        # Valid answer
        if len(path) == k:
            if current_sum == n:
                result.append(path[:])
            return
        # Numbers exhausted
        if num > 9:
            return
        # Sum exceeded
        if current_sum > n:
            return
        # -----------------
        # Include current number
        # -----------------
        path.append(num)
        dfs(num + 1,
            path,
            current_sum + num)
        path.pop()
        # -----------------
        # Exclude current number
        # -----------------
        dfs(num + 1,
            path,
            current_sum)
    dfs(1, [], 0)
    return result
print(combinationSum3(3,7))