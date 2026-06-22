#SINGLE ELEMENT IN A SORTED ARRAY

#USING LINEAR METHOD
def search(nums):
    left=0
    right=len(nums)-1
    while left<right:
        if nums[left]!=nums[left+1]:
            return nums[left]
        left+=2
    return nums[-1]
nums=[1,1,2,2,3,4,4]
print(search(nums))

#USING BINARY SEARCH METHOD
def search(nums):
    if not nums:
        return 0
    left=0
    right=len(nums)-1
    while left<right:
        mid=(left+right)//2
        if mid%2==1:
            mid-=1
        if nums[mid]==nums[mid+1]:
            left=mid+2
        else:
            right=mid
    return nums[left]
nums=[1,1,2,2,3,4,4]
print(search(nums))

#USING PYTHON LIST METHOD
def search(nums):
    for num in nums:
        if nums.count(num)==1:
            return num
nums=[1,1,2,2,3,4,4]
print(search(nums))