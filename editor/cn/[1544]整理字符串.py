# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def makeGood(self, s: str) -> str:
        res = list()
        for i in s:
            if res and res[-1].lower() == i.lower() and res[-1] != i:
                res.pop()
            else:
                res.append(i)
        return "".join(res)

# leetcode submit region end(Prohibit modification and deletion)
