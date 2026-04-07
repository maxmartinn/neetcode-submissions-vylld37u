# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            # 0 <- 1 -> 2 -> 3
            #     p   c tmp
            # we want prev to point at the curr
            # we want prev.next to point at curr.next
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev