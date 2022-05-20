# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        maxLen = 0
        left = 0
        right = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[j] == s[i]:
                    if j - i <= 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    left = i
                    right = j
        return s[left:right + 1]


# leetcode submit region end(Prohibit modification and deletion)

s1 = "babad"
x = Solution().longestPalindrome(s1)
print(x)