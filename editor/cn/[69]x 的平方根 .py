# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l = 0
        r = x
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 <= x:
                l = mid + 1
                res = mid
            else:
                r = mid -1
        return res
# leetcode submit region end(Prohibit modification and deletion)
