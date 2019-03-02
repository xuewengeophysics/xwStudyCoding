"""
题目描述：
给定一个数组A[0,1,...,n-1]，请构建一个数组B[0,1,...,n-1]，
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

思路：
分段法

"""
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        B = []
        lengths = len(A)
        if lengths == 0 or lengths == 1:
            return B
        else:
            for index in range(lengths):
                B.append(self.calBeforeNum(A, index) * self.calAfterNum(A, index))
            return B

    def calBeforeNum(self, A, index):
        i = 0
        before_num = 1
        while i < index:
            before_num *= A [i]
            i += 1
        return before_num

    def calAfterNum(self, A, index):
        i = len(A) - 1
        after_num = 1
        while i > index:
            after_num *= A[i]
            i -= 1
        return after_num


if __name__ == '__main__':
    array_A = [1, 2, 3, 4, 5]
    array_B = Solution()
    print(array_B.multiply(array_A))
