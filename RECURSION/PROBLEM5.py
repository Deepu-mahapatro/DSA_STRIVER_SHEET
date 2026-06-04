# GENERATE PARENTHESES
# TO GENERATE ALL VALID
# COMBINATIONS OF N PAIRS
# OF PARENTHESES
# CORE IDEA:
      # BUILD THE STRING RECURSIVELY
      # ADD "(" IF OPEN BRACKETS
      # ARE STILL AVAILABLE
      # ADD ")" ONLY IF THERE IS
      # AN UNMATCHED "("
      # STORE THE STRING WHEN
      # LENGTH BECOMES 2 * N
# EDGE CASES:
      # N = 0 -> [""]
      # N = 1 -> ["()"]
      # OPEN_COUNT CANNOT
      # EXCEED N
      # CLOSE_COUNT CANNOT
      # EXCEED OPEN_COUNT
# KEY OBSERVATION:
      # "(" CAN BE ADDED IF
      # OPEN_COUNT < N
      # ")" CAN BE ADDED IF
      # CLOSE_COUNT < OPEN_COUNT
      # THIS GUARANTEES ONLY
      # VALID PARENTHESES
      # ARE GENERATED
# CONCLUSION:
# BUILD THE STRING ONE
# CHARACTER AT A TIME.
# ALWAYS TRY "("
# WHEN AVAILABLE.
# TRY ")" ONLY
# WHEN VALID.
# STORE EVERY COMPLETE
# VALID STRING OF
# LENGTH 2 * N.

#USING STANDARD BACKTRACKING METHOD
def generate(n):
    #EDGE CASE
    if n<=0:
        return []
    result=[]
    #FOR BACKTRACKING
    def backtrack(curr,open,close):
        #IF VALID LENGTH
        if len(curr)==n*2:
            result.append(curr)
            #BACKTRACK
            return
        #TO ADD "(" IF
        if open<n:
            backtrack(curr+"(",open+1,close)
        #TO ADD ")" IF 
        if close<open:
            backtrack(curr+")",open,close+1)
    #SET INPUT VALUES
    backtrack("",0,0)
    return result
print(generate(2))

#RECURSION USING REMAINING OPEN/CLOSE
def generate(n):
    #EDGE CASE
    if n<0:
        return []
    result=[]
    def backtrack(curr,open,close):
        #VALID LENGTH
        if open==0 and close==0:
            result.append(curr)
            #BACKTRACK
            return
        #TO ADD "("
        if open>0:
            backtrack(curr+"(",open-1,close)
        #TO ADD ")"
        if close>open:
            backtrack(curr+")",open,close-1)
        #SET INPUT VALUES
    backtrack("",n,n)
    return result
print(generate(2))

