# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        ans=ListNode(0)
        temp1=l1
        temp2=l2
        a=ans
        while temp1 or temp2:
            if temp1 is None:
                temp1=ListNode(0)
            if temp2 is None:
                temp2=ListNode(0)
            sum=temp1.val+temp2.val+carry
            carry=sum//10
            digit=sum%10
            a.next=ListNode(digit)
            temp1=temp1.next
            temp2=temp2.next
            a=a.next
        if carry!=0:
            a.next=ListNode(carry)
        return ans.next