# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def binaryGap(self, n: int) -> int:
        tmp = bin(n)[2:]
        left = 0
        res = 0
        for i in range(len(tmp)):
            if tmp[i] == '1':
                res = max(res, i - left)
                left = i
        return res
# leetcode submit region end(Prohibit modification and deletion)

