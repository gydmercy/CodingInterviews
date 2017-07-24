# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
操作给定的二叉树，将其变换为源二叉树的镜像。
"""


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root is not None:
            # 交换左右节点
            root.left, root.right = root.right, root.left
            # 递归遍历左右子树，继续交换
            self.Mirror(root.left)
            self.Mirror(root.right)
        return root
