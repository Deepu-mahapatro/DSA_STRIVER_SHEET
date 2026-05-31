#SET MATRIX ZEROES
#PURPOSE:
#IF A CELL IS 0,
#MAKE ITS ENTIRE ROW AND COLUMN 0.
#PROCESS:
#TRAVERSE THE MATRIX.
#IF A 0 IS FOUND:
#STORE ITS ROW.
#STORE ITS COLUMN.
#AFTER TRAVERSAL:
#TRAVERSE THE MATRIX AGAIN.
#IF CURRENT CELL BELONGS TO A STORED ROW:
#MAKE IT 0.
#IF CURRENT CELL BELONGS TO A STORED COLUMN:
#MAKE IT 0.
#IMPORTANT RULES:
#DO NOT MODIFY WHILE FINDING ZEROS.
#USE ONLY ORIGINAL ZEROS.
#FIRST COLLECT, THEN UPDATE.
#WHY THIS WORKS:
#PREVENTS NEWLY CREATED ZEROS
#FROM AFFECTING OTHER CELLS.
#EDGE CASES:
#EMPTY MATRIX
#SINGLE ELEMENT
#NO ZERO PRESENT
#ALL ZEROS
#ONE ROW
#ONE COLUMN
#ZERO IN FIRST ROW/COLUMN
#MAIN LOGIC:
#FIND ALL ZERO POSITIONS.
#MARK THEIR ROWS AND COLUMNS.
#MAKE ALL MARKED ROWS
#AND COLUMNS ZERO.

#USING BRUTE FORCE APPROACH
def set_zeros(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    MARK=-1
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==0:
                #MARK ROW
                for c in range(cols):
                    if matrix[i][c]!=0:
                        matrix[i][c]=MARK
                #MARK COLUMN
                for r in range(rows):
                    if matrix[r][j]!=0:
                        matrix[r][j]=MARK
    #CONVERTS MARKS TO ZERO
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==MARK:
                matrix[i][j]=0
    return matrix
matrix=[
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
print(set_zeros(matrix))
