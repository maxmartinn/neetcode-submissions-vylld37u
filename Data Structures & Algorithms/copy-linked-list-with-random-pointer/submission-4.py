"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None : None}

        curr = head

        while curr:
            if curr not in oldToNew:
                oldToNew[curr] = Node(curr.val)
            if curr.next not in oldToNew:
                oldToNew[curr.next] = Node(curr.next.val)
            if curr.random not in oldToNew:
                oldToNew[curr.random] = Node(curr.random.val)
            oldToNew[curr].next = oldToNew[curr.next]
            oldToNew[curr].random = oldToNew[curr.random]
            curr = curr.next
        return oldToNew[head]