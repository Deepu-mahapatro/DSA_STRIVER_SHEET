#CHECK IF ARRAY IS SORTED AND ROTATED 

nums=[3,4,5,1,2]
n=len(nums)
count=0                          #count refer to break points 
for i in range(n):
    if nums[i]>nums[(i+1)%n]:    #this condition says that circular order
        count+=1                 #or else it reaches out of bound
if count<=1:
    print(True)
else:
    print(False)