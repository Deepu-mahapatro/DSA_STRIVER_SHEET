#SEARCH INSERT POSITION

#LINEAR SEARCH METHOD
def search(nums,target):
    for i in range(len(nums)):
        if nums[i]>=target:
            return i
    return len(nums)
nums=[1,3,4,5]
target=2
print(search(nums,target))

def search(nums,target):
    if not nums:
        return 0
    left=0
    right=len(nums)-1
    while left<=right:
        mid=left+(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left
nums=[1,3,4,5]
target=2
print(search(nums,target))


