class ListNode:
  def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current_node = head
        previous_node = None
        
        while current_node:
            new_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = new_node
        return previous_node
""""
Runtime: 36 ms, faster than 71.74% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.6 MB, less than 76.18% of Python3 online submissions for Reverse Linked List.
""""
