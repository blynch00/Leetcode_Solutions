from typing import *
from collections import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create arr1 and arr 2

        arr_1 = deque()
        arr_2 = deque()
        # Make deques and store in reverse
        head = l1
        while head:
            arr_1.appendleft(str(head.val))
            head = head.next
        # Get second deque
        head = l2
        while head:
            arr_2.appendleft(str(head.val))
            head = head.next
        
        # Convert to strings, then to int
        num_1 = int("".join(arr_1))
        num_2 = int("".join(arr_2))
        product = str(num_1 + num_2)
        
        index = 0
        head = None
        first = None
        while index < len(product):
            node = ListNode(int(product[index]))
            if head is None:
                head = node
                first = head
            else:
                head.next = node
                head = head.next
            index += 1
        # Now reverse the list

        curr, prev = first, None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev

        