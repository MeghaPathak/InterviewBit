class Solution:
    # @param x : integer -> base
    # @param n : integer -> exponent
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x == 0:
            return 1 % d
        ans = 1
        base = x
        base = base % d
        print("START : Ans,base : " , ans,base)

        while n > 0:
            # We need (base ** n) % p. 
            # Now there are 2 cases. 
            # 1) n is even. Then we can make base = base^2 and n = n / 2.
            # 2) n is odd. So we need base * base^(n-1) 
            if n % 2 == 1:
                ans = (ans * base) % d
                print("ODD : Ans,n : " , ans,n)
                n -= 1
            else:
                n = n >> 1 #n/2
                base = (base * base) % d
                print("EVEN : base,n : " , base,n)
        # if ans < 0:
        #     ans = (ans + d) % d
        return ans
