# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'a': 4,
            'b': 9,
            'c': 40,
            'd': 90,
            'e': 400,
            'f': 900
        }
        s = s.replace("IV", "a")
        s = s.replace("IX", "b")
        s = s.replace("XL", "c")
        s = s.replace("XC", "d")
        s = s.replace("CD", "e")
        s = s.replace("CM", "f")
        res = 0
        for i in s:
            res += dic[i]
        return res


# leetcode submit region end(Prohibit modification and deletion)

