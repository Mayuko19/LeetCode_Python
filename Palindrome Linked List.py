class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        value = []
        while head:
            value.append(head.val)
            head =  head.next
        return value == value[::-1]
""""
Runtime: 796 ms, faster than 73.48% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 47 MB, less than 56.71% of Python3 online submissions for Palindrome Linked List.
""""
