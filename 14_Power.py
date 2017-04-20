# -*- coding:utf-8 -*-

"""
给定一个double类型的浮点数base和int类型的整数exponent。
求base的exponent次方。
"""


class Solution:
    def Power(self, base, exponent):

        # 若底数为 0，则直接返回结果，防止出现底数为 0 指数为负数的情况而出错
        if abs(base - 0) < 0.0000001:
            return 1

        result = 1

        if exponent > 0:
            for i in range(exponent):
                result *= base
        elif exponent < 0:
            exponent = 0 - exponent
            for i in range(exponent):
                result *= base
            result = 1.0 / result

        return result
