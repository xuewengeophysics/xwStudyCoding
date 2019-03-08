"""
题目描述：
求1+2+3+...+n，
要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

思路：递归
1、将问题分解为sum(n) = n + sum(n-1);
2、分解后，除了数据规模不一样，求解思路完全一样；
3、递归终止条件为n等于1时，返回1。
"""

# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        if n == 1:
            return 1
        else:
            return n + self.Sum_Solution(n-1)
        
if __name__ == "__main__":
    result = Solution()
    print(result.Sum_Solution(10))
    
