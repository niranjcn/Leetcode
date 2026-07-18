class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {}
        curr = head
        
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            new = copy[curr]
            new.next = copy.get(curr.next)
            new.random = copy.get(curr.random)
            curr = curr.next
        return copy.get(head)