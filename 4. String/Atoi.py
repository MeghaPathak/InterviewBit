class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        A=A.lstrip().rstrip()
        num = 0
        count = 0
        minus = False
       # plus = False
        for i in range(len(A)):
            #print i==0 and A[i] == '-'
            if(i==0 and A[i] == '-'):
                minus = True
            elif(i==0 and A[i] == '+'):
                minus = False
            elif not (A[i] <= '9' and A[i] >= '0'):
                #print("ELif not,",A[i],num)
                if(minus):
                    return (-1)*num
                else :
                    return num;
            else:
                num = (num * 10) + int(A[i]);
                if num > 2147483647 and minus == True:
                    return -2147483647
                elif num > 2147483647 and minus == False:
                    return 2147483648
                #print("ELSE",num)
        if(minus):
            return (-1)*num
        else: 
            return num;