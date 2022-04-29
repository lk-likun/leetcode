# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minPartitions(self, n: str) -> int:
        res = 0
        for i in n:
            if int(i) > res:
                res = max(res, int(i))
        return res

# leetcode submit region end(Prohibit modification and deletion)
