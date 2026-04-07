# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        clairfication given a head of a list, the list needs to be mutated in a way that reorders the list so that this is true

        [0, n-1, 1, n-2, 2, n-3, ...]

        esentially the start and the list in regular order and reverse order of the back of the list is shuffled evenly

        so that [0, 1, 2, 3, 4, 5, 6] returns [0, 6, 1, 5, 2, 4, 3]
                       s1
                          s2

        naive solution

        reverse the second half of the list in oredr to begin shuffling phase

        plan:

        using slow and fast pointers the center of the list can be calculated

        starting from the ending of the slow pointer start reversing the list

        the 2 lists will look like

        l1 = [0, 1, 2]
        l2 = [6 5 4 3]

        now starting from the start of both list using a dummy pointer create the next list
        """

        # find center of list

        # reverse starting from slow

        # shuffle using a dummy pointer


        dummy = ListNode(0, head)
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next



        c = slow.next
        slow.next = None
        p = None

        while c:
            tmp = c.next
            c.next = p
            p = c
            c = tmp
        
        l1 = head
        l2 = p

        while l1 and l2:
            dummy.next = l1
            l1 = l1.next
            dummy = dummy.next

            dummy.next = l2
            l2 = l2.next
            dummy = dummy.next
        dummy.next = l1 if l1 else l2






