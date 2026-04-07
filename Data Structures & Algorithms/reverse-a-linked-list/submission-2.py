# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        #       0 -> 1 -> 2 -> 3
        #     <-p <- c

        # set the current next pointer to prev
        # set the set the prev pointer to current

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev 