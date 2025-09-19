# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy=head
        length=1
        while dummy.next:
            dummy=dummy.next
            length+=1
        position=k%length
        if position==0:
            return head
        curr=head
        for _ in range(length-position-1):
            curr=curr.next
        new_head=curr.next
        curr.next=None
        dummy.next=head
        return new_head