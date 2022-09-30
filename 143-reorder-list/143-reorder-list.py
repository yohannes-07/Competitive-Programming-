# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        left = head
        right = head.next
        while  right and right.next:
            left = left.next
            right = right.next.next
        
        prev, current, left.next = None, left.next, None
         
        
        while current:
            
            temp, current.next = current.next, prev
            prev, current = current, temp
           
        
        start1 = head
        start2 = prev
        
        while start2:
            temp1, temp2 = start1.next, start2.next
            start1.next = start2
            start2.next = temp1 
            start1, start2  = temp1, temp2 
            