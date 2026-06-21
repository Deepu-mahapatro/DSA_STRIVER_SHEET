#SEARCH IN ROTATED SORTED ARRAY-II

#LINEAR SEARCH METHOD
def search(nums,target):
    for num in nums:
        if num==target:
            return True
    return False
nums=[2,5,6,0,0,1,2]
target=0
print(search(nums,target))

#USING BINARY SEARCH
def search(nums,target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return True
        #CANNOT DETERMINE SORTED HALF DUE TO DUPLICATE
        if nums[left]==nums[mid]==nums[right]:
            left+=1
            right-=1
        #LEFT HALF IS SORTED
        elif nums[left]<=nums[mid]:
            if nums[left]<=target<=nums[mid]:
                right=mid-1
            else:
                left=mid+1
        #RIGHT HALF IS SORTED
        else:
            if nums[mid]<target<=nums[right]:
                left=mid+1
            else:
                right=mid-1
    return False
nums=[2,5,6,0,0,1,2]
target=0
print(search(nums,target))