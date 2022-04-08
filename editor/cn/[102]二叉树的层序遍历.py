# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    @staticmethod
    def levelOrder(root):
        if not root:
            return []
        res = list()
        LIST = [root]
        while LIST:
            res_temp = list()
            TEMP = list()
            for node in LIST:
                res_temp.append(node.val)
                if node.left:
                    TEMP.append(node.left)
                if node.right:
                    TEMP.append(node.right)
            res.append(res_temp)
            LIST = TEMP
        return res
# leetcode submit region end(Prohibit modification and deletion)
