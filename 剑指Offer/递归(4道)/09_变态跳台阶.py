"""
题目描述：
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。

具体思路：
1、也可以用逆推的思路去想，跳n级台阶，可以直接跳上去，也可以从n-1级跳上来，
   也可以从n-2级跳上来，依次下去，从第0级跳上去；设跳到n-1级有f(n-1)种跳法，
   所以，跳n级台阶的方法数相当于其它所有台阶数的方法的总和再加上直接跳上来这1种，
   表达式为f(n)  = 1 + f(n-1) + f(n-2) +...+ f(2) + f(1) + f(0)
          f(n-1) = 1 + f(n-2) + f(n-2) +...+ f(2) + f(1) + f(0)
   所以可得f(n) - f(n-1) = f(n-1)
   即f(n) = 2 * f(n-1)

参考资料：
[1] https://blog.csdn.net/not_guy/article/details/78842473


"""

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        return 2 * self.jumpFloorII(number - 1)


if __name__ == '__main__':
    n = 3
    result = Solution()
    print(result.jumpFloorII(n))
