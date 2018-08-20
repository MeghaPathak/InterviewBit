
class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        o =[]
        if(A == 0):
          return
        for i in range(1,A+1):
            if(i%5 == 0 and i%3 == 0):
                o.insert(i-1,"FizzBuzz")
            elif(i%5 == 0):
                o.insert(i-1,"Buzz")
            elif(i%3 == 0):
                o.insert(i-1,"Fizz")
            else:
                o.insert(i-1,i)
        return o
