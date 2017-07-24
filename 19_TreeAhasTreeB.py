# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        # 两棵树有一棵为空，就不是子树
        if pRoot1 is not None and pRoot2 is not None:
            # 如果树A的当前节点与树B的根节点相同，则递归判断A的子节点与B的子节点是否相同
            if pRoot1.val == pRoot2.val:
                result = self.OneHasAnother(pRoot1, pRoot2)
            # 递归判断树A的左子树寻找与树B根节点相同的节点
            if result is False:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            # 递归判断树A的左子树寻找与树B根节点相同的节点
            if result is False:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    # 判断树A是否包含树B
    def OneHasAnother(self, pRoot1, pRoot2):
        # 如果树B没有子树了，树A可能有可能没有子树，表明树A包含树B
        if pRoot2 is None:
            return True
        # 如果树B还有子树，而树A反而没有了，则不包含
        if pRoot1 is None:
            return False
        # 当前对应节点不同，则不包含
        if pRoot1.val != pRoot2.val:
            return False
        # 递归判断左右子树
        leftResult = self.OneHasAnother(pRoot1.left, pRoot2.left)
        rightResult = self.OneHasAnother(pRoot1.right, pRoot2.right)
        return leftResult and rightResult
