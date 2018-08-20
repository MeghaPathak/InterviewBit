class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        output = []
        if (A == 0):
            output.append([1])
            return output
        if (A == 1):
            output.append([1])
            output.append([1, 1])
            return output
        elif(A > 1):
            for j in range(A):
                s = []
                for i in range(j+1):
                    if (i == 0 or i == j):
                        s.insert(i,1)
                    else :
                        s.insert(i,output[j-1][i] + output[j-1][i - 1])
                output.insert(j,s);
        return output
            
            
