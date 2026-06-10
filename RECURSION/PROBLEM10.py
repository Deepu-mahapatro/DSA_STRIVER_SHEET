#LETTER COMBINATIONS OF A PHONE NUMBER
#THE PURPOSE OF LETTER COMBINATIONS IS:
#TO GENERATE ALL POSSIBLE LETTER COMBINATIONS
#THAT CAN BE FORMED FROM THE GIVEN PHONE DIGITS.
#PROCESS:
#START FROM THE FIRST DIGIT.
#GET ALL LETTERS MAPPED TO THAT DIGIT.
#PICK ONE LETTER.
#MOVE TO THE NEXT DIGIT.
#PICK ONE LETTER FROM THAT DIGIT.
#CONTINUE UNTIL ALL DIGITS ARE PROCESSED.
#STORE THE COMPLETE COMBINATION.
#BACKTRACK AND TRY OTHER LETTER CHOICES.
#REPEAT UNTIL ALL POSSIBILITIES ARE GENERATED.
#PHONE MAPPING:
    #2 -> abc
    #3 -> def
    #4 -> ghi
    #5 -> jkl
    #6 -> mno
    #7 -> pqrs
    #8 -> tuv
    #9 -> wxyz
#CONDITION:
    #ONE LETTER MUST BE CHOSEN
    #FROM EACH DIGIT.
#IMPORTANT RULES:
    #PROCESS DIGITS FROM LEFT TO RIGHT.
    #TRY EVERY POSSIBLE LETTER.
    #GENERATE ALL VALID COMBINATIONS.
    #USE EACH DIGIT EXACTLY ONCE.
    #COMBINATION LENGTH MUST EQUAL
    #NUMBER OF DIGITS.
#BASE CASE:
    #IF CURRENT COMBINATION LENGTH
    #EQUALS TOTAL DIGITS,
    #STORE THE COMBINATION.
#WHY THIS WORKS:
    #EVERY DIGIT PROVIDES MULTIPLE CHOICES.
    #BACKTRACKING EXPLORES ALL CHOICES.
    #NO COMBINATION IS MISSED.
    #ALL POSSIBLE RESULTS ARE GENERATED.
#EDGE CASES:
    #EMPTY STRING -> RETURN []
    #SINGLE DIGIT -> RETURN ALL LETTERS OF THAT DIGIT
    #DIGIT 7 OR 9 -> HAS 4 LETTERS
    #MULTIPLE DIGITS -> GENERATE CARTESIAN PRODUCT
    #OF ALL LETTER SETS
#EXAMPLE:
    #INPUT = "23"
    #2 -> abc
    #3 -> def
    #OUTPUT:
    #ad ae af
    #bd be bf
    #cd ce cf
#FINAL IDEA:
#FOR EACH DIGIT, TRY EVERY POSSIBLE LETTER,
#BUILD THE COMBINATION RECURSIVELY,
#AND STORE IT WHEN ALL DIGITS ARE USED.

#BRUTE FORCE METHOD
def letterCombination(digits):
    #EDGE CASE
    if not digits:
        return []
    phone={
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }
    result=[]
    def backtrack(index,current):
        #BASE CASE
        #COMBINATION FOUND
        if index==len(digits):
            result.append(current)
            return
        #GET LETTERS OF CURRENT DIGITS
        letters=phone[digits[index]]
        #TRY EVERY LETTER
        for ch in letters:
            #ADD LETTER
            backtrack(index+1,current+ch)
    backtrack(0,"")
    return result
digits="23"
print(letterCombination(digits))

#BETTER VERSION OPTIMIZED BRUTE FORCE
def letterCombination(digits):
    #EDGE CASE
    if not digits:
        return []
    phone={
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }
    result=[]
    path=[]
    def backtrack(index):
        #BASE CASE
        #COMBINATION FOUND
        if index==len(digits):
            result.append("".join(path))
            return
        #GET LETTERS OF CURRENT DIGITS
        letters=phone[digits[index]]
        #TRY EVERY LETTER
        for ch in letters:
            #CHOOSE
            path.append(ch)
            #EXPLORE
            backtrack(index+1)
            #UNDO CHOICE
            path.pop()
    backtrack(0)
    return result
digits="23"
print(letterCombination(digits))
