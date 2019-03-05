"""
题目描述：
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

具体思路：
1、n级台阶，如果第1步跳1级，设剩下n-1级的跳法有f(n-1)种，
           如果第1步跳2级，设剩下n-2级的跳法有f(n-2)种，
           那么，这n级台阶的跳法就有f(n-1)+f(n-2)种；
2、依此类推，递归算法。

参考资料：
[1] https://cuijiahua.com/blog/2017/11/basis_8.html

"""

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        return self.jumpFloor(number-2) + self.jumpFloor(number-1)



if __name__ == '__main__':
    n = 5
    result = Solution()
    print(result.jumpFloor(n))
