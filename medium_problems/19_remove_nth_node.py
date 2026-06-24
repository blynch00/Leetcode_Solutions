# Definition for singly-linked list.
from collections import *
from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node = head
        count = 0
        
        while(node):
            node = node.next
            count += 1
        
        position = count - n

        if position == 0:
            h = head.next
            head.next = None
            return h
        
        index = 0
        curr, prev = head, head

        while index < position:
            prev = curr
            curr = curr.next
            index += 1
        
        prev.next = curr.next
        return head