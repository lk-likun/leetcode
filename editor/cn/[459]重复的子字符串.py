# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)


# leetcode submit region end(Prohibit modification and deletion)

s1 = "abab"
Solution().repeatedSubstringPattern(s1)
