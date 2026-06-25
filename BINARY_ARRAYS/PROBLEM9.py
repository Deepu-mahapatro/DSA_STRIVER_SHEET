#MINIMUM DAYS TO MAKE M BOUQUETS

#LINEAR SEARCH METHOD
def minDays(bloomDay,m,k):
    if m * k > len(bloomDay):
        return -1
    left = min(bloomDay)
    right = max(bloomDay)
    for day in range(left, right + 1):
        bouquets = 0
        flowers = 0
        for bloom in bloomDay:
            if bloom <= day:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        if bouquets >= m:
            return day
    return -1
bloomDay=[1,10,3,10,2]
m=3
k=1
print(minDays(bloomDay,m,k))


#USING BINARY SEARCH METHOD
def minDays(bloomDay,m,k):
    #EDGE CASE
    #IF TOTAL FLOWERS NEEDED IS MORE THAN AVAILABLE FLOWERS
    if m*k>len(bloomDay):
        return -1
    #BINARY SEARCH RANGE
    left=min(bloomDay)
    right=max(bloomDay)
    answer=-1
    while left<=right:
        mid=(left+right)//2
        #CHECK IF MID IS POSSIBLE
        bouquets=0
        flowers=0
        for bloom in bloomDay:
            #FLOWERS HAS BLOOMED
            if bloom<=mid:
                flowers+=1
                #ENOUGH ADJACENT FLOWERS
                if flowers==k:
                    bouquets+=1
                    #FLOWERS ARE USED
                    flowers=0
            else:
                #ADJACENT BREAKS
                flowers=0
        #BINARY SEARCH DECISION
        if bouquets>=m:
            #STORE POSSIBLE ANSWER
            answer=mid
            #SEARCH FOR A SMALL DAY
            right=mid-1
        else:
            #NEED TO WAIT LONGER
            left=mid+1
    return answer
bloomDay=[1,10,3,10,2]
m=3
k=1
print(minDays(bloomDay,m,k))