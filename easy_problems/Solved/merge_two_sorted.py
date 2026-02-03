# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Check if either are empty:
        if list1 is None and list2 is None:
            return []
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        # 1. Set head (smaller value)
        if list1.val >= list2.val:
            new_head = list1 
            current_node = list1
            list1 = list1.next
        else:
            new_head = list2 
            current_node = list2
            list2 = list2.next

        while list1 is not None or list2 is not None:
            if list1 is None:
                current_node.next = list2
                current_node = current_node.next
                list2 = list2.next
                continue
            elif list2 is None:
                current_node.next = list1
                current_node = current_node.next
                list1 = list1.next
                continue
            if list1.val <= list2.val:
                current_node.next = list1
                list1 = list1.next
                current_node = current_node.next
            else:
                current_node.next = list2
                list2 = list2.next
                current_node = current_node.next
        current_node.next = None
        return new_head

sol = Solution()
list1_node_a = ListNode(4, None)
list1_node_b = ListNode(2, list1_node_a)
list1_node_c = ListNode(1, list1_node_b)
list2_node_a = ListNode(4, None)
list2_node_b = ListNode(3, list2_node_a)
list2_node_c = ListNode(1, list2_node_b)
print(sol.mergeTwoLists(list1_node_c,list2_node_c))