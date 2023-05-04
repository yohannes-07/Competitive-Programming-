# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, arrays: List[Optional[ListNode]]) -> Optional[ListNode]:
         
        heap = [] # Create a min heap to store elements from k arrays
        
        for i in range(len(arrays)):
            dummy = ListNode()
            dummy.next = arrays[i]
            
            if arrays[i]: # Check if the array is not empty
                
               # Push (element, array index, element index) tuple to heap
                heapq.heappush(heap, (arrays[i].val, i, dummy.next))
                
                
        #Merge elements from k arrays using the heap
        merged  = ListNode()
        temp = merged
        
        while heap:
            num, arr_idx, node = heapq.heappop(heap) # Pop smallest element from heap
            merged.next = ListNode(num) # Add popped element to merged array
            merged = merged.next
            
             # Check if there are more elements in the same array
            if node.next:
                
                # Push next element to heap
                curr = node.next.val
                node = node.next
                heapq.heappush(heap, (curr, arr_idx, node )) 
                
        return temp.next