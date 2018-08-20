module.exports = { 
    //param A : string
    //return an integer
    titleToNumber : function(A){
        A = A.toString().toUpperCase();
        var str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
        var num = 0;
        for (var i = A.length - 1; i >= 0; i--) {
            num += (str.indexOf(A[i]) + 1) * Math.pow(26, A.length - 1 - i)
        }
        return num;
    }
};

