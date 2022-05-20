# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = {"b": 0, "o": 0, "a": 0, "l": 0, "n": 0}
        for i in text:
            if i in dic:
                dic[i] += 1
        res = min(dic["b"], dic["o"] // 2, dic["a"], dic["n"], dic["l"] // 2)
        return res


# leetcode submit region end(Prohibit modification and deletion)

t = "nlaebolko"
Solution().maxNumberOfBalloons(t)
