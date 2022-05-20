# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxPower(self, s: str) -> int:
        res = 1
        tmp = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                tmp += 1
                res = max(res, tmp)
            else:
                tmp = 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

s1 = "abbcccddddeeeeedcba"
x = Solution().maxPower(s1)
print(x)