# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ls = text.split(" ")
        res = len(ls)
        for i in ls:
            for j in i:
                if j in brokenLetters:
                    res -= 1
                    break
        return res

# leetcode submit region end(Prohibit modification and deletion)
