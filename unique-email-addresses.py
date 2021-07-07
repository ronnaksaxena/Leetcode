class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = set()
        for mail in emails:
            parts = mail.split('@')
            local, domain = parts[0], parts[1]
            if local.find('+') >= 0:
                local = local[:local.find('+')]
            local = local.replace('.','')
            uniques.add(local + '@' + domain)
        return len(uniques)
