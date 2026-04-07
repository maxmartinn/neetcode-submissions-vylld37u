# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       # 9 7 3
       # 4 5 6
       # 3 3 0 1

        # carry = 1
        head = ListNode(0)
        dummy = ListNode(0)
        head.next = dummy
        carry = 0
        while l1 and l2:
            # add the values of l1 and l2
            value = l1.val + l2.val + carry
            carry = value // 10
            if value >= 10:
                value -= 10
            dummy.next = ListNode(value)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            value = l1.val + carry
            carry = value // 10
            if value >= 10:
                value -= 10
            dummy.next = ListNode(value)
            dummy = dummy.next
            l1 = l1.next
        while l2:
            value = l2.val + carry
            carry = value // 10
            if value >= 10:
                value -= 10
            l2 = l2.next
            dummy.next = ListNode(value)
            dummy = dummy.next
        if carry:
            dummy.next = ListNode(carry)
            dummy = dummy.next

                    
        return head.next.next

