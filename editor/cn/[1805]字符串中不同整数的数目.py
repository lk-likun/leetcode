# leetcode submit region begin(Prohibit modification and deletion)
from itertools import groupby


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ls = [''.join(list(g)) for k, g in groupby(word, key=lambda x: x.isdigit())]
        res = list()
        for i in ls:
            if i.isdigit():
                res.append(int(i))
        return len(set(res))


# leetcode submit region end(Prohibit modification and deletion)

word1 = "a123bc34d8ef34"
Solution().numDifferentIntegers(word1)
