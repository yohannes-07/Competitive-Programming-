# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        # replace the node value to be deleted on the next node
        # interchange their values 
        # then delete the next 
        node.val, node.next = node.next.val, node.next.next
        
       
        
    
        