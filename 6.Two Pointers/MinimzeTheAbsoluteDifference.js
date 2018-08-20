module.exports = { 
 //param A : array of integers
 //param B : array of integers
 //param C : array of integers
 //return an integer
    solve : function(A, B, C){
        x = A.length
        y = B.length
        z = C.length
        o = []
        i = j = k = 0
        diff=Number.POSITIVE_INFINITY
        if(x==y==z==1){
            return max(A[0],B[0],C[0]) - min(A[0],B[0],C[0])
        }
        if(x==0 || y==0 || z==0)
            return diff;
        while(i<x && j<y && k<z){
            maxi = Math.max(A[i],B[j],C[k])
            mini = Math.min(A[i],B[j],C[k])
            absDiff = maxi - mini
            
            if(absDiff<diff){
                diff = absDiff;
                o = [A[i],B[j],C[k]]
            }
            
            if(!diff)
                break;
            if(mini == A[i])
                i++
            else if(mini == B[j])
                j++
            else
                k++
        }
        return(Math.max(o[0],o[1],o[2])-Math.min(o[0],o[1],o[2]))
    }
};
