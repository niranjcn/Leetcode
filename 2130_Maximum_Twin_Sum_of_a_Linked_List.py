class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        fast = head
        slow = head
        res = 0
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        curr = slow.next
        slow.next = None
        prev = None
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        fast = prev
        slow = head
        
        while fast:
            res = max(res,slow.val + fast.val)
            slow = slow.next
            fast = fast.next
        return res