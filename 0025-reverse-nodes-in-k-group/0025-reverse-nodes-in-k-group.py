# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Check if there are k nodes to reverse
        curr = head
        for i in range(k):
            if not curr:
                return head
            curr = curr.next
        
        # Reverse first k nodes
        prev = None
        curr = head
        for i in range(k):
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # Recursively reverse remaining groups
        head.next = self.reverseKGroup(curr, k)
        
        return prev