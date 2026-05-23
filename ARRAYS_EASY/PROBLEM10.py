#MAXIMUM CONSECUTIVE ONES
#CONSECUTIVE MEANS CONTINUES(APPEARING ONE AFTER ANOTHER)
#FOR ONES: TEH GIVEN INPUT HAS 0'S AND 1'S 
#FOR THIS WE NEED TO FIND THE MAXIMUM LENGTH
#THE LENGTH MUST REPEATS ONES ONE BY ONE
#FOR EX: 11101->111 ID THE MAX LENGTH
#FOR 1 CONTINUE THE PROCESS
#WHEN 0 APPEARS STOP THE PROCESS
#NOW ABOUT COUNTING ONES TEH CONCEPT IS 
#LONGEST UNINTERRUPTED CHAIN OF ONES
#EDGE CASES:
#FOR EMPTY ARRAY->RETURN 0
#FOR ARRAY OF [0,0,0]->RETURN 0
#FOR SINGLE ELEMENTS [1]->1 AND [0]->0
#FOR TWO EQUAL STREAKS : [1,1,0,0,1,1]
#THE MAXIMUM STREAK 2 AND 2 -> 2

#BRUTE FORCE APPROACH
def max_con(nums):
    curr_count=0
    max_count=0
    for i in nums:
        if i==1:
            curr_count+=1
        if curr_count>max_count:
            max_count=curr_count
        else:
            curr_count=0
    return max_count
nums=[1,1,1,1,0,1,1]
print(max_con(nums))

#USING STRING SPLIT METHOD
def max_con(nums):
    #CONVERTS ARRAY TO STRING 
    s=''.join(map(str,nums))  
    #SPLIT WHEN '0' APPEARS
    #AS ['1111','11']
    groups=s.split('0')
    max_count=0
    for i in groups:
        #FIND MAX COUNT AS 
        #I='1111'->LEN(I)->4
        #INITIAL MAX_COUNT=0
        #MAX_COUNT=MAX(0,4)->4
        #I='11'->MAX_COUNT=2
        #AMONG THIS MAX(2,4)->4
        max_count=max(max_count,len(i))
    return max_count
nums=[1,1,1,1,0,1,1]
print(max_con(nums))