# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        result = ""
        
        pointer = head
        
        while pointer != None:
            result += str(pointer.val)
            pointer = pointer.next
            
        return int(result, 2)
            