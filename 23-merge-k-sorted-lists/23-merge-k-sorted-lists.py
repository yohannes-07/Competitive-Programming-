# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = head = ListNode(0)
        temp = []
        
        for curr in lists:
            while curr:
                temp.append(curr.val)
                curr = curr.next
        
        temp.sort()
        
        for  i in range(len(temp)):
            head.next = ListNode(temp[i])
            head = head.next
        return dummy.next