# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
      def partition(self, head, x):
        left = ListNode(-101)
        right = ListNode(-101) 
       
        left_tail , right_tail = left , right
        
        while head :
            if head.val < x:
                left_tail.next = head 
                left_tail = left_tail.next
                
            else:
                right_tail.next = head
                right_tail = right_tail.next
            head = head.next
            
        left_tail.next = right.next
        right_tail.next = None
        return left.next