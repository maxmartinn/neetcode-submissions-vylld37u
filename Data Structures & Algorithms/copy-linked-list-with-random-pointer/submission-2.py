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
        oldToCopy = {None: None}
        def copyNode(node):
            if node in oldToCopy:
                return oldToCopy[node]
            oldToCopy[node] = Node(node.val)
            oldToCopy[node].next = copyNode(node.next)
            oldToCopy[node].random = copyNode(node.random)
            return oldToCopy[node] 

        return copyNode(head)



            