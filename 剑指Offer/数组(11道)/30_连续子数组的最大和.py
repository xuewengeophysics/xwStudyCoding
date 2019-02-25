"""
题目描述：
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,
常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,
并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)

思路：
累加的子数组和，如果大于零，那么我们继续累加就行；否则，则需要剔除原来的累加和重新开始。找到最大的和。

"""

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        array_len = len(array)
        sum_temp = 0
        sum_list = []
        for each in array[0:]:
            sum_temp += each
            if sum_temp > 0:
                sum_list.append(sum_temp)
            else:
                sum_temp = 0

        return max(sum_list)

if __name__ == '__main__':
    array = [1, -2, 3, 10, -4, 7, 2, -5]
    result = Solution()
    print(result.FindGreatestSumOfSubArray(array))
