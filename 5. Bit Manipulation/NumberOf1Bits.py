class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        
        if (A == 0):
            return 0
     
        else:
     
            # if last bit set add 1 else
            # add 0
            return (A & 1) + self.numSetBits(A >> 1)