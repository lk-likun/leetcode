# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split(" ")
        ls = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        res = list()
        for i, v in enumerate(sentence):
            if v[0] in ls:
                v = v + "ma" + "a" * (i + 1)
            else:
                v = v[1:] + v[0] + "ma" + "a" * (i + 1)
            res.append(v)
        return ' '.join(res)

# leetcode submit region end(Prohibit modification and deletion)
