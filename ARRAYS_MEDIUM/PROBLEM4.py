#COUNT SUB ARRAYS WITH GIVEN SUM
#A SUB ARRAY MEANS THE CONTINUOUS PART OF AN ARRAY
#ELEMENTS MUST STAY TOGETHER ORDER CANNOT CHANGE
#FOR A GIVEN ARRAY AND A TARGET SUM
#FIND HOW MANY SUB ARRAYS HAVE TOTAL SUM EXACTLY EQUAL TO K
#WE USE PREFIX CONCEPT HERE
#PREFIX : RUNNING TOTAL FROM START UP TO CURRENT POSITION

#BRUTE FORCE APPROACH
def count_sub(arr,target):
    #EDGE CASE: EMPTY ARRAY
    if arr==[]:
        return 0
    #STORE TOTAL COUNT
    count=0
    #OUTER LOOP -> STARTING INDEX
    for start in range(len(arr)):
        #STORE RUNNING SUM
        current_sum=0
        #INNER LOOP -> ENDING INDEX
        for end in range(start,len(arr)):
            #ADD CURRENT ELEMENT
            current_sum+=arr[end]
            #CHECK IF SUM MATCHES TARGET
            if current_sum==target:
                count+=1
    return count
arr=[1,2,1]
target=2
print(count_sub(arr,target))

#USING PREFIX SUM +HASH MAP
def count_sub(arr, target):
    # EDGE CASE: EMPTY ARRAY
    if arr == []:
        return 0
    # HASHMAP TO STORE:
    # PREFIX_SUM -> FREQUENCY
    prefix_count = {}
    # VERY IMPORTANT:
    # PREFIX SUM 0 APPEARS ONCE INITIALLY
    #WITHOUT THIS SUB ARRAY FROM INDEX 0 WILL NOT BE COUNTED
    prefix_count[0] = 1
    # STORE RUNNING SUM
    current_sum = 0
    # STORE ANSWER
    count = 0
    # TRAVERSE ARRAY
    for num in arr:
        # UPDATE RUNNING SUM
        current_sum += num
        # FIND REQUIRED PREFIX SUM
        needed_sum = current_sum - target
        # IF REQUIRED SUM EXISTS
        # ADD ITS FREQUENCY
        if needed_sum in prefix_count:
            count += prefix_count[needed_sum]
        # STORE CURRENT PREFIX SUM
        if current_sum in prefix_count:
            prefix_count[current_sum] += 1
        else:
            prefix_count[current_sum] = 1
    return count
# TEST
arr = [1, 2, 3]
target = 3
print(count_sub(arr, target))

# SLIDING WINDOW (FOR POSITIVE NUMBERS)
def count_sub(arr, target):
    # EDGE CASE
    if arr == []:
        return 0
    left = 0
    current_sum = 0
    count = 0
    # EXPAND WINDOW
    for right in range(len(arr)):
        # ADD RIGHT ELEMENT
        current_sum += arr[right]
        # SHRINK WINDOW IF SUM TOO LARGE
        while current_sum > target and left <= right:
            current_sum -= arr[left]
            left += 1
        # CHECK TARGET
        if current_sum == target:
            count += 1
    return count
# TEST
arr = [1, 2, 1, 1, 1]
target = 3
print(count_sub(arr, target))

# RECURSIVE METHOD
def count_from_index(arr, target, start, current_sum):
    # IF SUM MATCHES TARGET
    count = 1 if current_sum == target else 0
    # TRY NEXT ELEMENTS
    for i in range(start, len(arr)):
        count += count_from_index(
            arr,
            target,
            i + 1,
            current_sum + arr[i]
        )
    return count
def count_sub(arr, target):
    # EDGE CASE
    if arr == []:
        return 0
    total = 0
    # START FROM EVERY INDEX
    for i in range(len(arr)):
        total += count_from_index(arr, target, i + 1, arr[i])
    return total
# TEST
arr = [1, 2, 1]
target = 3
print(count_sub(arr, target))