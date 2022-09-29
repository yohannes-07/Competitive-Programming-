# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper(self, node):
        if not node:
            return 
        prev = node.next
        curr = None
        if prev:
            curr = prev.next
        if curr:
            next_node = curr.next
            curr.next = prev
            node.next = curr
            prev.next = next_node
            self.helper(prev)
        
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        self.helper(dummy)
        return dummy.next
    
        