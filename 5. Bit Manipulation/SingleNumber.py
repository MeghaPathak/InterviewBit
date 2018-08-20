class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        n = len(A)
        if(n==0):
            return 0
         num = A[0]
         for i in range(n):
             num = num ^ A[i]
         return num
        