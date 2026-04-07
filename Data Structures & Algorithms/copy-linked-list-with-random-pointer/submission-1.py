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
        def copyList(node):
            if node in oldToCopy:
                return oldToCopy[node]
            oldToCopy[node] = Node(node.val)
            oldToCopy[node].next = copyList(node.next)
            oldToCopy[node].random = copyList(node.random)
            return oldToCopy[node] 

        return copyList(head)



            