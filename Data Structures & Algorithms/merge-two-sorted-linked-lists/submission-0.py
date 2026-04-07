# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # check if either list is null
        dummy = ListNode()
        tmp = dummy
     

        # create a dummy node 
        # while both lists are not null
        while list1 and list2:

        # check if the current value of either list is greater than one another
            if list1.val < list2.val:
                tmp.next = list1
                list1 = list1.next
        # append the greater value
            else:
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next

        # listX = listX.next

        # append the non null list to the dummy node
        if list1:
                tmp.next = list1
        if list2:
                tmp.next = list2
        # return dummy.next
        return dummy.next
        
