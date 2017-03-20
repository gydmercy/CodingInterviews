# -*- coding:utf-8 -*-

"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
"""


# 使用 循环 的方式
class Solution1:
    def Fibonacci(self, n):

        if n < 2:
            return n

        ele1, ele2 = 0, 1

        for i in range(2, n + 1):
            elei = ele1 + ele2
            ele1 = ele2
            ele2 = elei

        return ele2


# 使用 尾递归 的方式
class Solution2:
    def Fibonacci(self, n):

        if n < 2:
            return n

        ele1, ele2 = 0, 1

        return self.tail_recursion(n, ele1, ele2)

    def tail_recursion(self, n, ele1, ele2):
        if n < 2:
            return ele2
        return self.tail_recursion(n - 1, ele2, ele1 + ele2)
