nums = [1,2,3,4,5]
k = 2

n = len(nums)

# Edge case
if n == 0:
    print(nums)

else:

    # If k is bigger than array size
    k = k % n

    # Reverse helper function
    def reverse(left, right):

        while left < right:

            nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right -= 1

    # Reverse entire array
    reverse(0, n - 1)

    # Reverse first k elements
    reverse(0, k - 1)

    # Reverse remaining elements
    reverse(k, n - 1)

    print(nums)