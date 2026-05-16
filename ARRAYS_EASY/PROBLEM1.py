#LARGEST ELEMENT (STRIVER SHEET PROBLEM NO 1)

nums=[1,2,3,4,5]
largest=nums[0]
n=len(nums)
for i in nums:
    if i > largest:
        largest=i
print(largest) 


#USING TEH OOPS METHOD
class Solution:
    def largestElement(self, nums):
        largest=nums[0]
        n=len(nums)
        for i in nums:
            if i>largest:
                largest=i
        return largest
nums=[1,2,3,4,5]
obj=Solution()
print(obj.largestElement(nums))  