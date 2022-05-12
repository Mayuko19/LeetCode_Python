# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hashmap = {}
        while head != None:
            if head in hashmap:
                return True
            hashmap[head] = head
            head = head.next
        return False
""""
Runtime: 56 ms, faster than 66.13% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.9 MB, less than 16.84% of Python3 online submissions for Linked List Cycle.
""""

class Solution(object):
    def hasCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
