"""
题目描述：
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

思路：
递归

"""

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n < 0:
            return -1

        if n == 0:
            return 0

        if n == 1:
            return 1

        return self.Fibonacci(n-1) + self.Fibonacci(n-2)


if __name__ == '__main__':
    n = 10
    arrayFib = list(range(n+1))
    result = Solution()
    for i in range(len(arrayFib)):
        arrayFib[i] = result.Fibonacci(i)
    print(arrayFib[n])
