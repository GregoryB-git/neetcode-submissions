# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for lst in lists:
            while lst.next:
                arr.append(lst.val)
                lst = lst.next
            arr.append(lst.val)
        
        arr.sort()
        
        dummy = ListNode()
        prev = dummy
        for val in arr:
            node = ListNode(val)
            prev.next = node
            prev = node

        return dummy.next 