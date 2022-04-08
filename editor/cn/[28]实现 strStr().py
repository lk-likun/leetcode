# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if needle in haystack:
            haystack = haystack.replace(needle, '!')
            for i in range(len(haystack)):
                if haystack[i] == '!':
                    return i
        else:
            return -1

# leetcode submit region end(Prohibit modification and deletion)
