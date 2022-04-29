# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in t:
            if not s:
                return True
            if i == s[0]:
                s = s[1:]
        return not s


# leetcode submit region end(Prohibit modification and deletion)
a = "abc"
b = "ahbgdc"
x = Solution().isSubsequence(a, b)
print(x)