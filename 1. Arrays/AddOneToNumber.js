module.exports = { 
 //param A : array of integers
 //return a array of integers
    plusOne : function(A){

       var hasExtra = true;
        
        for(var i = A.length -1; i >= 0 ; i--) {
            if(!hasExtra)
                break;
            
            A[i] = (A[i] + 1)%10;
            hasExtra = false;
            
            if(A[i] == 0) {
                hasExtra = true;
            }
        }

        if(hasExtra) {
         A.unshift(1);
        }
        
        while(A[0] == 0) {
            A.shift();
        }
       
       return A;
    
    }
};
