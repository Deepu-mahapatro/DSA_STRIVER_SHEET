#NEXT PERMUTATION
#The purpose of Next Permutation is:
#To generate the immediate next bigger arrangement of numbers in lexicographical order.
#PROCESS:
#Traverse from right.
#Find first decreasing element.
#If not found, reverse whole array.
#Find next greater element from right.
#Swap both elements.
#Reverse remaining suffix.
#Result becomes immediate next permutation.
#CONDITION:
    #first decreasing element from right
    #That guarantees immediate next permutation

#USING OPTIMAL APPROACH 
#OPTIMAL METHOD
def nextPermutation(nums):
    #EDGE CASE: EMPTY OR SINGLE ELEMENT
    if len(nums) <= 1:
        return
    n = len(nums)
    #STEP 1: FIND PIVOT
    #FIRST INDEX FROM RIGHT WHERE nums[i] < nums[i+1]
    pivot = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break
    #EDGE CASE:
    #ARRAY IS IN DESCENDING ORDER
    #EXAMPLE: [3,2,1] THERE IS NO NEXT PERMUTATION
    if pivot == -1:
        nums.reverse()
        return
    #STEP 2: FIND NEXT GREATER ELEMENT FROM RIGHT
    for i in range(n - 1, pivot, -1):
        if nums[i] > nums[pivot]:
            #STEP 3: SWAP
            nums[i], nums[pivot] = nums[pivot], nums[i]
            break
    #STEP 4: REVERSE THE SUFFIX
    nums[pivot + 1:] = reversed(nums[pivot + 1:])
nums=[1,2,3]
nextPermutation(nums)
print(nums)

#USING SORT METHOD
def nextPermutation(nums):
    #EDGE CASE
    if len(nums) <= 1:
        return
    n = len(nums)
    #STEP 1: FIND PIVOT
    pivot = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break
    #EDGE CASE
    if pivot == -1:
        nums.sort()
        return
    #STEP 2: FIND NEXT GREATER ELEMENT
    for i in range(n - 1, pivot, -1):
        if nums[i] > nums[pivot]:
            #STEP 3: SWAP
            nums[i], nums[pivot] = nums[pivot], nums[i]
            break
    #STEP 4: SORT SUFFIX
    nums[pivot + 1:] = sorted(nums[pivot + 1:])
nums=[1,2,3]
nextPermutation(nums)
print(nums)

#USING MANUAL REVERSE METHOD
def nextPermutation(nums):
        #EDGE CASE
        if len(nums) <= 1:
            return
        n = len(nums)
        #STEP 1: FIND PIVOT
        pivot = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        #EDGE CASE:
        #LARGEST PERMUTATION
        if pivot == -1:
            #REVERSE WHOLE ARRAY
            left = 0
            right = n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return
        #STEP 2: FIND NEXT GREATER ELEMENT
        for i in range(n - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                #STEP 3: SWAP
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        #STEP 4: MANUAL REVERSE SUFFIX
        left = pivot + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
nums=[1,2,3]
nextPermutation(nums)
print(nums)