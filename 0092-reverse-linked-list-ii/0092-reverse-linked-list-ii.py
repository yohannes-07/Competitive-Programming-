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
            next_node = start.next
            start.next = prev
            prev = start
            start = next_node

        # connect the reversed
        pre_start.next.next = next_node
        pre_start.next = prev

        return dummy.next