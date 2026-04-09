# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        """
    
         given a array of k linked list

         sort all the linked lists to be one continous linked list

         optimization

         using a heap of size k start by storing the values of all lists as (listnode.val, listnode)

         pop from top of the heap and add to curr and then add the next listnode ot the heap

         at the end return dummy.next
        """
        curr = ListNode()
        dummy = curr

        minHeap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))

        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
            
        return dummy.next

        """
        Input: lists = [[1,2,4],[1,3,5],[3,6]]

        Output: [1,1,2,3,6]

        minHeap = []

        val, i, node = (6, 0, [6]),

        dummy = [0, 1, 1, 2, 3, 6]
        curr = [6]

        """

        
        