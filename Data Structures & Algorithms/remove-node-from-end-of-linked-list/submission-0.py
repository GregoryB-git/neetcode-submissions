# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        arr.pop(-n)
        if len(arr) == 0:
            return None

        curr = ListNode(arr[0])
        head = curr
        for i in arr[1:]:
          temp = ListNode(i)
          curr.next = temp
          curr = temp

        return head




