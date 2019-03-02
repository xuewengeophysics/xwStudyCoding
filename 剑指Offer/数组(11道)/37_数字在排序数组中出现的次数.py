"""
题目描述：
统计一个数字在排序数组中出现的次数。

思路：
1、判断首尾两个边界条件。
2、因为data中都是整数，所以可以转变思路，不搜索k的首尾位置，而是搜索k-0.5和k+0.5，这两个数应该插入的位置，然后相减即可。

参考资料：
[1] https://www.nowcoder.com/questionTerminal/70610bf967994b22bb1c26f9ae901fa2

"""

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # 暴力法
        # return data.count(k)
        # 二分法
        # 判断首尾两个边界条件
        if data[0] > k or data[-1] < k:
            return 0
        else:
            return self.biSearch(data, k + 0.5) - self.biSearch(data, k - 0.5)

    def biSearch(self, data, num):
        startIndex = 0
        endIndex = len(data) - 1
        while startIndex <= endIndex:
            midIndex = (startIndex + endIndex) // 2
            if data[midIndex] < num:
                startIndex = midIndex + 1
            else:
                endIndex = midIndex - 1
        return startIndex

if __name__ == '__main__':
    array = [2, 3, 3, 5, 5, 7, 9, 11]
    target = 3
    result = Solution()
    print(result.GetNumberOfK(array, target))
