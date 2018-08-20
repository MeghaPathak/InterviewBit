class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        for i in range(n):
            for j in range(i,len(A[i])):
                if(j!=i):
                    temp = A[i][j]
                    A[i][j] = A[j][i]
                    A[j][i] = temp
        res = [];
        for i in A:
            i.reverse()
            res.append(i)
        return res