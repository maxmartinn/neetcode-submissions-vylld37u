# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        
        if len(lists) == 0:
            return None
        while len(lists) >= 2:
            l1 = lists.pop()
            l2 = lists.pop()

            curr = ListNode()
            dummy = curr
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 else l2
            lists.append(dummy.next)

        return lists[0]
