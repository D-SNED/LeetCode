# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
#         _set = set()
#         curr = head
        
#         while curr:
#             if curr in _set:
#                 return True
#             else:
#                 _set.add(curr)
#                 curr = curr.next
#         return False
        
        
        s = head
        f = head
        
        while f and f.next:
            s = s.next
            f = f.next.next
            
            if s == f:
                return True
        return False
    
        
        