class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prevGroup = dummy;
        
        while (true) {
            ListNode kth = getKth(prevGroup, k);
            if (kth == null) break;
            
            ListNode nextGroup = kth.next;
            ListNode[] reversed = reverse(prevGroup.next, kth);
            
            prevGroup.next = reversed[0];
            reversed[1].next = nextGroup;
            prevGroup = reversed[1];
        }
        
        return dummy.next;
    }
    
    private ListNode getKth(ListNode node, int k) {
        while (node != null && k > 0) {
            node = node.next;
            k--;
        }
        return node;
    }
    
    private ListNode[] reverse(ListNode head, ListNode tail) {
        ListNode prev = tail.next;
        ListNode curr = head;
        while (prev != tail) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return new ListNode[]{tail, head};
    }
}