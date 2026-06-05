# BINARY SUB ARRAYS WITH SUM
# USING PREFIX SUM + HASHMAP
# CORE IDEA:
# STORE FREQUENCY OF PREFIX SUMS
# FIND PREVIOUS PREFIX SUMS
# THAT CAN FORM THE TARGET SUM
# PROCESS:
# TRAVERSE THE ARRAY
# UPDATE CURRENT PREFIX SUM
# CALCULATE REQUIRED PREFIX SUM
# CHECK IF REQUIRED PREFIX EXISTS
# ADD ITS FREQUENCY TO THE ANSWER
# STORE CURRENT PREFIX SUM
# UPDATE ITS FREQUENCY
# IMPORTANT FORMULA:
# CURRENT_PREFIX - OLD_PREFIX = GOAL
# REQUIRED_PREFIX =
# CURRENT_PREFIX - GOAL
# KEY OBSERVATION:
# IF REQUIRED PREFIX EXISTS
# A VALID SUB ARRAY IS FOUND
# HASHMAP STORES THE NUMBER
# OF TIMES EACH PREFIX SUM OCCURS
# MULTIPLE OCCURRENCES OF THE SAME
# PREFIX SUM CAN FORM MULTIPLE
# VALID SUB ARRAYS
# EDGE CASES:
# EMPTY ARRAY -> RETURN 0
# SINGLE ELEMENT EQUAL TO GOAL
# SINGLE ELEMENT NOT EQUAL TO GOAL
# GOAL = 0
# ALL ELEMENTS ARE 0
# NO VALID SUB ARRAY EXISTS
# MULTIPLE PREFIX SUM REPETITIONS
# TIME COMPLEXITY:
# O(n)
# SPACE COMPLEXITY:
# O(n)
# CONCLUSION:
# USE PREFIX SUMS TO TRACK
# CUMULATIVE SUMS
# USE HASHMAP TO STORE
# THEIR FREQUENCIES
# COUNT VALID SUB ARRAYS
# IN O(n) TIME

#USING BRUTE FORCE APPROACH 
def sub_withSum(num,goal):
    count=0
    n=len(num)
    for i in range(n):
        curr_sum=0
        for j in range(i,n):
            curr_sum+=num[j]
            if curr_sum==goal:
                count+=1
    return count
num=[1,1,0]
goal=2
print(sub_withSum(num,goal))


#USING SLIDING WINDOW METHOD
def sub_withSum(num, goal):
    if goal < 0:
        return 0
    left = 0
    curr_sum = 0
    count = 0
    for right in range(len(num)):
        curr_sum += num[right]
        while curr_sum > goal:
            curr_sum -= num[left]
            left += 1
        count += right - left + 1
    return count
def numSub_arraysWithSum(num, goal):
    return sub_withSum(num, goal) - sub_withSum(num, goal - 1)
num = [1, 1, 0]
goal = 2
print(numSub_arraysWithSum(num, goal))

#USING HASHMAP AND PREFIX METHOD
def sub_withSum(num,goal):
    #PREFIX SUM 0 APPEARS ONCE INITIALLY
    prefix_count={0:1}
    curr_sum=0
    count=0
    #TRAVERSE EACH ELEMENT
    for i in num:
        #UPDATE RUNNING PREFIX SUM
        curr_sum+=i
        #FIND REQUIRED PREFIX SUM
        required_prefix=curr_sum-goal
        #IF VALID SUB ARRAY
        if required_prefix in prefix_count:
            count+=prefix_count[required_prefix]
        #FREQUENCY COUNT
        prefix_count[curr_sum]=prefix_count.get(curr_sum,0)+1
    #RETURN COUNT
    return count
num=[1,1,0]
goal=2
print(sub_withSum(num,goal))