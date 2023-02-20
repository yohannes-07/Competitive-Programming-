# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        pre_start = dummy = ListNode(0)
        dummy.next = head
        
        # find pre start node
        for _ in range(left - 1):
            pre_start = pre_start.next

        # reverse    
        start = prev = pre_start.next
        for i in range(right - left + 1):
            temp  = start
            start = start.next
            temp.next = prev
            prev = temp
         

        # connect the reversed
       
        pre_start.next.next = start
        pre_start.next = prev
    
        return dummy.next