# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1 or (s[-1].isalpha() and s[-2] == ' '):
            return 1
        if s[-1].isalpha():
            return 1 + self.lengthOfLastWord(s[:-1])
        return self.lengthOfLastWord(s[:-1])
        # return len(s.split()[-1])
# leetcode submit region end(Prohibit modification and deletion)


# x = " fly me to the moon "
# y = Solution().lengthOfLastWord(x)
# print(y)