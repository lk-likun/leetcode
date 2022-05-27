# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ''
        tmp = 0
        for i in s:
            if i == ')':
                tmp -= 1
            if tmp:
                res += i
            if i == '(':
                tmp += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
