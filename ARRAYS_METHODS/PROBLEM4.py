#LONGEST REPEATING CHARACTER REPLACEMENT
# CORE IDEA:
# FIND THE LONGEST SUBSTRING THAT CAN BE
# MADE OF THE SAME CHARACTER
# AFTER REPLACING AT MOST K CHARACTERS
# PROCESS:
# EXPAND THE WINDOW USING RIGHT POINTER
# ADD CURRENT CHARACTER TO FREQUENCY MAP
# TRACK THE HIGHEST FREQUENCY CHARACTER
# CALCULATE CURRENT WINDOW SIZE
# FIND REQUIRED REPLACEMENTS
# REQUIRED REPLACEMENTS =
# WINDOW_SIZE - MAX_FREQUENCY
# IF REQUIRED REPLACEMENTS > K
# SHRINK WINDOW FROM LEFT
# REMOVE LEFT CHARACTER FROM FREQUENCY MAP
# MOVE LEFT POINTER FORWARD
# CONTINUE UNTIL WINDOW BECOMES VALID
# UPDATE MAXIMUM WINDOW LENGTH
# CONTINUE UNTIL STRING ENDS
# EDGE CASES:
# EMPTY STRING -> RETURN 0
# SINGLE CHARACTER -> RETURN 1
# ALL SAME CHARACTERS -> RETURN STRING LENGTH
# K = 0 -> FIND LONGEST REPEATING BLOCK
# K GREATER THAN STRING LENGTH -> RETURN STRING LENGTH
# ALL CHARACTERS DIFFERENT -> ANSWER DEPENDS ON K
# WINDOW NEVER NEEDS SHRINKING -> RETURN FULL LENGTH
# KEY OBSERVATION:
# KEEP THE MOST FREQUENT CHARACTER
# IN THE CURRENT WINDOW
# CHANGE ALL OTHER CHARACTERS
# INTO THAT CHARACTER
# IMPORTANT FORMULA:
# REPLACEMENTS_NEEDED =
# WINDOW_SIZE - MAX_FREQUENCY
# VALID WINDOW:
# REPLACEMENTS_NEEDED <= K
# INVALID WINDOW:
# REPLACEMENTS_NEEDED > K
# CONCLUSION:
# EXPAND WHEN WINDOW IS VALID
# SHRINK WHEN WINDOW IS INVALID
# STORE MAXIMUM VALID WINDOW SIZE
# RETURN FINAL ANSWER

#USING BRUTE FORCE APPROACH
def char_replacement(s,k):
    #EDGE CASE
    if not s:
        return ""
    result=0
    for start in range(len(s)):
        freq={}
        for end in range(start,len(s)):
            char=s[end]
            freq[char]=freq.get(char,0)+1
            max_freq=max(freq.values())
            window_size=end-start+1
            replacement_needed=window_size-max_freq
            if replacement_needed<=k:
                result=max(result,window_size)
    return result
s="AAABC"
print(char_replacement(s,2))            

#USING SLIDING WINDOW
def char_replacement(s,k):
    #EDGE CASE
    if not s:
        return ""
    #LEFT POINTER OF SLIDING WINDOW
    left=0
    #STORES MAXIMUM VALID WINDOW
    result=0
    #LENGTH OF THE STRING
    n=len(s)
    #FREQUENCY COUNT
    freq={}
    #STORES HIGHEST FREQUENCY COUNT
    max_freq=0
    #EXPAND WINDOW USING RIGHT POINTER
    for right in range(n):
        #CURRENT CHARACTER
        char=s[right]
        #FREQUENCY COUNT
        freq[char]=freq.get(char,0)+1
        #UPDATE MAXIMUM FREQUENCY
        max_freq=max(max_freq,freq[char])
        #CURRENT WINDOW SIZE
        window_size=right-left+1
        #IF REQUIRED REPLACEMENTS EXCEED K
        #SHRINK WINDOW FROM LEFT SIDE
        while window_size-max_freq>k:
            #REMOVE LEFT CHARACTER FREQUENCY
            freq[s[left]]-=1
            #MOVE LEFT FORWARD
            left+=1
            #RECALCULATE THE WINDOW SIZE
            window_size=right-left+1
        #UPDATE ANSWER WITH LARGEST VALID WINDOW
        result=max(result,window_size)
    #RETURN LONGEST VALID WINDOW LENGTH
    return result
s="AAABC"
print(char_replacement(s,2))