#SEARCH IN ROTATED SORTED ARRAY-I

#LINEAR SEARCH METHOD
def search_binary(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1
nums=[4,5,6,1,2,3]
target=2
print(search_binary(nums,target))


#USING BINARY SEARCH METHOD
def search_binary(nums,target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        if nums[left]<=nums[mid]:
            if nums[left]<=target<nums[mid]:
                right0=mid-1
            else:
                left=mid+1
        else:
            if nums[mid]<target<=nums[right]:
                left=mid+1
            else:
                right=mid-1
    return -1
nums=[4,5,6,1,2,3]
target=2
print(search_binary(nums,target))


#USING PYTHON LIST METHOD
def search_binary(nums,target):
    if target in nums:
        return nums.index(target)
    return -1
nums=[4,5,6,1,2,3]
target=2
print(search_binary(nums,target))