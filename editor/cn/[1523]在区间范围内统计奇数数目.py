# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = high - low + 1
        return (res >> 1) + (res & 1) & (low & 1)


# leetcode submit region end(Prohibit modification and deletion)

# low1 = 3
# high1 = 7
# x = Solution().countOdds(low1, high1)
# print(x)

def bn(n):
    if n == 0:
        return str()
    return bn(n // 2) + str(n % 2)


a = 10721
print(bin(a)[2:])
print(bn(a))