# leetcode submit region begin(Prohibit modification and deletion)
import string
from typing import List


class Solution:
    @staticmethod
    def uniqueMorseRepresentations(words: List[str]) -> int:
        dic = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
               'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
               'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
               'y': '-.--', 'z': '--..'}
        ls = list()
        for word in words:
            res = str()
            for i in word:
                res += dic[i]
            if res not in ls:
                ls.append(res)
        return len(ls)

# leetcode submit region end(Prohibit modification and deletion)

# x = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
#      "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
# y = string.ascii_lowercase
# z = dict(zip(list(y), x))
# print(z)
