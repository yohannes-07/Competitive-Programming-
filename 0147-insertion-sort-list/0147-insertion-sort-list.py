# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_head = ListNode(0, head)
        sorted_tail = head
        
        curr = head.next
        while curr:
            
            if curr.val > sorted_tail.val:
                sorted_tail = curr
                curr = curr.next
                
            else:
                
                sorted_tail.next = curr.next
                insertPos = sorted_head
                
                while insertPos.next.val < curr.val:
                    insertPos = insertPos.next
                    
                curr.next = insertPos.next
                insertPos.next = curr
                
                curr = sorted_tail.next
                
        return sorted_head.next

        