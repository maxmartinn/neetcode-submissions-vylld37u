# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # list is empty
        # list has one node
        # list has two or more nodes

        def merge(l1, l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next 
            
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            return dummy.next

        while len(lists) >= 2:
            # while the list is greater than one element
            new_list = []
            i = 0
            # have a while loop that iterates through the whole list merge two lists at a time
            while i < len(lists):
                head = merge(lists[i], lists[i+1] if (i + 1) < len(lists) else None)
                new_list.append(head)
                i += 2
            lists = new_list
           
        if lists:
            return lists[0]
        else:
            return None