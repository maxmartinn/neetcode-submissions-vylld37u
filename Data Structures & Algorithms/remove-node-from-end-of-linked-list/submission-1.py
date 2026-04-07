# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1, 2, 3, 4
        # 4  3  2  1
        #    i.    j
        # removed 2nd from the end
        # have a window that is n + 1 big
        # if fast.next is null that sent slow.next = j
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n and right:
            right = right.next
            n -= 1
            
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
