# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_index = arr.index(max(arr))
        left = arr[:max_index + 1]
        right = arr[max_index:]
        if len(left) >= 2 and len(right) >= 2:
            return all(left[i - 1] < left[i] for i in range(1, len(left))) and all(
                right[i - 1] > right[i] for i in range(1, len(right)))
        else:
            return False


# leetcode submit region end(Prohibit modification and deletion)

arr1 = [3, 5, 5]
x = Solution().validMountainArray(arr1)
print(x)
# if __name__ == '__main__':
#     nums = [0, 1, 2, 4, 6, 8, 9, 10]
#     x = all(nums[i - 1] < nums[i] for i in range(1, len(nums)))
#     print(x)
