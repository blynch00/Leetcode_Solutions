# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        new_list = []

        while list1 is not None or list2 is not None:
            if list1 is None and list2 is not None:
                new_list.append(list2.val)
                list2 = list2.next
                continue
            elif list1 is not None and list2 is None:
                new_list.append(list1.val)
                list1 = list1.next
                continue
            else:
                if list1.val < list2.val:
                    new_list.append(list1.val)
                    list1 = list1.next
                    continue
                elif list1.val > list2.val:
                    new_list.append(list2.val)
                    list2 = list2.next
                    continue
                else:
                    new_list.append(list1.val)
                    list1 = list1.next
                    new_list.append(list2.val)
                    list2 = list2.next
                    continue
        return new_list
    

sol = Solution()
node_next = ListNode(2)
list1 = ListNode(11, node_next)
list2 = ListNode(22)
print(sol.mergeTwoLists(list1,list2))