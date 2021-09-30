class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        
        while head != slow:
            slow = slow.next
            head = head.next
        return head
           
"""
Runtime: 56 ms, faster than 39.27% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.3 MB, less than 53.83% of Python3 online submissions for Linked List Cycle II.
"""
    
        
