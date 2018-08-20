module.exports = { 
 //param A : array of integers
 //param B : array of integers
 //return a array of integers
    intersect : function(A, B){
             p = 0
    q= 0
    o =[]
    a = A.length
    b = B.length
    //console.log(a,b)
    if(a === 0 && b ===0)
     return [];
    if(a === 1 && b===1 && A[0] === B[0])
    return [A[0]]
    while(p<a && q<b){
        //console.log("p and q are:", p,q)
        //console.log("A[p] and B[q] are:", A[p],B[q])
        if(A[p]<B[q]){
            p++;
            }
        else if(B[q]<A[p]){
            q++
        }
        else if(A[p]===B[q]){
          //  console.log("Pushing to O", A[p])
            o.push(A[p])
            p++;q++;
        }
            
    }
    return o;
    }
};
