# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = list()
        w_d = {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1, 'a': 2, 's': 2, 'd': 2,
               'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2, 'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3}
        for word in words:
            res.append(word)
            word = word.lower()
            for i in set(word):
                if w_d[i] != w_d[word[0]]:
                    res.pop()
                    break
        return res


# leetcode submit region end(Prohibit modification and deletion)

s = ["Hello", "Alaska", "Dad", "Peace"]
x = Solution().findWords(s)
print(x)
