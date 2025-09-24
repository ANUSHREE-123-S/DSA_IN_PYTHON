# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.

class Solution:
    def splitListToParts(self, head, k):
        ans = [None] * k
        # Calculate total size of the linked list
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        # Minimum size of each part
        width = n // k
        remainder = n % k  # Remaining nodes to distribute
        curr = head
        for i in range(k):
            ans[i] = curr
            parts_size = width + (1 if remainder > 0 else 0)
            remainder -= 1
            # Traverse to the end of the current part
            for _ in range(parts_size - 1):
                if curr:
                    curr = curr.next
            # Cut the list
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
        return ans