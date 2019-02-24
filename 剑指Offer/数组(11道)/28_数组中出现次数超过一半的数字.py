"""
题目描述:
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

"""
# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        counter = Counter(numbers)
        lens_half = len(numbers) // 2
        number_most = counter.most_common(1)
        if number_most[0][1] > lens_half:
            return number_most[0][0]
        else:
            return 0

if __name__ == '__main__':
    array = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    result = Solution()
    print(result.MoreThanHalfNum_Solution(array))
