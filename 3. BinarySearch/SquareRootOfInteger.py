class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if(A==0):
            return 0
        if(A == 1):
            return 1
        
        n = A
        start = 1
        end = n
        
        while(start<=end):
            mid = (start + end )/2
            
            if(mid*mid == n):
                return int(mid)
            
            elif( mid*mid > n):
                end = mid-1
            
            else:
                start = mid+1
                temp = mid
        return temp
    

