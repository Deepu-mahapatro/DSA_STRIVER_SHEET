#NUMBER OF SUBSTRINGS CONTAIN ALL THREE CHARACTERS
#SLIDING WINDOW
#CORE IDEA:
#FIND A WINDOW
#CONTAINING
#a,b,c
#KEY OBSERVATION:
#ONCE WINDOW
#HAS a,b,c
#ADDING MORE
#CHARACTERS
#STILL KEEPS
#IT VALID
#SO COUNT ALL
#SUCH SUBSTRINGS
#AT ONCE
#FORMULA:
#ANSWER+=
#n-right
#PROCESS:
#EXPAND RIGHT
#UNTIL WINDOW
#BECOMES VALID
#COUNT:
#n-right
#SHRINK LEFT
#TO FIND MORE
#VALID WINDOWS
#EDGE CASE:
#STRING LENGTH
#LESS THAN 3
#NO POSSIBLE
#ANSWER
#EDGE CASE:
#MISSING ANY OF
#a,b,c
#WINDOW NEVER
#BECOMES VALID
# #ANSWER=0
#EDGE CASE:
#MULTIPLE SAME
#CHARACTERS
#FREQUENCY
#HELPS TRACK
#VALID WINDOW
#TIME:
#O(n)
#SPACE:
#O(1)

#BRUTE FORCE APPROACH
def numberOfSubstring(s):
    n=len(s)
    count=0
    for i in range(n):
        for j in range(i,n):
            sub=s[i:j+1]
            if 'a' in sub and 'b' in sub and 'c' in sub:
                count+=1
    return count
s="abcabcabc"
print(numberOfSubstring(s))


#LAST SEEN POSITION METHOD
def numberOfSubstring(s):
    last=[-1,-1,-1]
    count=0
    for i in range(len(s)):
        last[ord(s[i])-ord('a')]=i
        count+=min(last)+1
    return count
s="abcabcabc"
print(numberOfSubstring(s))

#USING SLIDING WINDOW CONCEPT 
def numberOfSubstring(s):
    left=0
    count=0
    n=len(s)
    freq={'a':0,'b':0,'c':0}
    for right in range(n):
        freq[s[right]]+=1
        while freq['a']>0 and freq['b']>0 and freq['c']>0:
            count+=n-right
            freq[s[left]]-=1
            left+=1
    return count
s="abcabcabc"
print(numberOfSubstring(s))