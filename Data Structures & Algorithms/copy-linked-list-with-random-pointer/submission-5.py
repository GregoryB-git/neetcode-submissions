
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old = {None:None}
        
        
        cur = head
        while cur:
            copy = Node(cur.val)
            old[cur] = copy
            cur = cur.next
        
        cur = head

        while cur:
            copy = old[cur]
            copy.next = old[cur.next]
            copy.random = old[cur.random]
            cur = cur.next
        
        return old[head]




        