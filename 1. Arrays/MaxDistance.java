public class Solution {
    // DO NOT MODIFY THE ARGUMENTS WITH "final" PREFIX. IT IS READ ONLY
    public int maximumGap(final int[] A) {
        int n = A.length;
        int Lmin []= new int[n];
        int Rmax [] = new int[n];
        int maxD = -1;
        
        if(n==2 && A[1]>A[0]){
            return 1;
        }
        else if(n==2 && A[1]<A[0])
            return -1;
            
        else if(n==1){
            return 0;
        }
    //A = [3,5,4,2]
        Lmin[0] = A[0];
        Rmax[n-1] = A[n-1];
        //fill Lmin
        
        for(int i=1;i<n;i++){
            if(Lmin[i-1] < A[i]){
                Lmin[i] = Lmin[i-1];
            }
            else
                Lmin[i] = A[i];
        }
        
        for(int i=n-1;i>0;i--){
            if(Rmax[i] > A[i-1]){
                Rmax[i-1] = Rmax[i];
            }
            else
            Rmax[i-1]= A[i-1];
        }
        
        for (int first = 0,second=0 ; (first<n && second<n) ; ){
            if(Lmin[first]<Rmax[second]){
                maxD = Math.max(maxD, Math.abs(second-first));
                second++;
                
            }
            else{
                first++;
            }
        }
        return maxD;
    }
}
