# COUNT SUBSEQUENCES WITH SUM = K
# CORE IDEA:
# TAKE OR NOT TAKE EACH ELEMENT
# STATE:
# (INDEX,CURRENT_SUM)
# BASE CASE:
# INDEX == N
# CURRENT_SUM == K -> RETURN 1
# ELSE RETURN 0
# CHOICE 1:
# TAKE
# CURRENT_SUM + ARR[INDEX]
# CHOICE 2:
# NOT TAKE
# CURRENT_SUM SAME
# RETURN:
# TAKE + NOT_TAKE
# DP STATE:
# DP[INDEX][CURRENT_SUM]
# TIME:
# O(2^N)
# MEMOIZATION:
# O(N*K)
# TEMPLATE:
# STATE
# BASE CASE
# TAKE
# NOT TAKE
# COMBINE ANSWERS
# PATTERN:
# COUNT PROBLEM => TAKE + NOT TAKE

#PURE RECURSION
def count_subsequences(arr,k):
    n=len(arr)
    def solve(i,curr_sum):
        if i==n:
            return 1 if curr_sum==k else 0
        take=solve(i+1,curr_sum+arr[i])
        not_take=solve(i+1,curr_sum)
        return take+not_take
    return solve(0,0)
arr=[1,2,1,1]
k=3
print(count_subsequences(arr,k))

#RECURSION + MEMORIZATION
def count_subsequences(arr, k):
    n = len(arr)
    dp = {}
    def solve(i, curr_sum):
        if i == n:
            return 1 if curr_sum == k else 0
        if (i, curr_sum) in dp:
            return dp[(i, curr_sum)]
        take = solve(i + 1, curr_sum + arr[i])
        not_take = solve(i + 1, curr_sum)
        dp[(i, curr_sum)] = take + not_take
        return dp[(i, curr_sum)]
    return solve(0, 0)
arr=[1,2,1,1]
k=3
print(count_subsequences(arr,k))

#SPACE OPTIMIZED METHOD
def count_subsequences(arr, k):
    prev = [0]*(k+1)
    prev[0] = 1
    for num in arr:
        curr = prev[:]
        for s in range(k, num-1, -1):
            curr[s] += prev[s-num]
        prev = curr
    return prev[k]
arr=[1,1,2,1]
k=3
print(count_subsequences(arr,k))