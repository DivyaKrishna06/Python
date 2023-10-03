class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        
        # Create a dp matrix to store intermediate results
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: an empty pattern matches an empty string
        dp[0][0] = True
        
        # Handle patterns with '*'
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill in the dp matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        
        return dp[m][n]

# Test cases
solution = Solution()
print(solution.isMatch("aa", "a"))  # Output: False
print(solution.isMatch("aa", "*"))  # Output: True
print(solution.isMatch("cb", "?a"))  # Output: False
print(solution.isMatch("adceb", "*a*b"))  # Output: True