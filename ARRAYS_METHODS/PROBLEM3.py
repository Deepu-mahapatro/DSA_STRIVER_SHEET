# FRUIT INTO BASKETS
# CORE IDEA:
# FIND THE LONGEST SUBARRAY WITH
# AT MOST 2 DISTINCT FRUIT TYPES# PROCESS:
# EXPAND THE WINDOW USING RIGHT
# ADD CURRENT FRUIT TO FREQUENCY MAP
# CHECK NUMBER OF DISTINCT TYPES
# IF TYPES > 2
# SHRINK WINDOW FROM LEFT
# REMOVE FRUITS UNTIL TYPES <= 2
# UPDATE MAXIMUM WINDOW LENGTH
# CONTINUE UNTIL ARRAY ENDS
# EDGE CASES:
# EMPTY ARRAY -> RETURN 0
# ONE FRUIT -> RETURN 1
# ALL SAME FRUITS -> RETURN ARRAY LENGTH
# EXACTLY 2 TYPES -> RETURN ARRAY LENGTH
# MORE THAN 2 TYPES -> SHRINK WINDOW
# EVERY FRUIT DIFFERENT -> ANSWER IS 2
# KEY OBSERVATION:
# WINDOW MUST ALWAYS CONTAIN
# AT MOST 2 DISTINCT TYPES
# CONCLUSION:
# EXPAND WHEN VALID
# SHRINK WHEN INVALID
# STORE MAXIMUM WINDOW SIZE
# RETURN FINAL ANSWER

#USING BRUTE FORCE APPROACH
def total_fruit(fruits):
    if not fruits:
        return 0
    n=len(fruits)
    answer=0
    for start in range(n):
        fruit_types=set()
        for end in range(start,n):
            fruit_types.add(fruits[end])
            #MORE THAN 2 FRUIT TYPES
            if len(fruit_types)>2:
                break
            answer=max(answer,end-start+1)
    return answer
fruits=[1,2,1,2,3]
print(total_fruit(fruits))


#USING SLIDING WINDOW METHOD
def total_fruit(fruits):
    if not fruits:
        return 0
    left=0
    answer=0
    current_count={}
    for right in range(len(fruits)):
        fruit=fruits[right]
        current_count[fruit]=current_count.get(fruit,0)+1
        while len(current_count)>2:
            left_fruit=fruits[left]
            current_count[left_fruit]-=1
            if current_count[left_fruit]==0:
                del current_count[left_fruit]
            left +=1
        answer=max(answer,right-left+1)
    return answer
fruits=[1,2,1,2,3]
print(total_fruit(fruits))
