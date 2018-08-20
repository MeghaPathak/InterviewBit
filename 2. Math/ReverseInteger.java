public class Solution {
    public int reverse(int A) {
         // Handling negative numbers
        boolean negativeFlag = false;
        if (A < 0)
        {
            negativeFlag = true;
            A = -A ;
        }
      
        int prev_rev_num = 0, rev_num = 0;
        while (A != 0)
        {
            int curr_digit = A%10;
      
            rev_num = (rev_num*10) + curr_digit;
      
            // checking if the reverse overflowed or not.
            // The values of (rev_num - curr_digit)/10 and
            // prev_rev_num must be same if there was no
            // problem.
            if ((rev_num - curr_digit)/10 != prev_rev_num)
            {
             
                return 0;
            }
      
            prev_rev_num = rev_num;
            A = A/10;
        }
      
        return (negativeFlag == true)? -rev_num : rev_num;
    }
}
