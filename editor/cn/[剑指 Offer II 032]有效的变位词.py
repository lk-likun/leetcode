# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return False
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)
        return count_s == count_t

# leetcode submit region end(Prohibit modification and deletion)
