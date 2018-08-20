class Solution:
    # @param A : list of integers
    # @return an integer
    import sys
    def findMinXor(self, A):
        mini = int(sys.float_info.max)
        n = len(A)
        for i in range(0,n-1):
            res = A[i] ^ A[i+1]
            mini = min(mini,res)
        return mini