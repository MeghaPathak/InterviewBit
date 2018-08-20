class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        
        A = A.lstrip().rstrip()
     
        s = A.split(' ')
           
        s = s[::-1]
        for i in range(len(s)-1):
            if(s[i] == ''):
                s.remove('')
        
        return ' '.join(s)
        
