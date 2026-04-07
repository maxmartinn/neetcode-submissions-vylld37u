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
        # make a copy hashmap
        # iterate through current node 
        # set the old node to the copy node using the hashmap

        curr = head
        while curr:
            node = Node(curr.val)
            oldToCopy[curr] = node
            curr = curr.next
        
        curr = head
        while curr:
            tmp = curr.next
            node = oldToCopy[curr]
            node.next = oldToCopy[curr.next]
            node.random = oldToCopy[curr.random]
            curr = tmp
        
        return oldToCopy[head]


            