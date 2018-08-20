// Definition for singly-linked list.
//    function Node(data){
//      this.data = data
//      this.next = null
//    }

module.exports = { 
 //param A : head node of linked list
 //param B : integer
 //param C : integer
 //return the head node in the linked list
    reverseBetween : function(A, B, C){
        loop = C-B
        prev = curr = next = A
        i = 1
        if(!A)
            return null
        if (B>=C)
            return A
        while(i<B){
            prev = prev.next
            //console.log("i & prev",i,prev.data)
            i++;
        }
        
        temp = A
        size = 0;
        while(temp!=null){
            size++
            temp = temp.next;
        }
        temp_prev = prev
        curr = prev.next
        next =  prev.next.next || prev.next
    //    console.log("loop",loop)
        while(loop>0){
            curr.next = prev
            prev = curr
            curr = next
            next = next.next || next 
            loop--;
        }
        //console.log(prev.data,curr.data,next.data)
        ptr = A
        
        if(B === 1 && C === size){
           // console.log("It;s here. Ptr.data,curr.data" ,ptr.data,curr.data)
            A = curr
            ptr.next = null
            return A
        }
        
        if(B === 1 && C <= size){
         //   console.log("It;s here. Ptr.data,curr.data" ,ptr.data,curr.data)
            A.next = curr
            A = prev
            return A
        }

        while(ptr.next!==temp_prev){
            ptr = ptr.next
        }
        if(B > 1 && C === size){
            ptr.next=prev
            temp_prev.next = null
            return A
        }
        //console.log(temp_prev.data,ptr.data)
        ptr.next=prev
        temp_prev.next = curr
        
        return A
    }
};
