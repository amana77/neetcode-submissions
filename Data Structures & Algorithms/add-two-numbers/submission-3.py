# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        ans=ListNode(0)
        a=ans
        while l1 or l2:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            sum=v1+v2+carry
            carry=sum//10
            digit=sum%10
            a.next=ListNode(digit)
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            a=a.next
        if carry!=0:
            a.next=ListNode(carry)
        return ans.next