def getHint(self, secret: str, guess: str) -> str:
        numBulls = 0
        numCows = 0
        
        secHash = defaultdict(int)
        
        for c in secret:
            secHash[c] += 1
        
        for c in guess:
            if c in secHash and secHash[c] > 0:
                numCows += 1
                secHash[c] -= 1
        
        for idx, c in enumerate(guess):
            if secret[idx] == c:
                numBulls += 1
                numCows -= 1

        res = str(numBulls) + "A" + str(numCows) + "B"
        return res
