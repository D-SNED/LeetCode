# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        pointer = head
        length = 0
        
        while pointer != None:
            pointer = pointer.next
            length += 1
        
        if length % 2 == 0:
            middle = math.ceil(length / 2) + 1
        else:
            middle = math.ceil(length / 2)
        
        pointer = head
        stop_point = middle
        
        while pointer != None and stop_point != 1:
            pointer = pointer.next
            stop_point -= 1
            
        return pointer
            
        
            
        
        
        
        
        
        # while middle != 0:
        #     pointer = pointer.next
        #     middle -= 1
        # return pointer.val
        
        
            
            