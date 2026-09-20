# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        currNode = sentinel
        while list1 is not None and list2 is not None:
            print(list1)
            if list1.val <= list2.val:
                currNode.next = ListNode(list1.val)
                list1 = list1.next
                currNode = currNode.next
            else:
                currNode.next = ListNode(list2.val)
                list2 = list2.next
                currNode = currNode.next

        if list1 is not None:
            currNode.next = list1
        elif list2 is not None:
            currNode.next = list2
        return sentinel.next
        
        