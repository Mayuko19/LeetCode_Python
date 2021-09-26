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
