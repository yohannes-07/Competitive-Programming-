# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = node = ListNode()
        def helper():
            
            nonlocal list1,list2, node
            if not list1 or not list2:
                return 
            
            if list1.val <= list2.val:
                node.next = list1
                node = node.next
                list1 = list1.next
                helper()
                
            else:
                node.next = list2
                node = node.next
                list2 = list2.next
                helper()
            
            return node
        
        val = helper()
        
        if list1 and val:
            val.next = list1
            
        if list2 and val: 
            val.next = list2
        
        if not val:
            if list1: return list1
            if list2: return list2
        
        return head.next
  
