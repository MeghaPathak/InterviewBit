class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        n = len(A)
        flag = -1
        if(A[n-1] == 0 or A[0]==0):
            return 1
        for i in range(n-1):
            if(A[i]==A[i+1]):
                continue
            if(n - (i+1) == A[i]):
                flag = 1
                break
        return flag
