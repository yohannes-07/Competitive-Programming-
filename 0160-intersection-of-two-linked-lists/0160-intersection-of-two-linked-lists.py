# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        curA,curB = headA,headB
        lenA,lenB = 0,0
        
        while curA is not None:
            lenA += 1
            curA = curA.next
            
        while curB is not None:
            lenB += 1
            curB = curB.next
            
        curA,curB = headA,headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next
                
        elif lenB > lenA:
            for i in range(lenB-lenA):
                curB = curB.next
                
        while curB != curA:
            curB = curB.next
            curA = curA.next
            
        return curA