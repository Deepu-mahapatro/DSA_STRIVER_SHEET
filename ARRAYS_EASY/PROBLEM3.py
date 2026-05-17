#SECOND LARGEST NUMBER

nums=[1,2,3,4,5,6,7,7]
n=len(nums)
second=float('-inf')
largest=float('-inf')
for i in range(n):
    if nums[i]>largest:
        second=largest
        largest=nums[i]
    elif nums[i]>second and nums[i]!= largest:  #this executes when teh condition fails
        second=nums[i]                          #for nums=[10,50,30] for this condition
print("largest:",largest)                       #used for unsorted arrays
print("second largest:",second)