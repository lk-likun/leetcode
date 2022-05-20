# leetcode submit region begin(Prohibit modification and deletion)
import string


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.convert(firstWord) + self.convert(secondWord) == self.convert(targetWord)

    def convert(self, word):
        dic = dict(zip(string.ascii_lowercase, [i for i in range(27)]))
        num = ""
        for i in word:
            num += str(dic[i])
        return int(num)


# leetcode submit region end(Prohibit modification and deletion)

f = "acb"
s = "cba"
t = "cdb"
Solution().isSumEqual(f, s, t)
