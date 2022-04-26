# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def backspaceCompare(self, s: str, t: str):
        return self.op(s) == self.op(t)

    def op(self, t):
        ls_t = list()
        for i in t:
            if i == "#":
                if ls_t:
                    ls_t.pop()
                continue
            ls_t.append(i)
        return ls_t



# leetcode submit region end(Prohibit modification and deletion)
# #
# a = "y#fo##f"
# b = "y#f#o##f"
# # a = "ab##"
# # b = "c#d#"
# Solution().backspaceCompare(a, b)

