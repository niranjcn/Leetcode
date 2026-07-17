def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        for _ in range(n + 1):
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow= slow.next
        slow.next = slow.next.next
        return dummy.next