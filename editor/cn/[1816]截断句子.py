# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res = s.split(" ")
        return " ".join(res[:k])

# leetcode submit region end(Prohibit modification and deletion)
