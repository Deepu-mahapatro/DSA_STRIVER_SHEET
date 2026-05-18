#ROTATE ARRAY LEFT BY ONE 

nums=[1,2,3,4,5]
n=len(nums)
if n>0:
    first=nums[0]
    for i in range(n-1):
        nums[i]=nums[i+1]
    nums[n-1]=first
print(nums)

#USING SLICING METHOD
nums=[1,2,3,4,5]
n=len(nums)
if n>0:
    result=nums[1:]+[nums[0]]
print(result)

#USING POP() AND APPEND()
nums=[1,2,3,4,5]
n=len(nums)
if n>0:
    first=nums.pop(0)
    nums.append(first)
print(nums)