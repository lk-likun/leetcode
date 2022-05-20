# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count("1")
        
# leetcode submit region end(Prohibit modification and deletion)

