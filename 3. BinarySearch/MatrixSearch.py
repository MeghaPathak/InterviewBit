class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self,A, B):
        nRow =  len(A)
        nCol = len(A[0])
        #print("row, col",nRow, nCol)
        if(nRow == nCol and nRow == 1 and B == A[nRow-1][nCol-1]):
            return 1
        found = 0
        for i in range(nRow-1):
         #   print("i" , i)
            if(B>A[i][nCol-1] and B<=A[i+1][nCol-1]):
                found = i+1
                break
        if(self.binarySearch(A[found],B) == -1):
            return 0;
        else:
            return 1;
         
    def binarySearch(self, a,val):
        start = 0
        end = len(a)-1
        while(start<=end):
            mid = int(start + (end - start)/2)
            if(a[mid] == val):
                return mid
            if(val < a[mid] ):
                end = mid-1;

            if(val > a[mid]):
                start = mid+1
        return -1
             
                
            