# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        
        curr = head
        next_node = curr.next
        
        def divisor(node1, node2):
            start = min(node1.val, node2.val)
            
            while start > 0:
                if node1.val % start == 0 and node2.val % start == 0:
                    return ListNode(start)
                start -= 1
        
        while next_node:
            divisor_node = divisor(curr, next_node)
            
            curr.next = divisor_node
            divisor_node.next = next_node
            
            curr = next_node
            next_node = next_node.next
            
        return head
            
            
            
        