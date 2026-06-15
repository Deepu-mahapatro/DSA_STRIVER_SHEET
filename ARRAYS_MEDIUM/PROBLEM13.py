#PRINT THE MATRIX IN SPIRAL MANNER
#SPIRAL MATRIX TRAVERSAL
#PROBLEM:
#PRINT MATRIX ELEMENTS IN SPIRAL ORDER
#CORE IDEA:
#USE FOUR BOUNDARIES
#TOP,BOTTOM,LEFT,RIGHT
#TRAVERSE LAYER BY LAYER
#AND SHRINK BOUNDARIES
#TRAVERSAL ORDER:
#TOP ROW
#RIGHT COLUMN
#BOTTOM ROW
#LEFT COLUMN
#BOUNDARY UPDATES:
#TOP+=1
#RIGHT-=1
#BOTTOM-=1
#LEFT+=1
#WHY?
#VISITED SIDES SHOULD NOT
#BE VISITED AGAIN
#WHILE CONDITION:
#TOP<=BOTTOM
#AND
#LEFT<=RIGHT
#TOP:
#FIRST UNVISITED ROW
#BOTTOM:
#LAST UNVISITED ROW
#LEFT:
#FIRST UNVISITED COLUMN
#RIGHT:
#LAST UNVISITED COLUMN
#PROCESS:
#INITIALIZE BOUNDARIES
#TRAVERSE TOP
#UPDATE TOP
#TRAVERSE RIGHT
#UPDATE RIGHT
#TRAVERSE BOTTOM
#UPDATE BOTTOM
#TRAVERSE LEFT
#UPDATE LEFT
#REPEAT UNTIL
#BOUNDARIES CROSS
#TIME COMPLEXITY:
#O(m*n)
#SPACE COMPLEXITY:
#O(1)
#MEMORY TRICK:
#TOP→DOWN
#RIGHT→LEFT
#BOTTOM→UP
#LEFT→RIGHT

def spiral_manner(matrix):
    #EDGE CASE
    if not matrix:
        return []
    result=[]
    top=0
    bottom=len(matrix)-1
    left=0
    right=len(matrix[0])-1
    while top<=bottom and left<=right:
        #TRAVERSE TOP ROW
        for col in range(left,right+1):
            result.append(matrix[top][col])
        top+=1
        #TRAVERSE RIGHT COLUMN 
        for row in range(top,bottom+1):
            result.append(matrix[row][right])
        right-=1
        #TRAVERSE BOTTOM ROW 
        if top<=bottom:
            for col in range(right,left-1,-1):
                result.append(matrix[bottom][col])
            bottom-=1
        #TRAVERSE FROM LEFT
        if left<=right:
            for row in range(bottom,top-1,-1):
                result.append(matrix[row][left])
            left+=1
    return result
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(spiral_manner(matrix))               