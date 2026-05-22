#FIND MISSING NUMBER

nums=[1,2,3,5]
n=5
if n<=0:
    print("invalid number")
elif len(nums)!=n-1:
    print("invalid array")
else:
    result=n*(n+1)//2
    sum=sum(nums)
    missing=result-sum
print("missing number:",missing)  

#USING LOOP METHOD
nums=[1,2,3,5]
n=5
if n<=0:
    print("invalid array")
else:
    for i in range(1,n+1):
        if i not in nums:
            print("missing number:",i)
            
#USING HASH SET METHOD
nums=[1,2,3,5]
n=5
if n<=0:
    print("invalid array")
else:
    hash_set=set(nums)
    for i in range(1,n+1):
        if i not in hash_set:
            print("missing number:",i)
            
#USING XOR METHOD
arr = [1,2,4,5]
n = 5
# Edge Case
if n <= 0:
    print("Invalid n")
elif len(arr) != n - 1:
    print("Invalid array size")
else:
    xor1 = 0
    xor2 = 0
    # XOR from 1 to n
    for i in range(1, n + 1):
        xor1 ^= i
    # XOR array elements
    for num in arr:
        xor2 ^= num
    missing = xor1 ^ xor2
    print("Missing Number:", missing)