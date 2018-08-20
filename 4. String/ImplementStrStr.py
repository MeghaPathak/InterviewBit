class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        found = False
        isStr = False
        if(len(A)==1 and len(B)=1 && A[0] == B[0]):
            return 1
        for i in range(len(A)):
            if(A[i]==B[0]):
                found = True
              #  print("ith Loop:",A[i], B[0])
            if(found):
                index = i
                isStr = True
                for j in range(len(B)):
                  #  print(" j loop : A[i], B[j]", A[i],B[j])
                    if(A[index] == B[j] and index < (len(A)-1)):
                        index = index + 1
                        isStr = True
                    else:
                        isStr = False;
                        break;
            if(isStr):
                return 1;
        return -1

               
           
           \