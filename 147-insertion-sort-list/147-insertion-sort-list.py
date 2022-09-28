# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001)
        curr = head
        while curr:
            group_prev = dummy
            
            while group_prev and curr.val > group_prev.val:
                prev = group_prev
                group_prev = group_prev.next
                
            prev.next = curr
            curr = curr.next
            prev.next.next = group_prev
            
        return dummy.next