# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow =  curr = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = start = slow
        while slow:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp
            
        max_ = 0
        while head and prev and head != prev:
            max_ = max(max_, head.val + prev.val)
            
            head = head.next
            prev = prev.next
            
        return max_
        
        
      