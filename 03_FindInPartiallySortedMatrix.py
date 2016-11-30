# -*- coding:utf-8 -*-

"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
"""


class Sulution:
    # array 二维列表
    def Find(self, target, array):

        row_count = len(array)  # 行数
        if row_count == 0:
            return False
        column_count = len(array[0])  # 列数
        if column_count == 0:
            return False

        # 与右上角的元素比较大小
        if target < array[0][column_count - 1]:
            for i in range(row_count):
                del array[i][column_count - 1]
            return self.Find(target, array)
        elif target > array[0][column_count - 1]:
            del array[0]
            return self.Find(target, array)
        else:
            return True
