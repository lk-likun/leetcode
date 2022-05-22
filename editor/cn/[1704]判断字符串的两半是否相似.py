# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        target = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        n = len(s) // 2
        left = right = 0
        for i in range(n):
            if s[i] in target:
                left += 1
            if s[i + n] in target:
                right += 1
        return left == right
# leetcode submit region end(Prohibit modification and deletion)
