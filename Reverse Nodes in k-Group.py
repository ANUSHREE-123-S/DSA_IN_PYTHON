# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        group_prev=dummy
        while True:
            kth=group_prev
            for _ in range(k):
                kth=kth.next
                if not kth:
                    return dummy.next
            group_next=kth.next
            prev,curr=group_next,group_prev.next
            while curr!=group_next:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            temp=group_prev.next
            group_prev.next=kth
            group_prev=temp