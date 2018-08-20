class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        res = 0;
        num = 5
        power = 1
        while(A >= (num**power)):
            res = res + (A/(num**power))
            power = power + 1
        return res
        