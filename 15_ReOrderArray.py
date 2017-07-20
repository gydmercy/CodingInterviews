# -*- coding:utf-8 -*-

"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""


class Solution:
    def reOrderArray(self, array):
        for i in range(len(array)):
            value = array[i]
            # 如果当前元素是奇数，就插入到最前面的偶数之前
            if value % 2 != 0:
                j = i - 1
                while j >= 0 and array[j] % 2 == 0:
                    array[j + 1] = array[j]
                    j = j - 1
                array[j + 1] = value
        return array
