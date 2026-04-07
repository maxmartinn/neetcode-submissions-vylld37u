# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get middle of the list
        # reverse the list from the slow pointer

        # merge the two lists using tmp variables to preserve nodes when switching

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        prev = slow.next = None
        # 1 <- 2 -> 3 -> 4
        #      p.   c.tmp
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # 2 -> 4  8 -> 6
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        

        