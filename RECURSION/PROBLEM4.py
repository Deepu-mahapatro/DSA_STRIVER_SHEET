# GENERATE BINARY STRINGS WITHOUT CONSECUTIVE 1s
# TO GENERATE ALL BINARY STRINGS
# OF LENGTH N WITHOUT ADJACENT 1s
# CORE IDEA:
      # BUILD THE STRING RECURSIVELY
      # ADD 0 AT ANY TIME
      # ADD 1 ONLY IF THE PREVIOUS
      # CHARACTER IS NOT 1
      # STORE THE STRING WHEN
      # LENGTH BECOMES N
# EDGE CASES:
      # N = 0 -> [""]
      # N = 1 -> ["0","1"]
      # LEADING 0s ARE ALLOWED
      # NO CONSECUTIVE 1s ALLOWED
# KEY OBSERVATION:
      # 0 IS ALWAYS SAFE
      # 1 CAN ONLY FOLLOW 0
      # OR AN EMPTY STRING
      # USE RECURSION TO EXPLORE
      # ALL VALID CHOICES
# CONCLUSION:
# BUILD THE STRING ONE CHARACTER
# AT A TIME.
# ALWAYS TRY 0.
# TRY 1 ONLY WHEN VALID.
# STORE EVERY COMPLETE STRING
# OF LENGTH N.

#BETTER VERSION TO SOLVE IT
def binary_strings(n):
    result=[]
    def traverse(current):
        #BASE CASE
        if len(current)==n:
            result.append(current)
            return
        #ADD ZEROS 
        traverse(current+"0")
        #ADD ONE BY CHECK CONDITION
        if not current or current[-1]!="1":
            traverse(current+"1")
    traverse("")
    return result
print(binary_strings(3))

#USING PREVIOUS VERSION
def binary_strings(n):
    result=[]
    def traverse(current,pre_one):
        #BASE CASE
        if len(current)==n:
            result.append(current)
            return
        #ADD ZEROS (FALSE LAST CHARACTER IS NOT 1)
        traverse(current+"0",False)
        #ADD ONE IF PREVIOUS IS NOT 1 (LAST CHAR IS 1)
        if not pre_one:
            traverse(current+"1",True)
    traverse("",False)
    return result
print(binary_strings(3))