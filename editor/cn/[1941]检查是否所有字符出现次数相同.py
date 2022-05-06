# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = collections.Counter(s)
        return len(set(count.values())) == 1


# leetcode submit region end(Prohibit modification and deletion)

s1 = "abacbc"
x = Solution().areOccurrencesEqual(s1)
print(x)
