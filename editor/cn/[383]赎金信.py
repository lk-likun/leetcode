# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        return not collections.Counter(ransomNote)-collections.Counter(magazine)


# leetcode submit region end(Prohibit modification and deletion)

a = "fihjjjjei"
b = "hjibagacbhadfaefdjaeaebgi"
Solution().canConstruct(a, b)
