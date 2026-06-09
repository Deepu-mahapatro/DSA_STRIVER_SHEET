# MAXIMUM POINTS YOU CAN OBTAIN FROM CARDS
# CORE IDEA:
      # YOU CAN ONLY PICK CARDS FROM THE START OR END
      # PICKING K CARDS MEANS LEAVING (N-K) CARDS
      # THE LEFTOVER CARDS ALWAYS FORM A CONTIGUOUS SUBARRAY
      # FIND THE MINIMUM SUM SUBARRAY OF LENGTH (N-K)
      # ANSWER = TOTAL SUM - MINIMUM SUBARRAY SUM
# WHY THIS WORKS:
      # TOTAL SUM = PICKED CARDS + LEFTOVER CARDS
      # TO MAXIMIZE PICKED CARDS
      # WE MUST MINIMIZE LEFTOVER CARDS
# APPROACH:
      # CALCULATE TOTAL SUM
      # FIND WINDOW SIZE = N-K
      # FIND FIRST WINDOW SUM
      # SLIDE WINDOW THROUGH ARRAY
      # TRACK MINIMUM WINDOW SUM
      # RETURN TOTAL SUM - MINIMUM WINDOW SUM
# EDGE CASES:
      # K == N
            # TAKE ALL CARDS
            # RETURN TOTAL SUM
      # K == 0
            # TAKE NO CARDS
            # RETURN 0
      # ARRAY SIZE = 1
      # ALL ELEMENTS SAME
# INTUITION:
      # TAKE K CARDS
      # LEAVE N-K CARDS
      # FIND SMALLEST N-K SUBARRAY
      # REMOVE IT FROM TOTAL SUM
      # REMAINING SUM IS THE ANSWER
# TIME COMPLEXITY:
      # O(N)
# SPACE COMPLEXITY:
      # O(1)

#BRUTE FORCE APPROACH
def max_card(cards,k):
    n=len(cards)
    # BASE CASE
    # IF K EQUALS TOTAL CARDS
    # WE MUST TAKE ALL CARDS
    if k==n:
        return sum(cards)
    # STORES THE MAXIMUM SCORE FOUND SO FAR
    ans=0
    # TRY ALL POSSIBLE LEFT PICKS
    # left = 0,1,2,...,k
    for left in range(k+1):
        # REMAINING CARDS MUST COME FROM RIGHT
        # left + right = k
        right=k-left
        # SUM OF LEFT PICKED CARDS
        # + SUM OF RIGHT PICKED CARDS
        curr=sum(cards[:left])+sum(cards[n-right:])
        # UPDATE MAXIMUM SCORE
        ans=max(ans,curr)
    #RETURN FINAL ANSWER
    return ans
cards=[1,2,3,4,5,6,1]
k=3
print(max_card(cards,k))

#USING PREFIX SUM METHOD
def max_card(cards,k):
    n=len(cards)
    #BASE CASE 
    if k==n:
        return sum(cards)
    left=[0]*(k+1)
    right=[0]*(k+1)
    for i in range(1,k+1):
        left[i]=left[i-1]+cards[i-1]
    for i in range(1,k+1):
        right[i]=right[i-1]+cards[n-i]
    ans=0
    for take_left in range(k+1):
        take_right=k-take_left
        ans=max(ans,left[take_left]+right[take_right])
    return ans
cards=[1,2,3,4,5,6,1]
k=3
print(max_card(cards,k))

#OPTIMIZING SLIDING WINDOW
def max_card(cards,k):
    n=len(cards)
    #BASE CARDS
    if k==n:
        return sum(cards)
    total=sum(cards)
    window_size=n-k
    window_sum=sum(cards[:window_size])
    min_sum=window_sum
    for i in range(window_size,n):
        window_sum+=cards[i]
        window_sum-=cards[i-window_size]
        min_sum=min(min_sum,window_sum)
    return total-min_sum
cards=[1,2,3,4,5,6,1]
k=3
print(max_card(cards,k))