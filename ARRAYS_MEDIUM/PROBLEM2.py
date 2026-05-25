#SORT AN ARRAY OF 0'S 1'S 2'S
#THIS PROBLEM ALSO CALLED AS DUTCH NATIONAL FLAG PROBLEM
#ALL THE 0 SHOULD COME FIRST 
#THEN ALL 1'S COMES NEXT
#THEN ALL 2'S COMES NEXT
#HANCE THE ARRAY MUST CONSISTS OF 0'S 1'S 2'S
#HENCE 0 BELONGS TO LEFT
#HENCE 1 BELONGS TO MIDDLE
#HENCE 2 BELONGS TO RIGHT
#EDGE CASES :
            #EMPTY ARRAY->[]
            #SINGLE ELEMENT->ALREADY SORTED
            #SAME ELEMENTS
#HENCE FOR INPUT:[0,2,1,1,1,0,2,2,0]
#THE OUTPUT SHOULD BE:[0,0,0,1,1,1,2,2,2]

#USING BRUTE FORCE METHOD
def sort_Element(arr):
    #EDGE CASE: EMPTY ARRAY
    if len(arr)==0:
        return []
    arr.sort()
    return arr
print(sort_Element([1,2,0,0,0,2,1,2,1]))

#USING COUNTING METHOD
def sort_Element(arr):
    #EDGE CASE: EMPTY ARRAY
    if len(arr)==0:
        return []
    #COUNT VARIABLES
    count0=0
    count1=0
    count2=0
    #COUNT FREQUENCIES
    for num in arr:
        if num==0:
            count0+=1
        elif num==1:
            count1+=1
        elif num==2:
            count2+=1
    #REBUILD THE ARRAY
    index=0
    #PLACE 0'S
    for i in range(count0):
        arr[index]=0
        index+=1
    #PLACE 1'S
    for i in range(count1):
        arr[index]=1
        index+=1
    #PLACE 2'S
    for i in range(count2):
        arr[index]=2
        index+=1
    return arr
print(sort_Element([0,2,1,2,1,2,1,0,0]))

#DUTCH NATIONAL FLAG ALGORITHM
def sort_colors(arr):
    # EDGE CASE : EMPTY ARRAY
    if len(arr) == 0:
        return []
    low = 0
    mid = 0
    high = len(arr) - 1
    # PROCESS ARRAY
    while mid <= high:
        # CASE 1 : CURRENT ELEMENT IS 0
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        # CASE 2 : CURRENT ELEMENT IS 1
        elif arr[mid] == 1:
            mid += 1
        # CASE 3 : CURRENT ELEMENT IS 2
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
print(sort_colors([2,0,2,1,1,0,0,1,2]))
