# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node before head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head:
            # If current node is a duplicate
            if head.next and head.val == head.next.val:
                # Skip all nodes with this value
                while head.next and head.val == head.next.val:
                    head = head.next
                # Skip the last duplicate node
                prev.next = head.next
            else:
                # No duplicate, move prev forward
                prev = prev.next
            
            # Move to next node
            head = head.next
        
        return dummy.next