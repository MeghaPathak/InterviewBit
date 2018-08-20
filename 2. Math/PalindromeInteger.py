class Solution:
	# @param A : integer
	# @return an integer
	def isPalindrome(self, A):
            if A < 0:
                return 0
            elif str(A) == str(A)[::-1] :
                return 1
            else:
                return 0