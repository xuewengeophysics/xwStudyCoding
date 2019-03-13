"""
题目描述：
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。

输出描述：
对应每个测试案例，输出两个数，小的先输出。

参考资料：
[1] https://cuijiahua.com/blog/2018/01/basis_42.html

"""

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        length = len(array)
        if length <= 1:
            return []
        
        leftIndex = 0
        rightIndex = length - 1
        while leftIndex < rightIndex:
            currentSum = array[leftIndex] + array[rightIndex]
            if currentSum == tsum:
                return array[leftIndex], array[rightIndex]
            elif currentSum < tsum:
                leftIndex += 1
            else:
                rightIndex -= 1
                
        return []



if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12, 13]
    tsum = 12
    result = Solution()
    print(result.FindNumbersWithSum(array, tsum))
