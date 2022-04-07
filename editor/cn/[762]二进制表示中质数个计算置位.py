# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    @staticmethod
    def countPrimeSetBits(left: int, right: int) -> int:
        ls = [2, 3, 5, 7, 11, 13, 17, 19]
        num = 0
        for i in range(left, right + 1):
            if sum(bin(i)) in ls:
                num += 1
        return num

# leetcode submit region end(Prohibit modification and deletion)
