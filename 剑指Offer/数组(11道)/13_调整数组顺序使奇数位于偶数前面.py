"""
题目描述：
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。

"""

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        array_len = len(array)
        array_reOrder = []
        i = 0
        while i <= array_len-1:
            array_reOrder.append(array[i])
            i += 2

        j = 1
        while j <= array_len-1:
            array_reOrder.append(array[j])
            j += 2

        return array_reOrder

if __name__ == '__main__':
    array = [5, 1, 2, 3, 4]
    result = Solution()
    print(result.reOrderArray(array))
