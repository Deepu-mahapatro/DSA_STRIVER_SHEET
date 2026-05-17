#REMOVING DUPLICATES FROM SORTED ARRAY

nums=[1,1,2,3,3,5,5]
if len(nums)==0:
    print("invalid")
else:
    k=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[k]=nums[i]
            k+=1
print("unique elements:",k)
print("after removing duplicates")
for i in range(k):
    print(nums[i],end="")
    
    
#REMOVING DUPLICATES FORM UNSORTED ARRAY
nums=[1,2,3,2,3,1,2,2,3,1,2]
n=len(nums)
unique=[]
if n==0:
    print("invalid array")
else:
    for i in range(1,n):
        if nums[i] not in unique:
            unique.append(nums[i])
print("unique elements:",len(unique))
print("after removing duplicates:")
for i in unique:
    print(i,end="")