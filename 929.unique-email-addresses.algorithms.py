class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        mails = []
        for mail in emails:
            text, dom = mail.split('@')
            valid = text.replace('.', '').split('+')[0]
            m = valid + '@' + dom
            if not (m in mails):
                mails.append(m)
        return len(mails)
