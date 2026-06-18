class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        d1=ListNode(0)
        d1.next=head
        prev=d1
        while True:
            temp=prev
            for _ in range(k):
                temp=temp.next
                if temp is None:
                    return d1.next
            curr=prev.next
            for _ in range(k-1):
                to_move=curr.next
                curr.next=to_move.next
                to_move.next=prev.next
                prev.next=to_move
            prev=curr
        return d1.next