module.exports = { 
 //param A : array of integers
 //return a strings
    largestNumber : function(A){
    A.sort(function(x,y){
        xy = String(x) + String(y);
        yx = String(y) + String(x);
        return parseInt(yx) > parseInt(xy);
        });
        
        // c = A.map(function(i){
        //     return String(i);
        // })

    A.toString();
    p=A.join("");
    if(parseInt(p)==0){
        return "0"    
    }
    else
        return p
    }
        
    
};

