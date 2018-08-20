module.exports = { 
 //param A : array of integers
 //return an integer
    maxSpecialProduct : function(A){
       if (A.length === 0) return A;
      var SP = [0];
      var lstack = [0];
      for (var i = 1; i < A.length; i++) {
        var lsp = 0;
        while (lstack.length > 0) {
          if (A[lstack[lstack.length - 1]] > A[i]) {
            lsp = lstack[lstack.length - 1];
            break;
          }
          else lstack.pop();
        }
        lstack.push(i);
        SP.push(lsp);
      }
      SP[SP.length - 1] = 0;
      var rstack = [A.length - 1];
      var smax = 0;
      for (i = A.length - 2; i >= 0; i--) {
        var rsp = 0;
        while (rstack.length > 0) {
          if (A[rstack[rstack.length - 1]] > A[i]) {
            rsp = rstack[rstack.length - 1];
            break;
          }
          else rstack.pop();
        }
        rstack.push(i);
        var spval = SP[i] * rsp;
        if (smax < spval) smax = spval;
      }
      return smax % 1000000007;
    }
};
