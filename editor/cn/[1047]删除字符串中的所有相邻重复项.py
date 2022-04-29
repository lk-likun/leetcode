# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for i in s:
            if res and i == res[-1]:
                res.pop()
            else:
                res.append(i)
        return ''.join(res)
# leetcode submit region end(Prohibit modification and deletion)

