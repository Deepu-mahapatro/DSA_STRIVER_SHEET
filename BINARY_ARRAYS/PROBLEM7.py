#FIND PEAK ELEMENT

#USING BINARY SEARCH METHOD
def findPeakElement(nums):
    if not nums:
        return 0
    left=0
    right=len(nums)-1
    while left<right:
        mid=(left+right)//2
        if nums[mid]<nums[mid+1]:
            left=mid+1
        if nums[mid]>nums[mid+1]:
            right=mid
    return left
nums=[1,2,3,4,3]
print(findPeakElement(nums))


#LINEAR SEARCH METHOD
def findPeakElement(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return i
    return len(nums)-1
nums=[1,2,3,4,3]
print(findPeakElement(nums))

#PYTHON LIST METHOD
def findPeakElement(nums):
    return nums.index(max(nums))
nums=[1,2,3,4,3]
print(findPeakElement(nums))