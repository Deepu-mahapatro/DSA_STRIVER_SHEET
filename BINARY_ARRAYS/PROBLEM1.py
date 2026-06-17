#SEARCH X IN SORTED ARRAY

#BRUTE FORCE APPROACH
nums=[1,2,3,4,5]
target=4
for i in nums:
    if nums[i]==target:
        print(i)
        break
else:
    print(-1)
    
#BINARY SEARCH 
def binary_search(nums,target):
    left=0
    right=len(nums)-1
    while left<right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
nums=[1,2,3,4,5]
target=4
print(binary_search(nums,target))

#LINEAR SEARCH METHOD:
def search(num,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1
nums=[1,2,3,4,5]
target=4
print(search(nums,target))

#RECURSIVE BINARY SEARCH
def search(nums,left,right,target):
    if left>right:
        return -1
    mid=(left+right)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]<target:
        return search(nums,mid+1,right,target)
    else:
        return search(nums,left,mid-1,target)
nums=[1,2,3,4,5]
target=4
print(search(nums,0,len(nums)-1,target))