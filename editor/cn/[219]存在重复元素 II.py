# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # dic = dict()
        # for i, v in enumerate(nums):
        #     if v in dic and i - dic[v] <= k:
        #         return True
        #     dic[v] = i
        # return False
        s = set()
        for i, num in enumerate(nums):
            if i > k:
                s.remove(nums[i - k - 1])
            if num in s:
                return True
            s.add(num)
        return False
# leetcode submit region end(Prohibit modification and deletion)
