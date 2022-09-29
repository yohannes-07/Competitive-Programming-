# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        idx, answer, mstack = -1, [], []
        curr = head
        while curr:
            idx += 1
            answer.append(0)
            while mstack and mstack[-1][1] < curr.val:
                i, value = mstack.pop()
                answer[i] = curr.val
#                print (answer)
            
            mstack.append((idx, curr.val))
            curr = curr.next
      
    
        return answer 
        