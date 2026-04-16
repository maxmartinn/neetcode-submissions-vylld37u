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
        nodeMap = {None : None}

        curr = head
        while curr:
            if curr not in nodeMap:
                nodeMap[curr] = Node(curr.val)
            if curr.next not in nodeMap:
                nodeMap[curr.next] = Node(curr.next.val)
            if curr.random not in nodeMap:
                nodeMap[curr.random] = Node(curr.random.val)
            nodeMap[curr].next = nodeMap[curr.next]
            nodeMap[curr].random = nodeMap[curr.random]

            curr = curr.next
        return nodeMap[head]