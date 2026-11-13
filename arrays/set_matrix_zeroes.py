#First Developed the simple straightforward solution with O(m + n) space:

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows,cols=set(),set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    rows.add(r)
                    cols.add(c)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols: matrix[i][j] = 0

#Then developed O(1) space:
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r0=False         #variable to store overlapping 1st row and col as we do not know whether - The first row or first column or both need to become zero.
 
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    matrix[0][c]=0            #indicate to set column to 0
                    if r!=0: matrix[r][0]=0   #set row to 0
                    else: r0=True
        
        for r in range(1,len(matrix)):   #To make ros and col 0 iterate 1 more time
            for c in range(1,len(matrix[0])):
                if matrix[0][c]==0 or matrix[r][0]==0:      #Make whole col 0
                    matrix[r][c]=0
        
        if matrix[0][0] == 0:    #Make 1st col 0 since we have seperate r0 for row
            for r in range(len(matrix)):
                matrix[r][0] = 0
        
        if r0:     #Make 1st row 0 
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
