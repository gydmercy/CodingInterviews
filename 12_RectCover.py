# -*- coding:utf-8 -*-

"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""


class Solution:
    def rectCover(self, number):

        if number < 3:
            return number

        ele1, ele2 = 1, 2

        for i in range(3, number + 1):
            elei = ele1 + ele2
            ele1 = ele2
            ele2 = elei

        return ele2
