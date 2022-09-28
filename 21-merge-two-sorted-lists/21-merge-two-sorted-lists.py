# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def mergeTwoLists(self, list1, list2):
        head = node = ListNode()
        while list1 and list2:
            l1 = list1.val
            l2 = list2.val
          
            if l1 <= l2:
                node.next = list1
                node = node.next
                list1 = list1.next
                
            else:
                node.next = list2
                node = node.next
                list2 = list2.next
            
        if list1:
            node.next = list1
        if list2:
            node.next = list2
  
        return head.next
        
    
        