# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortSentence(self, s: str) -> str:
        dic = dict()
        for i in s.split(" "):
            dic.update({i[-1]: i[:-1]})
        res = list(dict(sorted(dic.items(), key=lambda x: x[0])).values())
        return " ".join(res)


# leetcode submit region end(Prohibit modification and deletion)

s1 = "is2 sentence4 This1 a3"
x = Solution().sortSentence(s1)
print(x)
