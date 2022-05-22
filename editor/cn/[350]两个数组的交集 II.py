# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intersect(self, nums1, nums2):
        nums1, nums2 = sorted(nums1), sorted(nums2)
        l1, l2 = 0, 0
        res = []
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] == nums2[l2]:
                res.append(nums1[l1])
                l1 += 1
                l2 += 1
            elif nums1[l1] < nums2[l2]:
                l1 += 1
            else:
                l2 += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

n1 = [4, 9, 5]
n2 = [9, 4, 9, 8, 4]
x = Solution().intersect(n1, n2)
print(x)
