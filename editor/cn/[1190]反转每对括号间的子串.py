# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseParentheses(self, s: str):
        stack = list()
        word = ""
        for i in s:
            if i == "(":
                stack.append(word)
                word = ""
            elif i == ")":
                word = stack.pop(-1) + word[::-1]
            else:
                word += i
        return word

# leetcode submit region end(Prohibit modification and deletion)
#
# st = "(ed(et(oc))el)"
# Solution().reverseParentheses(st)
