# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        seen = defaultdict(list)
        while head:
            if head.val in seen and seen[head.val] == head.next:
                return True
            seen[head.val] = head.next
            head = head.next

        return False
            