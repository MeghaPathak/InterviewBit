aclass Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        o =[]
        sum = 0
        size = len(A)
        for i in range(size):
            index = abs(A[i])-1
            if A[index] > 0:
                #p = A[index]
                #p = -1 * p
                #A[index]= list(p)
                A[index] = -1 * list( A)[index]
        for i in range (size):
            sum = sum + abs(A[i])
            if(A[i] > 0):
                missing = i + 1
        actualSum = size * (size+1)/2
        repeat = abs(actualSum - sum - missing)
        return [repeat+1, missing]
        