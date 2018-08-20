module.exports = { 
 //param A : array of integers
 //param B : integer
 //return a array of integers
    maxone : function(A, B){
       
wl = wr= 0
bl = 0 
bw = -1
max = 0
o =[]
start = 0
end = 0
n = A.length
m = B
while(wr<n){
    
        if(max <= m){
            if(A[wr]===0)
                max++
            wr++
        }

        if(max > m){
            if(A[wl]===0)
                max--
            wl++
        }
        diff = wr-wl +1
        if(diff>bw){
            bw = diff
            start=wl
            end = wr
        }
            
    }
    for (var i = start;i<end;i++){
        
            o.push(i);
        
    }
return o
}
    
};
