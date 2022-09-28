# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # use two pointers prev and curr
        node =  ListNode()
        node.next = head
        curr = prev = node
        # make the pointers difference n steps
        for i in range(0, n):
            curr = curr.next
        # now when curr reaches the last node, prev will reach
        # len(all nodes) - n node 
        while curr.next:
            prev = prev.next
            curr = curr.next
        # delete  prev.next   
        prev.next = prev.next.next
        return node.next
            
        
     
     
   
     
        