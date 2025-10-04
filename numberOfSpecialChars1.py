class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper = set()
        lcase = set()
        for c in word:
            print(c, c.isupper())
            if c.isupper():
                upper.add(c)
            else:
                lcase.add(c)

        res = []
        for c in upper:
            if c.lower() in lcase:
                res.append(c)

        return len(res)
