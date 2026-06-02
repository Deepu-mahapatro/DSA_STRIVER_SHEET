# PROBLEM: COUNT GOOD NUMBERS
# DEFINITION
# A GOOD NUMBER IS A NUMBER WHERE:
# - EVEN INDICES CONTAIN EVEN DIGITS.
# - ODD INDICES CONTAIN PRIME DIGITS.
# PURPOSE
# FIND THE TOTAL NUMBER OF POSSIBLE GOOD NUMBERS OF LENGTH N.
# ALLOWED DIGITS
# EVEN INDICES
# 0, 2, 4, 6, 8
# TOTAL CHOICES = 5
# ODD INDICES
# 2, 3, 5, 7
# TOTAL CHOICES = 4
# KEY OBSERVATION
# EACH POSITION IS INDEPENDENT.
# THEREFORE, MULTIPLY THE NUMBER OF CHOICES.
# EVEN POSITIONS
# COUNT = (N + 1) // 2
# ODD POSITIONS
# COUNT = N // 2
# FORMULA
# TOTAL GOOD NUMBERS =
# 5^(EVEN_POSITIONS) × 4^(ODD_POSITIONS)
# WHY?
# EACH EVEN POSITION HAS 5 CHOICES.
# EACH ODD POSITION HAS 4 CHOICES.
# MULTIPLY ALL POSSIBLE CHOICES.
# OPTIMIZATION
# USE BINARY EXPONENTIATION FOR LARGE N.
# EDGE CASES
# N = 1
# ONLY ONE EVEN POSITION EXISTS.
# N IS EVEN
# EVEN AND ODD POSITIONS ARE EQUAL.
# N IS ODD
# EVEN POSITIONS GET ONE EXTRA SLOT.
# VERY LARGE N
# USE FAST POWER CALCULATION.
# COMMON MISTAKES
# FORGETTING THAT INDEXING STARTS FROM 0.
# USING WRONG COUNT OF EVEN POSITIONS.
# FORGETTING THAT 0 IS A VALID EVEN DIGIT.
# NOT USING FAST EXPONENTIATION.
# TIME COMPLEXITY
# O(LOG N)
# SPACE COMPLEXITY
# O(LOG N)  -> RECURSIVE POWER
# O(1)      -> ITERATIVE POWER
# GOLDEN FORMULA
# TOTAL GOOD NUMBERS =
# 5^((N + 1) // 2) × 4^(N // 2)

#USING SIMPLE RECURSIVE POWER FUNCTION
def power(x,n):
    #BASE CASE
    if n==0:
        return 1
    #HANDLE NEGATIVE POWER
    if n<0:
        return 1/power(x,-n)
    #RECURSIVE CASE
    return x*power(x,n-1)
#COUNT OF GOOD NUMBERS
def good_numbers(n):
    #EDGE CASE 
    if n<=0:
        return 0
    even_pos=(n+1)//2
    odd_pos=n//2
    return power(5,even_pos)*power(4,odd_pos)
print(good_numbers(4))

#BINARY EXPONENTIATION(DIVIDE AND CONQUER) METHOD
def power(x,n):
    #BASE CASE
    if n==0:
        return 1
    #HANDLE NEGATIVE CASE
    if n<0:
        return 1/power(x,-n)
    #RECURSIVE CASE
    half=power(x,n//2)
    #EVEN POWER
    if n%2==0:
        return half*half
    #ODD POWER
    return x*half*half
def good_numbers(n):
    #EDGE CASE
    if n<=0:
        return 0
    even_pos=(n+1)//2
    odd_pos=n//2
    return power(5,even_pos)*power(4,odd_pos)
print(good_numbers(4))

#USING PURE RECURSION METHOD
def solve(index,n):
    #BASE CASE
    if index==n:
        return 1
    #EVEN INDEX
    if index%2==0:
        return 5*solve(index+1,n)
    #ODD INDEX
    return 4*solve(index+1,n)
#COUNT GOOD NUMBERS
def good_numbers(n):
    #EDGE CASE
    if n<=0:
        return 0
    return solve(0,n)
print(good_numbers(4))