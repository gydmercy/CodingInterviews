# -*- coding:utf-8 -*-

"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""


class Solution1:
    # 初始化两个栈
    stack1 = []
    stack2 = []

    def push(self, node):
        # 添加元素统统添加到 stack1 中
        self.stack1.append(node)

    def pop(self):
        # 删除的元素始终从 stack2 中退栈
        # 假如 stack2 为空，则先把 stack1 中的元素转移到 stack2 中
        if len(self.stack2) == 0:
            # 两个栈中都没有元素，就返回 None
            if len(self.stack1) == 0:
                return None
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()


"""
相反：用两个队列来实现一个栈
"""


class Solution2:
    # 初始化两个队列
    # 要模拟栈，经过分析，插入之前或者说删除之后，必有至少一个队列是空的
    queue1 = []
    queue2 = []

    def push(self, node):
        # 将元素插入非空的队列中，若都为空，则任意选择一个
        if len(self.queue1) != 0:
            self.queue1.append(node)
        elif len(self.queue2) != 0:
            self.queue2.append(node)
        else:
            self.queue1.append(node)

    def pop(self):
        # 从非空的队列中删除元素，删除之前，先把除了要删除元素(当前队列最后一个)之外的元素都转移到另一个队列中
        if len(self.queue1) > 0:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop()
        if len(self.queue2) > 0:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop()
        # 两个队列都为空，就返回 None
        return None
