class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        o = []
        flag = 1
        n = len(A)
        for i in range(n):
            if(A[i].isalnum()):
                o.append(A[i].upper())
        for i in range(int(n/2)):
            if(o[i] != o[n-i-1]):
                flag = 0
                return 0;
        return 1
        
