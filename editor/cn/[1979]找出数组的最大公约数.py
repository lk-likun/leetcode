# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        num1, num2 = min(nums), max(nums)
        while num1:
            num1, num2 = num2 % num1, num1
        return num2

# leetcode submit region end(Prohibit modification and deletion)
