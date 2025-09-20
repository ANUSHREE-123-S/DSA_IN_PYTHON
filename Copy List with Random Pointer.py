"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        hash={None:None}
        curr=head
        while curr:
            hash[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            copy=hash[curr]
            copy.next=hash[curr.next]
            copy.random=hash[curr.random]
            curr=curr.next
        return hash[head]