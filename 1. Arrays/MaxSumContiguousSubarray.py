class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        curr_max = A[0]
        max_so_far = A[0]
        
        for i in range(len(A)):
            curr_max = max(curr_max + A[i],A[i]);
            max_so_far = max(max_so_far,curr_max);
        
        return max_so_far