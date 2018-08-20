class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        n = len(A)
        n2 = len(A[0])
        for i in range(n):
            for j in range(n2):
                if(A[i][j]==0):
                    for col in range(n2):
                        if(A[i][col] == 0):
                            continue
                        else:
                            A[i][col] = -1
                    for row in range(n):
                        if(A[row][j] == 0):
                            continue
                        else:
                            A[row][j] = -1
        for i in range(n):
            for j in range(n2):
                if(A[i][j] != 1):
                    A[i][j] = 0
        return A