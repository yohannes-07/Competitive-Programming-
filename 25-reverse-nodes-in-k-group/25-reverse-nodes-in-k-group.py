# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = n_ext
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_left = dummy
        start = head
        while start:
            local_k = k
            for i in range(k-1):
                if start.next:
                    start = start.next
                    local_k -= 1
            if local_k != 1:
                return dummy.next
            
            next_node = start.next
          
            prev, curr = next_node, prev_left.next
            while curr != next_node:
                temp = curr.next
                curr.next = prev
                prev = curr 
                curr = temp
            
            temp = prev_left.next
            prev_left.next = start
            prev_left = temp
            start = curr
            
        return dummy.next
