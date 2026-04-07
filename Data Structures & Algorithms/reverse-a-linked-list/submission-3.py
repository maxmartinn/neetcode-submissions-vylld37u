# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        null 0 < 1 < 2 < 3
             c
         p
        """
        
        p = None
        c = head

        while c:
            tmp = c.next
            c.next = p
            p = c
            c = tmp
        return p
            

