# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str):
        ls = sentence.split(" ")
        for i, word in enumerate(ls):
            if word.startswith(searchWord):
                return i + 1
        return -1

# leetcode submit region end(Prohibit modification and deletion)
