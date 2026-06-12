#MAXIMUM SUBARRAY SUM
#USING KADANE'S ALGORITHM
#PROBLEM:
#FIND THE CONTIGUOUS SUBARRAY
#WITH THE MAXIMUM SUM
#CORE IDEA:
#AT EACH POSITION
#DECIDE WHETHER TO
#CONTINUE THE CURRENT SUBARRAY
#OR START A NEW SUBARRAY
#IMPORTANT FORMULA:
#CURRENT_SUM=
#MAX(num,current_sum+num)
#KEY OBSERVATION:
#NEGATIVE SUMS CAN HURT
#FUTURE SUBARRAY SUMS
#IF STARTING NEW IS BETTER
#DISCARD THE OLD SUBARRAY
#CURRENT_SUM REPRESENTS:
#BEST SUBARRAY SUM
#ENDING AT CURRENT INDEX
#MAX_SUM REPRESENTS:
#BEST ANSWER FOUND
#SO FAR
#PROCESS:
#INITIALIZE CURRENT_SUM
#WITH FIRST ELEMENT
#INITIALIZE MAX_SUM
#WITH FIRST ELEMENT
#TRAVERSE THE ARRAY
#COMPARE STARTING NEW
#AND EXTENDING OLD
#UPDATE CURRENT_SUM
#UPDATE MAX_SUM
#EDGE CASES:
#EMPTY ARRAY
#SINGLE ELEMENT ARRAY
#ALL POSITIVE NUMBERS
#ALL NEGATIVE NUMBERS
#ARRAY CONTAINING ZEROS
#TIME COMPLEXITY:
#O(n)
#SPACE COMPLEXITY:
#O(1)
#CONCLUSION:
#USES DYNAMIC PROGRAMMING
#TO KEEP ONLY NECESSARY DATA
#FINDS THE ANSWER
#IN A SINGLE PASS

#USING BRUTE FORCE METHOD
def max_sub_array(nums):
    #EDGE CASE
    if not nums:
        return 0
    max_sum=float('-inf')
    #PICK STARTING POINT
    for start in range(len(nums)):
        current_sum=0
        #EXTEND SUB ARRAY
        for end in range(start,len(nums)):
            current_sum+=nums[end]
            max_sum=max(max_sum,current_sum)
    return max_sum
nums=[-2,1,-3,4]
print(max_sub_array(nums))

#USING KADANE'S ALGORITHM
def max_sub_array(nums):
    #EDGE CASE
    if not nums:
        return 0
    current_sum=nums[0]
    max_sum=nums[0]
    for num in nums[1:]:
        #EITHER CONTINUE OLD SUB ARRAY 
        #OR START A NEW FRESH ARRAY
        current_sum=max(num,current_sum+num)
        #UPDATE ANSWER
        max_sum=max(max_sum,current_sum)
    return max_sum
nums=[-2,1,-3,4]
print(max_sub_array(nums))

#BEGINNER FRIENDLY KADANE VERSION
def max_sub_array(nums):
    #EDGE CASE
    if not nums:
        return 0
    current_sum=nums[0]
    max_sum=nums[0]
    for i in range(1,len(nums)):
        num=nums[i]
        extend_previous=current_sum+num
        start_new=num
        current_sum=max(extend_previous,start_new)
        max_sum=max(max_sum,current_sum)
    return max_sum
print(max_sub_array(nums))