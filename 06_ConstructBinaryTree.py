# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # 如果遍历序列为空，则根节点不存在
        if len(pre) == 0 or len(tin) == 0:
            return None

        # 前序遍历的第一个节点就是根节点
        root_value = pre[0]
        root_node = TreeNode(root_value)

        # 记录根节点在中序遍历中的索引位置
        tin_root_index = 0
        for i in range(len(tin)):
            if tin[i] == root_value:
                tin_root_index = i

        # 递归重建左子树
        if tin_root_index > 0:
            pre_child = pre[1:1 + tin_root_index]
            tin_child = tin[0:tin_root_index]
            root_node.left = self.reConstructBinaryTree(pre_child, tin_child)
        # 递归重建右子树
        if len(tin) - tin_root_index > 1:
            pre_child = pre[1 + tin_root_index:len(pre)]
            tin_child = tin[tin_root_index + 1:len(tin)]
            root_node.right = self.reConstructBinaryTree(pre_child, tin_child)

        # 返回根节点
        return root_node
