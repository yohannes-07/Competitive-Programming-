# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = prev_node = prev_val = ListNode(0)
        
        node = dummy
        while head:

            while head and head.val == prev_val:
                head = head.next
                node = prev_node

            node.next = head

            prev_node, node = node, node.next
            if head:
                prev_val = head.val
                head = head.next

        return dummy.next
       
        
 
        