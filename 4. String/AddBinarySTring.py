class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
       c = bin(int(A,2)+ int(B,2));
       return c.lstrip('0b');