# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        length = 1
        tail = head
        
        while tail.next:
            tail = tail.next
            length += 1
        
        k %= length
        
        if k == 0:
            return head
        
        
        steps_to_new_head = length - k
        tail.next = head
        
        while steps_to_new_head > 0:
            tail = tail.next
            steps_to_new_head -= 1
        
        new_head = tail.next
        tail.next = None
        
        return new_head