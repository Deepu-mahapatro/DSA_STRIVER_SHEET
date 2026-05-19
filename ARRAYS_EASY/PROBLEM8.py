#ADD ZEROS AT END

#USING EXTRA LIST
nums=[1,0,2,0,3,0,4]
result=[]
#ADD NON ZERO ELEMENTS
for i in nums:
    if i!=0:
        result.append(i)
#COUNT ZEROS
zero_count=nums.count(0)
#ADD ZEROS AT END
for i in range(zero_count):
    result.append(0)
print(result)

#USING TWO POINTER TECHNIQUE
nums=[1,2,0,3,0,4,0]
index=0
#MOVE NON ZERO ELEMENTS FORWARD
for i in range(len(nums)):
    if nums[i]!=0:
        nums[index]=nums[i]
        index+=1
#FILL REMAINING ELEMENTS WITH ZERO
while index<len(nums):
    nums[index]=0
    index+=1
print(nums)

#SWAP METHOD()
nums=[1,0,3,2,0,0,4]
j=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        j+=1
print(nums)

#USING LIST COMPREHENSION
nums=[1,2,3,0,0,4,0]
#NON ZEROS COUNT
non_zeros=[x for x in nums if x!=0]
#ZEROS COUNT
zeros=[0] * nums.count(0)
#ADDING NON_ZEROS AND ZEROS
result=non_zeros+zeros
print(result)