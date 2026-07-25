# Definition for singly-linked list.
from typing import *
from collections import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        count  = 0

        node = head
        while (node):
            count += 1
            node = node.next

        def reverseSublist(head):
            prev = None
            node = head

            while(node):
                temp = node.next
                node.next = prev 
                prev = node
                node = temp
            
            return prev


        middle = head
        end = head

        while end and end.next:
            middle = middle.next
            end = end.next.next
        
        # [middle:end] is the second list, but we can just start at the second list and continue

        list_a = head
        list_b = reverseSublist(middle)
        # Create the first node, then iterate until lists end
        new_head = list_a
        curr_node = new_head

        list_a = list_a.next
        turn = 1
        while turn < count:
            if turn % 2 == 0:
                curr_node.next = list_a
                temp = list_a.next
                list_a.next = None
                list_a = temp
                turn += 1
                curr_node = curr_node.next
                continue
            else:
                curr_node.next = list_b
                temp = list_b.next
                list_b.next = None
                list_b = temp
                turn += 1
                curr_node = curr_node.next
                continue
        return new_head




        