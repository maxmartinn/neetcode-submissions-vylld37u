class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        curr, prev = slow.next, None
        slow.next = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge
        l1, l2 = head, prev
        while l2:
            l1.next, l2.next, l1, l2 = l2, l1.next, l1.next, l2.next