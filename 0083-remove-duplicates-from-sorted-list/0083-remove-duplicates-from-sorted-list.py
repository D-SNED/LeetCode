# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        pointer = head
        
        _set = set()
        
        while pointer:
            if pointer.val not in _set:
                _set.add(pointer.val)
                prev = pointer
                pointer = pointer.next
            else:
                prev.next = pointer.next
                pointer = pointer.next
                
        return head
            
            