# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            i = word.index(ch)
            return word[i::-1] + word[i + 1:]
        return word


# leetcode submit region end(Prohibit modification and deletion)

a = "abcdefd"
b = "x"
x = Solution().reversePrefix(a, b)
print(x)
