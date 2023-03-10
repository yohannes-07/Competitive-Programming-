# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = node = ListNode()
        while list1 and list2:
          
            if list1.val <= list2.val:
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
  
        return dummy.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None
        
        list1 = self.sortList(head)
        list2 = self.sortList(mid)
        
        return self.mergeTwoLists(list1, list2)
        
        
