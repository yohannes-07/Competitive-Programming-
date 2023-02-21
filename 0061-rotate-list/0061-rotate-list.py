# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return  head
        
        dummy = pre_start = curr = ListNode(0, head)
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
          
        k %= length
        if k == 0:
            return head
        
        for i in range(k):
            curr = curr.next
            
        while curr and curr.next:
            pre_start = pre_start.next
            curr = curr.next
        
        reversedNodes = pre_start.next 
        pre_start.next = None
        
        curr.next = dummy.next
        return reversedNodes