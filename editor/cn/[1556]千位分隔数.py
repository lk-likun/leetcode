# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def thousandSeparator(self, n: int):
        # return format(n, ",").replace(',', '.')

        # i = 0
        # m = str(n)[::-1]
        # ml = len(m)
        # s = str()
        # while i < ml:
        #     s += m[i: i + 3] + '.'
        #     i += 3
        # return s[-2::-1]

        return '{:,}'.format(n).replace(',', '.')

# leetcode submit region end(Prohibit modification and deletion)


x = Solution().thousandSeparator(6789)
print(x)