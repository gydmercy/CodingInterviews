# -*- coding:utf-8 -*-

"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # 数组大小为0，则返回0
        if len(rotateArray) == 0:
            return 0
        # 数组大小为1，则返回该元素
        if len(rotateArray) == 1:
            return rotateArray[0]

        i, j = 0, len(rotateArray) - 1

        # 如果 rotateArray[i] < rotateArray[j]，则表示根本没旋转，则返回第一个元素即 rotateArray[i]
        while rotateArray[i] >= rotateArray[j]:

            if j - i == 1:
                return rotateArray[j]

            mid = (i + j) / 2

            # 考虑左边元素与右边元素、中间元素相等的情况，这种情况无法缩小寻找范围，则直接顺序查找
            if rotateArray[mid] == rotateArray[i] and rotateArray[mid] == rotateArray[j]:
                min = rotateArray[0]
                for ele in rotateArray:
                    if ele < min:
                        min = ele
                return ele

            if rotateArray[mid] >= rotateArray[i]:
                i = mid
            elif rotateArray[mid] <= rotateArray[j]:
                j = mid

        return rotateArray[i]
