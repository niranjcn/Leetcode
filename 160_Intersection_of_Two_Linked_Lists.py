class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB

        while a != b:
            if a is None:
                a = headB
            else:    
                a = a.next
            
            if b is None:
                b = headA
            else:
                b = b.next

        return a