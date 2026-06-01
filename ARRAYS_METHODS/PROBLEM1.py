# LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
#THE PURPOSE OF LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS IS:
#TO FIND THE LENGTH OF THE LONGEST CONTINUOUS SUBSTRING
#CONTAINING ONLY UNIQUE CHARACTERS.
#PROCESS:
#USE A SLIDING WINDOW.
#EXPAND WINDOW WHILE CHARACTERS ARE UNIQUE.
#CHECK WHETHER CURRENT CHARACTER ALREADY EXISTS IN WINDOW.
#IF DUPLICATE IS FOUND:
#SHRINK WINDOW FROM THE LEFT.
#REMOVE CHARACTERS UNTIL DUPLICATE IS REMOVED.
#CONTINUE EXPANDING WINDOW.
#UPDATE MAXIMUM WINDOW LENGTH.
#RESULT BECOMES THE LONGEST VALID SUBSTRING LENGTH.
#CONDITION:
#CURRENT CHARACTER MUST NOT ALREADY EXIST IN THE WINDOW.
#THAT GUARANTEES ALL CHARACTERS REMAIN UNIQUE.
#IMPORTANT RULES:
#SUBSTRING MUST BE CONTINUOUS.
#ONLY UNIQUE CHARACTERS ARE ALLOWED.
#DUPLICATE CHARACTER MAKES WINDOW INVALID.
#USE A SET FOR FAST DUPLICATE CHECKING.
#USE WHILE, NOT IF, TO REMOVE DUPLICATES.
#WHY THIS WORKS:
#THE WINDOW ALWAYS CONTAINS UNIQUE CHARACTERS.
#EXPANDING HELPS FIND LARGER VALID SUBSTRINGS.
#SHRINKING REMOVES DUPLICATES EFFICIENTLY.
#THIS AVOIDS RECHECKING PREVIOUS CHARACTERS.
#EDGE CASES:
#EMPTY STRING -> ANSWER = 0
#SINGLE CHARACTER -> ANSWER = 1
#ALL UNIQUE CHARACTERS -> ANSWER = LENGTH OF STRING
#ALL SAME CHARACTERS -> ANSWER = 1
#DUPLICATE MAY REQUIRE MULTIPLE REMOVALS
#SPACES AND NUMBERS ARE ALSO CHARACTERS
#FINAL IDEA:
#KEEP A WINDOW OF UNIQUE CHARACTERS.
#EXPAND FOR UNIQUE CHARACTERS.
#SHRINK FOR DUPLICATE CHARACTERS.
#CONTINUOUSLY TRACK THE MAXIMUM VALID WINDOW LENGTH.

#USING BRUTE FORCE APPROACH
def longest_substring(s):
    #EDGE CASE: EMPTY STRING
    if not s:
        return 0
    max_length=0
    n=len(s)
    for i in range(n):
        seen=set()
        for j in range(i,n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_length=max(max_length,j-i+1)
    return max_length
s="abcabcbb"
print(longest_substring(s))

#USING SLIDING WINDOW METHOD
def longest_substring(s):
    #EDGE CASE: EMPTY STRING
    if not s:
        return 0
    seen=set()
    left=0
    max_length=0
    for right in range(len(s)):
        #REMOVE DUPLICATES
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        #ADD CURRENT CHARACTER
        seen.add(s[right])
        #UPDATE MAX_LENGTH
        max_length=max(max_length,right-left+1)
    return max_length
s="abcabcbb"
print(longest_substring(s))

#USING HASHMAP AND JUMP METHOD
def longest_substring(s):
    #EDGE CASE: EMPTY STRING
    if not s:
        return 0
    n=len(s)
    left=0
    max_length=0
    seen={}
    for right in range(n):
        current_char=s[right]
        #IF CHARACTER IS DUPLICATE
        if current_char in seen and seen[current_char]>=left:
            #JUMP LEFT POINTER INSTEAD OF REMOVE
            left=seen[current_char]+1
        #STORE CURRENT CHARACTER
        seen[current_char]=right
        #UPDATE MX_LENGTH
        max_length=max(max_length,right-left+1)
    return max_length
s="abcabcbb"
print(longest_substring(s))