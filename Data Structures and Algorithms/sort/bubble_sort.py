"""
Summary: 冒泡排序（Bubble Sort）
Author: Xue Wen
Date:   2019-02-17
Reference:
[1] https://github.com/amusi/coding-note/tree/master/Data%20Structures%20and%20Algorithms/sort

通俗理解：大值后移法（降序则为小值后移法）
基本思想：比较相邻的两个元素，将值大的元素交换到右边（降序则相反）
步骤：
1、比较相邻的元素。如果第一个比第二个大，就交换它们两个；
2、对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
3、针对所有的元素重复以上的步骤，除了最后一个；
4、重复步骤1~3，直到排序完成。
说明：
1、有n个元素，那么第一轮迭代，需要比较n-1次（因为是相邻成对比较，最后一个元素没有下一个相邻对象，所以是n-1次）；
2、此次迭代完成后确定了最后一个元素为最大值；
3、第二轮迭代，需要比较n-2次，因为第一轮迭代已经确定好了最后一个元素为最大值，所以不再需要比较；
4、第i轮比较迭代，需要比较n-i次，此时确定后面i个元素是有序的较大元素；
5、第n-1轮比较迭代，需要比较n-(n-1)次，此时完成冒泡排序操作。

时间复杂度：o(n^2) = (n-1)*(n-1)
稳定性：稳定
改进：当某一轮迭代中没有交换位置的操作，说明已经排好序了，就没必要再循环了，break退出循环即可。

复杂度分析：
1、时间复杂度：若给定的数组刚好是排好序的数组，采用改进后的冒泡排序算法，只需循环一次就行了，此时是最优时间复杂度：O(n)，
               若给定的是倒序，此时是最差时间复杂度：O(n^2) ，因此综合平均时间复杂度为：O(n^2)
2、空间复杂度：因为每次只需开辟一个temp的空间，因此空间复杂度是：O(1)
"""

def BubbleSort(array):
    array_len = len(array)
    for i in range(array_len - 1):    # 每轮找最大值排最后，所以要迭代n-1轮
        for j in range(array_len - 1 - i):    # 原本应该比较n-i次，但程序中i的起始值为0，而实际是1，所以为n-1-i
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array

if __name__ == '__main__':
    array = [1, 3, 8, 5, 2, 10, 7, 16, 7, 4, 5]
    print("Original array: ", array)
    array = BubbleSort(array)
    print("SelectionSort: ", array)
