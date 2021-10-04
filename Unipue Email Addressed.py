class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        fixed_email = set()
        for lists in emails:
            local, domain = lists.split("@")
            local = local.split("+")[0].replace(".", "")
            fixed_email.add(local + "@" + domain)
        return len(fixed_email)

""""
Runtime: 44 ms, faster than 94.36% of Python3 online submissions for Unique Email Addresses.
Memory Usage: 14.5 MB, less than 32.08% of Python3 online submissions for Unique Email Addresses.
""""
