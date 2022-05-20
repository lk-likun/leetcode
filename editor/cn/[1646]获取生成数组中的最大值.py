# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):
            nums[i] = nums[i // 2] + i % 2 * nums[i // 2 + 1]
        return max(nums)


# leetcode submit region end(Prohibit modification and deletion)

n1 = 7
x = Solution().getMaximumGenerated(n1)
print(x)