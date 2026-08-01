# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 2 pointers for the lists
        node_A = list1
        node_B = list2
        new_list = None
        list_head = None
        # 2 pointers for iterations

        while (node_A or node_B):
            if(node_A is not None and node_B is not None):
                # Compare node values:
                if node_A.val <= node_B.val:
                    # A <= B
                    if new_list is None:
                        new_list = node_A
                        list_head = node_A
                        node_A = node_A.next
                        continue
                    new_list.next = node_A
                    new_list = new_list.next
                    node_A = node_A.next
                    continue
                
                else:
                # A > B
                    if new_list is None:
                        new_list = node_B
                        list_head = node_B
                        node_B = node_B.next
                        continue
                    new_list.next = node_B
                    new_list = new_list.next
                    node_B = node_B.next
                    continue
            elif(node_A and node_B is None):
                # A & !(B)
                if new_list is None:
                    new_list = node_A
                    list_head = node_A
                    break
                else:
                    new_list.next = node_A
                    break
            else:
                # !(A) & B
                if new_list is None:
                    new_list = node_B
                    list_head = node_B
                    break
                new_list.next = node_B
                break
        return list_head
        