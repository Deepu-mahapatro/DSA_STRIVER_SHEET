#FIRST AND LAST OCCURRENCE

#LINEAR SEARCH METHOD
def searchRange(nums,target):
    first=-1
    last=-1
    for i in range(len(nums)):
        if nums[i]==target:
            if first==-1:
                first=i
            last=i
    return [first,last]
nums=[1,2,2,2,3,4]
target=2
print(searchRange(nums,target))


#USING PYTHON LIST METHOD
def searchRange(nums,target):
    if target not in nums:
        return [-1,-1]
    first=nums.index(target)
    last=len(nums)-1-nums[::-1].index(target)
    return [first,last]
nums=[1,2,2,2,3,4]
target=2
print(searchRange(nums,target))

#BINARY SEARCH METHOD
def first_occurrence(nums,target):
    left=0
    right=len(nums)-1
    ans=-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            ans=mid
            right=mid-1
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return ans
def last_occurrence(nums,target):
    left=0
    right=len(nums)-1
    ans=-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            ans=mid
            left=mid+1
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return ans
def searchRange(nums,target):
    return [
        first_occurrence(nums,target),
        last_occurrence(nums,target)
    ]
nums=[1,2,2,2,3,4]
target=2
print(searchRange(nums,target))