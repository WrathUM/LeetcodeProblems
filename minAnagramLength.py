class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1

        for i in range(1, n):
            if n % i != 0:
                continue
            first_window = s[0:i]
            c1 = Counter(first_window)
            for j in range(1, n//i):
                window_start = j * i
                second_window = s[window_start: window_start + i]
                c2 = Counter(second_window)
                if c1 != c2:
                    break
            if c1 == c2:
                return len(first_window)
            
        return n
            
