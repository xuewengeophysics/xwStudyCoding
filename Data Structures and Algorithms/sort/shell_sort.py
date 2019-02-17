"""
Summary: 希尔排序（Shell Sort）
Author: Xue Wen
Date:   2019-02-17
Reference:
[1] https://github.com/amusi/coding-note/tree/master/Data%20Structures%20and%20Algorithms/sort

通俗理解：改进的插入排序，小元素跨步前置
基本思想：设待排序元素序列有n个元素，首先取一个整数grap（小于n）作为间隔将全部元素分为grap个子序列，
          所有距离为grap的元素放在同一个子序列中，在每一个子序列中分别实行插入排序。

说明：在希尔排序算法提出之前，排序算法的时间复杂度都为O(n^2)，如冒泡排序、选择排序和插入排序；
      而希尔排序算法是突破这个时间复杂度的第一批算法之一，该复杂度为O(nlogn)。
      它是直接插入排序算法的改进版，也称为缩小增量排序。
      希尔排序减少了其复制的次数，速度要快很多。
      原因是，当n值很大时，数据项每一趟排序需要移动的个数很少，但数据项的距离很长；
              当n值减小时，每一趟需要移动的数据增多。正是因为这两种情况的结合才使得希尔排序效率比插入排序高很多。
步骤：
先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，具体算法描述：
1、选择一个增量序列t1，t2，…，tk
2、按增量序列个数k，对序列进行k 趟排序；
3、每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。
   仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
注：增量的初始值一般为序列长度的一半，然后之后每次再自身减半。

稳定性：不稳定

复杂度分析：
1、时间复杂度：平均O(n^1.3)；最差O(n^2)；最好O(n)。
2、空间复杂度：O(1)

"""

def ShellSort(array):
    array_len = len(array)
    # 初始化gap
    grap = array_len // 2
    # 减少增量，遍历子序列进行插入排序
    while grap > 0:
        for i in range(grap, array_len):    # 分成多少段序列，就有多少轮
            currentValue = array[i]    # 当前要插入的值
            preIndex = i-grap    # 前一个值的索引
            # 循环条件：前一个索引对应元素值大于当前值，前一个索引值大于等于0
            # 子序列插入排序
            while preIndex >= 0 and array[preIndex] > currentValue:
                array[preIndex+grap] = array[preIndex]    # 前一个索引对应元素往后移
                preIndex -= grap    # 待比较元素的前一个索引前移
            array[preIndex+grap] = currentValue    # 当array[preIndex] < currentValue时，循环结束，将currentValue放在preIndex后
        grap = grap // 2

    return array

if __name__ == '__main__':
    array = [1, 3, 8, 5, 2, 10, 7, 16, 7, 4, 5]
    print("Original array: ", array)
    array = ShellSort(array)
    print("ShellSort: ", array)
