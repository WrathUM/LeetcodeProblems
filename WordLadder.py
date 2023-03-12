def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        
        

        bfs = [(beginWord, 1)]
        visited = set()
        visited.add(beginWord)
        while bfs:
            curWord, length = bfs.pop(0)
            visited.add(curWord)
            for i in range(len(curWord)):
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = curWord[:i] + letter + curWord[i+1:]
                    if newWord in wordList:       
                        if newWord == endWord:
                            return length + 1
                        if newWord in visited:
                            continue
                        bfs.append((newWord, length + 1))
                
        return 0
