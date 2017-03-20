# -*- coding:utf-8 -*-

"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""


class Solution:
    # 其实就是斐波那契数列，但是初始值不同
    def jumpFloor(self, number):
        # 初始值从 1 开始，索引序列也从 1 开始，即 1,2,3,5,8...
        if number <= 2:
            return number

        ele1, ele2 = 1, 2

        return self.tail_recursion(number, ele1, ele2)

    def tail_recursion(self, n, ele1, ele2):
        if n < 3:
            return ele2
        return self.tail_recursion(n - 1, ele2, ele1 + ele2)
