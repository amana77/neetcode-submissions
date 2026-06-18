# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d1=d2=ListNode(0)
        while list1 and list2:
            if list1.val<=list2.val:
                d1.next=list1
                list1=list1.next
            else:
                d1.next=list2
                list2=list2.next
            d1=d1.next
        if list1:
            d1.next=list1
        if list2:
            d1.next=list2
        return d2.next
        