# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        return len(pattern) == len(s) and len(set(pattern)) == len(set(s)) == len(set(zip(pattern, s)))


# leetcode submit region end(Prohibit modification and deletion)

a = "abba"
b = "dog cat cat dog"
Solution().wordPattern(a, b)
