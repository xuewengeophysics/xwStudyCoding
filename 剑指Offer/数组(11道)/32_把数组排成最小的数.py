"""
题目描述：
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

思路：
1、构造一个比较函数，当str1+str2>str2+str1时，我们将字符串排序为[str2, str1]。
2、将字符串列表按照比较函数的规定进行冒泡排序（或其它方法排序），”小”的字符串往前排。
3、最后将字符串列表链接起来，便是所求。

参考资料：
[1] https://www.cnblogs.com/lliuye/p/9159152.html

"""

# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        array_len = len(numbers)
        for i in range(array_len-1):
            for j in range(i+1, array_len):
                if str(numbers[i])+str(numbers[j]) > str(numbers[j])+str(numbers[i]):
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return ''.join(str(s) for s in numbers)
    
if __name__ == '__main__':
    array = [3, 32, 321]
    result = Solution()
    print(result.PrintMinNumber(array))
