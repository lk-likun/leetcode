# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")
# leetcode submit region end(Prohibit modification and deletion)
