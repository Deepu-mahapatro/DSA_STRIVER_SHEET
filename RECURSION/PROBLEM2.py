#POW(x, n)
#PURPOSE:
#CALCULATE x RAISED TO POWER n.
#EDGE CASE:
#IF n == 0 RETURN 1.
#EDGE CASE:
#IF n < 0 RETURN 1 / POW(x, -n).
#BASE CASE:
#IF n == 0 RETURN 1.
#RECURSIVE STEP:
#CALCULATE HALF = POW(x, n // 2).
#EVEN CASE:
#IF n % 2 == 0
#RETURN HALF × HALF.
#ODD CASE:
#IF n % 2 != 0
#RETURN x × HALF × HALF.
#SMALLER PROBLEM:
#REDUCE n TO n // 2.
#WHY THIS WORKS:
#REUSE THE SAME HALF ANSWER TWICE.
#IMPORTANT RULE:
#ANY NUMBER POWER 0 IS 1.
#IMPORTANT RULE:
#x^(-n) = 1 / (x^n).
#EDGE CASE:
#x = 0 AND n > 0 → RETURN 0.
#EDGE CASE:
#x = 1 → RETURN 1.
#FINAL IDEA:
#DIVIDE EXPONENT BY HALF.
#SOLVE RECURSIVELY.
#HANDLE EVEN AND ODD POWERS.
#TIME COMPLEXITY: O(LOG N)
#SPACE COMPLEXITY: O(LOG N)

#USING N0RML BRUTE FORCE METHOD 
def power(x,n):
    #BASE CASE
    if n==0:
        return 1
    #HANDLE NEGATIVE POWER CASE
    if n<0:
        return 1/power(x,-n)
    #RECURSIVE CASE
    return x*power(x,n-1)
print(power(2,5))

#DIVIDE AND CONQUER METHOD
def power(x,n):
    #BASE CASE
    if n==0:
        return 1
    #HANDLE NEGATIVE POWER
    if n<0:
        return 1/power(x,-n)
    #SOLVE HALF PROBLEM
    half=power(x,n//2)
    #EVEN POWER
    if n%2==0:
        return half*half
    #ODD NUMBER
    else:
        return x*half*half
print(power(2,5))

#ANOTHER SAME METHOD 
def power(x, n):
    # BASE CASE
    if n == 0:
        return 1
    # HANDLE NEGATIVE POWER
    if n < 0:
        return power(1 / x, -n)
    # EVEN POWER
    if n % 2 == 0:
        return power(x * x, n // 2)
    # ODD POWER
    return x * power(x * x, n // 2)
print(power(2,5))