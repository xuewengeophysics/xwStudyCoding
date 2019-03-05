"""
题目描述：
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

具体思路：
1、n个2*1的小矩形，如果第1个竖放，设剩下2*(n-1)的大矩形有f(n-1)种覆盖方法，
                  如果第1个横放，设剩下2*(n-2)的大矩形有f(n-2)种覆盖方法，
             那么，这个2*n的大矩形有f(n-1)+f(n-2)种覆盖方法；
2、依此类推，递归算法。

"""

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        return self.rectCover(number-2) + self.rectCover(number-1)


if __name__ == '__main__':
    n = 3
    result = Solution()
    print(result.rectCover(n))
