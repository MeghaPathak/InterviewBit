# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if(A is None):
            return None
        if(A.next == None):
            return A
        slow = fast = A
        if(fast.next.next == A):
            return A
        loop = False
        while(slow and fast.next and fast):
            slow = slow.next
            fast = fast.next.next or fast.next
            if(slow == fast):
                loop = True
                break
        
        
        if(loop):
            slow = A
            while(slow!=fast):
                slow = slow.next
                fast = fast.next
            return slow
        return None
            
        
        
