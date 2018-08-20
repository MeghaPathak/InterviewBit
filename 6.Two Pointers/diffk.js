module.exports = { 
 //param A : array of integers
 //param B : integer
 //return an integer
    diffPossible : function(A, B){
       var n = A.length
        
        if(n===0)
            return 0
        if(n===1)
             if(A[0] === B)
                return 1
        
            var i = 0;
            var j = 1;
            
            while( i<n || j<n ){
                if( (A[j]-A[i])===B && i!=j)
                    return 1
                else{
                    sub = A[j]-A[i]
                    if(sub <= B )
                        j++
                    else
                        i++
                }
                
            }
            return 0
    }
};