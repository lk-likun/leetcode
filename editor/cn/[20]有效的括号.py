# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        dic = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        ls = list()
        for i in s:
            if i in dic:
                if not ls or ls[-1] != dic[i]:
                    return False
                ls.pop()
            else:
                ls.append(i)
        return not ls

# leetcode submit region end(Prohibit modification and deletion)
