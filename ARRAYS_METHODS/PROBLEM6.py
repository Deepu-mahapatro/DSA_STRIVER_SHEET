#COUNT NUMBER OF NICE SUB ARRAYS
#CORE IDEA:
#COUNT SUB ARRAYS WITH
#EXACTLY K ODD NUMBERS
#PROCESS:
#ADD 1 TO PREFIX
#IF NUMBER IS ODD
#FIND PREFIX-K
#IF IT EXISTS
#ADD ITS FREQUENCY
#TO ANSWER
#STORE CURRENT PREFIX
#KEY OBSERVATION:
#CURRENT_PREFIX-
#PREVIOUS_PREFIX=K 
#THAT MEANS
#SUB ARRAY HAS
#EXACTLY K ODDS
#HASHMAP STORES
#PREFIX FREQUENCIES
#WHY?
#SAME PREFIX CAN
#APPEAR MANY TIMES
#FORMULA:
#REQUIRED=
#PREFIX-K
#START WITH:
#FREQ={0:1}
#TO HANDLE
#SUB ARRAYS FROM
#INDEX 0
#TIME:
#O(n)
#SPACE:
#O(n)

#USING BRUTE FORCE APPROACH
def nice_sub(nums,k):
    n=len(nums)
    count=0
    #GENERATE ALL SUB ARRAYS
    for i in range(n):
        odd_count=0
        for j in range(i,n):
            #COUNT ODD NUMBERS
            if nums[j]%2==1:
                odd_count+=1
            #NICE SUB ARRAY FOUND
            if odd_count==k:
                count+=1
    return count
nums=[1,2,1]
k=2
print(nice_sub(nums,k))

#USING PREFIX ODD COUNT + HASHMAP
def nice_sub(nums, k):
    #STORES FREQUENCY OF ODD PREFIXES COUNTS
    freq = {0: 1}
    prefix = 0
    answer = 0
    for num in nums:
        # ODD NUMBER FOUND
        if num % 2 == 1:
            prefix += 1
        # COUNT VALID PREVIOUS PREFIXES
        answer += freq.get(prefix - k, 0)
        # STORE CURRENT PREFIX
        freq[prefix] = freq.get(prefix, 0) + 1
    return answer
nums=[1,2,1]
k=2
print(nice_sub(nums,k))

#CONVERTING INTO BINARY ARRAY
def nice_sub(nums, k):
    binary = []
    for num in nums:
        if num % 2 == 1:
            binary.append(1)
        else:
            binary.append(0)
    freq = {0: 1}
    prefix = 0
    answer = 0
    for value in binary:
        prefix += value
        answer += freq.get(prefix - k, 0)
        freq[prefix] = freq.get(prefix, 0) + 1
    return answer
nums=[1,2,1]
k=2
print(nice_sub(nums,k))

#USING SLIDING WINDOW
def nice_sub(nums, k):
    def atMost(k):
        left = 0
        odd_count = 0
        answer = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1
            while odd_count > k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1
            answer += (right - left + 1)
        return answer
    return atMost(k) - atMost(k - 1)
nums=[1,2,1]
k=2
print(nice_sub(nums,k))