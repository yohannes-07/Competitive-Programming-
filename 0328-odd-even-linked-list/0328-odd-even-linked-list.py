# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd = head
        even = head.next
        
        odd_dummy = ListNode(0, head)  
        even_dummy = ListNode(0, even)
      
        
        while odd.next and even.next:
            
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
            
        odd.next = even_dummy.next
        return odd_dummy.next
