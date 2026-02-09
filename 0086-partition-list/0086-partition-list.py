# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        # Create two dummy nodes for less than and greater/equal partitions
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        
        # Pointers to build the two lists
        less = less_dummy
        greater = greater_dummy
        
        # Traverse the original list
        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        
        # Connect the two lists
        greater.next = None  # Important: terminate the greater list
        less.next = greater_dummy.next
        
        return less_dummy.next