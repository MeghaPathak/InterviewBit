class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        str1 = ':'.join(str(e) for e in A)
        str1 = str1.split(':')
        for i in range(len(str1)):
            # print((int(str1[i])))
            # print(int(str1[(int(str1[i]))]))
            A[i] = int(str1[(int(str1[i]))])