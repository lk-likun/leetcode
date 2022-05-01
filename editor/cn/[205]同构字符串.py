# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(s) == len(t) and len(set(s)) == len(set(t)) == len(set(zip(s, t)))


# leetcode submit region end(Prohibit modification and deletion)

s1 = "egg"
t1 = "add"
x = Solution().isIsomorphic(s1, t1)
print(x)