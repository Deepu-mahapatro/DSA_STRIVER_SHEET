#KOKO EATING BANANAS

#USING LINEAR SEARCH METHOD
def minEatingSpeed(piles,h):
    for speed in range(1,max(piles)+1):
        hours=0
        for pile in piles:
            hours+=(pile+speed-1)//speed
        if hours<=h:
            return speed
piles=[3,6,7,11]
h=8
print(minEatingSpeed(piles,h))


#USING BINARY SEARCH METHOD (FOR INTEGERS)
def minEatingSpeed(piles,h):
    if not piles:
        return 0
    #MINIMUM POSSIBLE SPEED
    left=1
    #MAXIMUM POSSIBLE SPEED 
    right=max(piles)
    #BINARY SEARCH ON ANSWER
    while left<=right:
        #GUESS A SPEED
        mid=(left+right)//2
        #CALCULATE TOTAL HOURS NEEDED
        hours=0
        for pile in piles:
            #CEILING DIVISION (FOR INTEGERS)
            hours+=(pile+mid-1)//mid
        #IF KOKO CAN FINISH WITHIN 1 HOUR
        if hours<=h:
            #FOR MINIMUM SPEED SEARCH LEFT SIDE
            right=mid-1
        else:
            #MID IS TOO LOW SEARCH ON RIGHT SIDE
            left=mid+1
        #LEFT WILL POINT TO FIRST VALID SPEED
    return left
piles=[3,6,7,11]
h=8
print(minEatingSpeed(piles,h))


#USING BINARY SEARCH METHOD (FOR FLOATING POINTS)
import math 
def minEatingSpeed(piles,h):
    if not piles:
        return 0
    #MINIMUM POSSIBLE SPEED
    left=1
    #MAXIMUM POSSIBLE SPEED 
    right=max(piles)
    #BINARY SEARCH ON ANSWER
    while left<=right:
        #GUESS A SPEED
        mid=(left+right)//2
        #CALCULATE TOTAL HOURS NEEDED
        hours=0
        for pile in piles:
            #CEILING DIVISION
            hours+=math.ceil(pile/mid)
        #IF KOKO CAN FINISH WITHIN 1 HOUR
        if hours<=h:
            #FOR MINIMUM SPEED SEARCH LEFT SIDE
            right=mid-1
        else:
            #MID IS TOO LOW SEARCH ON RIGHT SIDE
            left=mid+1
        #LEFT WILL POINT TO FIRST VALID SPEED
    return left
piles=[3,6,7,11]
h=8
print(minEatingSpeed(piles,h))