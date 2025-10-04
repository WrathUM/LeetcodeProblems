class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ucase = set()
        lcase = set()
        not_special = set()
        for c in word:
            if c.isupper():
                ucase.add(c)
            else:
                if c.upper() in ucase:
                    not_special.add(c)
                lcase.add(c)

        res = []
        for c in ucase:
            if c.lower() in lcase and c.lower() not in not_special:
                res.append(c)

        return len(res)
