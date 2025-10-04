class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()

        n = len(word)
        if n < 3:
            return False

        lf = Counter(word)
        has_vowel = False
        has_consonant = False
        vowels = ['a', 'e', 'i', 'o', 'u']
        for c in lf.keys():
            if c in vowels:
                has_vowel = True
            else:
                u = c.upper()
                if u.isalpha():
                    has_consonant = True
                else:
                    if not u.isnumeric():
                        return False

            
        if not has_vowel or not has_consonant:
            return False

        return True

        
