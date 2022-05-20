# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = [i for i in t]
        for i in s:
            res.remove(i)
        return res[0]


# leetcode submit region end(Prohibit modification and deletion)

s1 = "abcd"
t1 = "abcde"
Solution().findTheDifference(s1, t1)
