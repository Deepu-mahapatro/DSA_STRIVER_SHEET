#LONGEST SUB ARRAY WITH GIVEN SUM K (POSITIVE NUMBERS)
#THE PURPOSE OF LONGEST SUB ARRAY WITH GIVEN SUM K IS:
#TO FIND THE LENGTH OF THE LONGEST CONTIGUOUS SUB ARRAY
#WHOSE SUM IS EXACTLY EQUAL TO K.
#PROCESS:
#USE TWO POINTERS (LEFT AND RIGHT) TO FORM A SLIDING WINDOW.
#INITIALIZE LEFT = 0, RIGHT = 0.
#KEEP TRACK OF CURRENT WINDOW SUM.
#EXPAND WINDOW BY MOVING RIGHT POINTER.
#ADD CURRENT ELEMENT TO WINDOW SUM.
#IF WINDOW SUM BECOMES GREATER THAN K:
#SHRINK WINDOW FROM LEFT SIDE.
#KEEP REMOVING LEFT ELEMENTS UNTIL SUM <= K.
#IF WINDOW SUM BECOMES EQUAL TO K:
#CALCULATE CURRENT WINDOW LENGTH.
#UPDATE MAXIMUM LENGTH FOUND SO FAR.
#CONTINUE UNTIL RIGHT REACHES END OF ARRAY.
#RETURN MAXIMUM LENGTH.
#CONDITION:
#IF CURRENT_SUM > K:
#MOVE LEFT POINTER FORWARD
#AND SUBTRACT LEFT ELEMENT FROM SUM.
#IF CURRENT_SUM == K:
#UPDATE ANSWER.
#IMPORTANT RULES:
#THIS APPROACH WORKS ONLY FOR POSITIVE NUMBERS.
#ADDING A NEW ELEMENT ALWAYS INCREASES THE SUM.
#REMOVING AN ELEMENT ALWAYS DECREASES THE SUM.
#USE SLIDING WINDOW FOR O(N) SOLUTION.
#TRACK WINDOW SUM CONTINUOUSLY.
#TRACK MAXIMUM LENGTH THROUGHOUT TRAVERSAL.
#WHY THIS WORKS:
#SINCE ALL NUMBERS ARE POSITIVE:
#WINDOW SUM CAN ONLY INCREASE WHEN RIGHT MOVES.
#WINDOW SUM CAN ONLY DECREASE WHEN LEFT MOVES.
#THEREFORE WE CAN ADJUST THE WINDOW EFFICIENTLY
#WITHOUT RECHECKING PREVIOUS SUB ARRAYS.
#EACH ELEMENT IS VISITED AT MOST TWICE.
#THIS GIVES O(N) TIME COMPLEXITY.
#WINDOW MOVEMENT LOGIC:
#IF SUM < K:
#EXPAND WINDOW
#MOVE RIGHT
#IF SUM > K:
#SHRINK WINDOW
#MOVE LEFT
#IF SUM == K:
#UPDATE ANSWER
#THEN CONTINUE EXPANDING
#EXAMPLE:
#ARRAY:
# [1,2,3,1,1,1,1]
# K = 6
#WINDOW:
# [1,2,3]
# SUM = 6
# LENGTH = 3
#WINDOW:
# [3,1,1,1]
# SUM = 6
# LENGTH = 4
#ANSWER:
# 4
#EDGE CASES:
#EMPTY ARRAY:
#ANSWER = 0
#SINGLE ELEMENT EQUAL TO K:
#ANSWER = 1
#SINGLE ELEMENT NOT EQUAL TO K:
#ANSWER = 0
#NO SUB ARRAY WITH SUM K:
#ANSWER = 0
#WHOLE ARRAY SUM = K:
#ANSWER = ARRAY LENGTH
#MULTIPLE VALID SUB ARRAYS:
#RETURN THE LONGEST LENGTH
#ALL ELEMENTS GREATER THAN K:
#ANSWER = 0
#IMPORTANT LIMITATION:
#THIS SLIDING WINDOW APPROACH ONLY WORKS
#WHEN ALL ELEMENTS ARE POSITIVE.
#IF NEGATIVE NUMBERS EXIST:
#SLIDING WINDOW FAILS
#BECAUSE SUM MAY INCREASE OR DECREASE UNPREDICTABLY.
#FOR NEGATIVE NUMBERS:
#USE PREFIX SUM + HASHMAP APPROACH.
#TIME COMPLEXITY:
#O(N)
#SPACE COMPLEXITY:
#O(1)
#FINAL IDEA:
#MAINTAIN A MOVING WINDOW USING TWO POINTERS.
#EXPAND THE WINDOW WHEN SUM IS SMALLER THAN K.
#SHRINK THE WINDOW WHEN SUM IS GREATER THAN K.
#WHEN SUM BECOMES EXACTLY K,
#UPDATE THE MAXIMUM WINDOW LENGTH.
#CONTINUE UNTIL ENTIRE ARRAY IS PROCESSED.

#USING BRUTE FORCE APPROACH
def longest_sub(arr, k):
    n = len(arr)
    longest = 0
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += arr[end]
            if current_sum == k:
                longest = max(longest, end - start + 1)
    return longest
print(longest_sub([1,2,3,1,1,1,1],6))


#OPTIMAL SLIDING WINDOW METHOD
def longest_sub(arr, k):
    left = 0
    current_sum = 0
    longest = 0
    for right in range(len(arr)):
        current_sum += arr[right]
        while current_sum > k:
            current_sum -= arr[left]
            left += 1
        if current_sum == k:
            length = right - left + 1
            longest = max(longest, length)
    return longest
print(longest_sub([1,2,3,1,1,1,1],6))

#PREFIX + HASHMAP METHOD
def longest_sub(arr, k):
    prefix_map = {}
    current_sum = 0
    longest = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum == k:
            longest = i + 1
        remaining = current_sum - k
        if remaining in prefix_map:
            length = i - prefix_map[remaining]
            longest = max(longest, length)
        if current_sum not in prefix_map:
            prefix_map[current_sum] = i
    return longest
print(longest_sub([1,2,3,1,1,1,1],6))

#BEST METHOD
def longest_sub(arr, k):
    left = 0
    current_sum = 0
    longest = 0
    for right in range(len(arr)):
        current_sum += arr[right]
        while current_sum > k:
            current_sum -= arr[left]
            left += 1
        if current_sum == k:
            longest = max(
                longest,
                right - left + 1
            )
    return longest
print(longest_sub([1,2,3,1,1,1,1,1],6))