"""
题目描述：
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

思路：
使用两个stack，一个为数据栈，另一个为辅助栈。数据栈用于存储所有数据，辅助栈用于存储最小值。
举个例子：
入栈的时候：首先往空的数据栈里压入数字3，显然现在3是最小值，我们也把最小值压入辅助栈。
            接下来往数据栈里压入数字4。由于4大于之前的最小值，因此我们只要入数据栈，不压入辅助栈。
            辅助栈中后入的数据必定是越来越小的，所以辅助栈顶就是最小值。
出栈的时候：当数据栈和辅助栈的栈顶元素相同的时候，辅助栈的栈顶元素出栈。否则，数据栈的栈顶元素出栈。
            因为辅助栈顶总是代表当前数组栈中的最小值，当两个栈顶相等时，此时数组栈顶为最小值，
            所以我们也要将辅助栈顶删除，以确保辅助栈顶总是代表数组栈中的最小值。
栈顶元素：直接返回数据栈的栈顶元素。
栈最小元素：直接返回辅助栈的栈顶元素。

参考资料：
[1] https: // blog.csdn.net / qq_34178562 / article / details / 79768874
[2] https://cuijiahua.com/blog/2017/12/basis_20.html
"""

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.dataStack = []
        self.minStack = []

    def push(self, node):
        if len(self.minStack) == 0:
            self.minStack.append(node)
        if self.minStack[-1] > node:
            self.minStack.append(node)
        self.dataStack.append(node)

    def pop(self):
        if self.dataStack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.dataStack.pop()

    def top(self):
        return self.dataStack[-1]

    def min(self):
        return self.minStack[-1]

if __name__ == "__main__":
    # 测试部分
    mStack = Solution()
    mStack.push(15)
    print("Data: ", mStack.dataStack)
    print("Min: ", mStack.min())
    mStack.push(-1)
    print("Data: ", mStack.dataStack)
    print("Min: ", mStack.min())
    mStack.push(2.6)
    print("Data: ", mStack.dataStack)
    print("Min: ", mStack.min())
    mStack.push(0)
    print("Data: ", mStack.dataStack)
    print("Min: ", mStack.min())
    mStack.push(-6)
    print("Data: ", mStack.dataStack)
    print("Min: ", mStack.min())
    mStack.push(100)
    print("Data: ", mStack.dataStack)
    print("Min: ", mStack.min())
    mStack.push(0.6)
    print("Data: ", mStack.dataStack)
    print("Min: ", mStack.min())
    mStack.pop()
    print("Data: ", mStack.dataStack)
    print("Min: ", mStack.min())
    mStack.pop()
    print("Data: ", mStack.dataStack)
    print("Min: ", mStack.min())
    mStack.pop()
    print("Data: ", mStack.dataStack)
    print("Min: ", mStack.min())
