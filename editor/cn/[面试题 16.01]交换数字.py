# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0], numbers[1] = numbers[1], numbers[0]
        return numbers

# class Solution:
#     def swapNumbers(self, numbers: List[int]) -> List[int]:
#         if not numbers:
#             return numbers
#         numbers[0] = numbers[0] ^ numbers[1]
#         numbers[1] = numbers[0] ^ numbers[1]
#         numbers[0] = numbers[0] ^ numbers[1]
#         return numbers
# leetcode submit region end(Prohibit modification and deletion)
