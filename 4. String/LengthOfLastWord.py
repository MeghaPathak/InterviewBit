class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self,A):
        s = A.split(' ')
        s = s.rstrip()
        length = len(s)
        if(length == 0):
            return 0
        if(length == 1):
            return len(s[0])
        else:
            return len(s[length-1])
        
