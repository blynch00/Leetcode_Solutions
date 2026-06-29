from typing import *
from collections import *
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        associations = {None:None}

        node = head 

        while(node):

            new_node = Node(node.val, None, None)
            associations[node] = new_node
            node = node.next

        
        # Now we loop through, changing .next and .val of each node

        node = associations[head]
        old_node = head
        while(node):
            node.next = associations[old_node.next]
            node.random = associations[old_node.random]
            node = node.next
            old_node = old_node.next
        
        return associations[head]