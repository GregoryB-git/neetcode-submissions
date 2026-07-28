
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        oldToNew = {}
        cur = head

        while cur:
            copy = Node(cur.val)
            oldToNew[cur] = copy
            cur = cur.next
        
        cur = head

        while cur:

            copy = oldToNew[cur]
            
            if cur.next:
                copy.next = oldToNew[cur.next]
            else:
                None

            if cur.random:
                copy.random = oldToNew[cur.random]
            else:
                None
            cur = cur.next
        
        return oldToNew[head]




        