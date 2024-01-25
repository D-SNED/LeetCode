# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        
        if head is None:
            return None
        
        curr = head.next
        trailer = head
        
        while curr:
            if curr.val == val:
                trailer.next = curr.next
                curr = curr.next
            else:
                trailer = trailer.next
                curr = curr.next
                
        return head