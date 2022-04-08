# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    @staticmethod
    def levelOrder(root) -> List[List[int]]:
        if not root:
            return []
        nodes, res = [root], []
        while nodes:
            nxt, cur = [], []
            for node in nodes:
                cur.append(node.val)
                nxt += [child for child in node.children]
            nodes = nxt
            res.append(cur)
        return res
# leetcode submit region end(Prohibit modification and deletion)
