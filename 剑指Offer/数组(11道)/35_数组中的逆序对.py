"""
题目描述：
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
输入描述：
题目保证输入的数组中没有的相同的数字
数据范围：
	对于%50的数据,size<=10^4
	对于%75的数据,size<=10^5
	对于%100的数据,size<=2*10^5
    
"""

# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        array_len = len(data)
        p = 0
        for i in range(array_len-1):
            for j in range(i+1, array_len):
                if data[i] > data[j]:
                    p += 1
        return p%1000000007
    
if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 0]
    result = Solution()
    print(result.InversePairs(array))

