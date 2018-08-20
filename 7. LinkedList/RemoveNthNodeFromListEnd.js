// Definition for singly-linked list.
//    function Node(data){
//      this.data = data
//      this.next = null
//    }

module.exports = { 
 //param A : head node of linked list
 //param B : integer
 //return the head node in the linked list
    removeNthFromEnd : function(A, B){
        first = A;
        second = A;
        third = A;
        size = 0
        
       
        
        while(first.next!=null){
            size++;
            first = first.next;
        }
        
        if(size == 0)
            return null
        
        if(B>size){
            temp = A.next
            A.next = null
            A= temp;
            return A;
        }
        
        first = A;
        
        for (i=1;i<B;i++){
            first = first.next   
        }
        
        while(first && first.next != null){
            second = second.next;
            first = first.next;
        }
        
        while(third.next != second){
            third=third.next
        }
        
        third.next = second.next
        second.next = null
        
        
        return A
        
    }
};
