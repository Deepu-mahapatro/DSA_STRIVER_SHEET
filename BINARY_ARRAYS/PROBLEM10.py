#FIND THE SMALLEST DIVISOR

#USING BINARY SEARCH METHOD
import math
def small_div(nums,threshold):
    #EDGE CASE
    if not nums:
        return 0
    #SEARCH SPACE RANGE
    l=1
    r=max(nums)
    result=0
    #BINARY SEARCH
    while l<=r:
        mid=(l+r)//2
        sum=0
        for val in nums:
            sum+=math.ceil(val/mid)
        if sum<=threshold:
            result=mid
            r=mid-1
        else:
            l=mid+1
    return result
nums=[1,2,5,9]
threshold=6
print(small_div(nums,threshold))


#LINEAR SEARCH METHOD
import math
def small_div(nums,threshold):
    #TRY EVERY DIVISOR
    for divisor in range(1,max(nums)+1):
        total=0
        #CALCULATE SUM
        for num in nums:
            total+=math.ceil(num/divisor)
        #FIRST VALID DIVISOR
        if total<=threshold:
            return divisor
nums=[1,2,5,9]
threshold=6
print(small_div(nums,threshold))


#USING BINARY SEARCH OPTIMAL SOLUTION
def small_div(nums,threshold):
    #EDGE CASE
    if not nums:
        return 0
    #SEARCH SPACE FOR DIVISORS
    l=1
    r=max(nums)
    #AS LAST NUMBER ALWAYS VALID DIVISOR
    ans=r
    #BINARY SEARCH
    while l<=r:
        #FIND THE MIDDLE DIVISOR
        mid=(l+r)//2
        #CALCULATE TEH TOTAL AFTER DIVIDING THE MID
        total=0
        for num in nums:
            #CEILING DIVISION METHOD (NO MATH)
            total+=(num+mid-1)//mid
        #IF CURRENT DIVISOR SATISFIES THE THRESHOLD
        if total<=threshold:
            #STORE THE CURRENT DIVISOR
            ans=mid
            #TRY TO FIND SMALLEST AT LEFT RIGHT
            r=mid-1
        else:
            #DIVISOR IS TOO SMALL INCREASE IT SEARCH ON RIGHT
            l=mid+1
    #RETURN THE SMALLEST DIVISOR
    return ans
nums=[1,2,5,9]
threshold=6
print(small_div(nums,threshold))
        