# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow =   head
        
        #traverse till the right middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse the list from the right middle node to the last node
        prev = slow
        while slow:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp
        
        # recorde max value of twin sums by traversing from the 
        # beginning and end(first node for reversed part) of the original list
        max_ = 0
        while head and prev and head != prev:
            max_ = max(max_, head.val + prev.val)
            
            head = head.next
            prev = prev.next
            
        return max_
        
        
      