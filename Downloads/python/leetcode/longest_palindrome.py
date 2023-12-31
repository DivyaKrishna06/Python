lass Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        start, max_len = 0, 1  # Initialize the start index and maximum length

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_len:
                        start = i
                        max_len = length

        return s[start:start + max_len]