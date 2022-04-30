# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        tmp = 0
        for i in s:
            if i == 'R':
                tmp += 1
            else:
                tmp -= 1
            if tmp == 0:
                res += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

st = "RLRRLLRLRL"
Solution().balancedStringSplit(st)
