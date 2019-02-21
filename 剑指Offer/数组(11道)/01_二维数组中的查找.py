"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

思路：
1、先判断两个临界值：最小值（左上）和最大值（右下）
2、与右上角的值进行比较，若小于右上角的值，则不用与该列比较了，j左移；
                         若大于它，则不用与该行比较了，i下移
3、以此类推

参考资料：
[1] https://cuijiahua.com/blog/2017/11/basis_1.html
[2] https://github.com/amusi/coding-note/tree/master/Coding%20Interviews
"""

# -*- coding:utf-8 -*-
class Solution:

    def Find(self, target, array):
        if target < array[0][0]:
            return False

        rows = len(array)
        cols = len(array[0])

        if target > array[rows-1][cols-1]:
            return False
        else:
            i = 0
            j = cols - 1
            while i < rows and j >= 0:
                if target == array[i][j]:
                    return True
                elif target < array[i][j]:
                    j -= 1
                else:
                    i += 1

        return False

if __name__ == '__main__':
    array = [[1,  2,  8,  9],
             [2,  4,  9, 12],
             [4,  7, 10, 13],
             [6,  8, 11, 15]]

    target = 5

    result = Solution()
    print(result.Find(target, array))
