/**
 * @input A : Integer
 * @input B : Integer
 * 
 * @Output Integer
 */
int uniquePaths(int A, int B) {
    int m = A;
    int n = B;
    if (m == 1 || n == 1)
        return 1;
 
   // If diagonal movements are allowed then the last addition
   // is required.
   return  uniquePaths(m-1, n) + uniquePaths(m, n-1);
    
}
