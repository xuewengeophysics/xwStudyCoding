"""
Summary: 插入排序（Insertion Sort）
Author: Xue Wen
Date:   2019-02-17
Reference:
[1] https://github.com/amusi/coding-note/tree/master/Data%20Structures%20and%20Algorithms/sort

通俗理解：小元素逐步前置
基本思想：插入排序（insertion sort）又称直接插入排序（staright insertion sort），
          将未排序元素一个个插入到已排序列表中。对于未排序元素，在已排序序列中从后向前扫描，找到相应位置把它插进去；
          在从后向前扫描过程中，需要反复把已排序元素逐步向后挪，为新元素提供插入空间。
步骤：
1、从第一个元素开始，该元素可以认为已经被排序；
2、取出下一个元素（未排序），在已经排序的元素序列中从后向前扫描；
3、如果该元素（已排序）大于新元素，将该已排序元素移到下一位置，将该新元素往前移动；
4、重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
5、将新元素插入到该位置后；
6、重复步骤2~5。

说明：
1、有n个元素，那么第1轮迭代，需要比较1次（因为第一个元素可以认为已经被排序）；
2、每次迭代完成后确定了前i+1个元素已排好序；
3、第2轮迭代，需要比较i次；
4、第n-1轮比较迭代，需要比较n-1次，此时完成选择排序操作。

时间复杂度：O(n^2) = (n-1)*(n-1)

复杂度分析：
1、时间复杂度：O(n2)。注：无论什么数据进去，选择都是O(n2)的时间复杂度，所以若要使用它，建议数据规模越小越好。
2、空间复杂度：O(1)

"""

def InsertionSort(array):
    array_len = len(array)
    for i in range(1, array_len):    # n-1轮
        currentValue = array[i]    # 当前要插入的值
        preIndex = i-1    # 前一个值的索引
        # 循环条件：前一个索引对应元素值大于当前值，前一个索引值大于等于0
        while preIndex >=0 and array[preIndex] > currentValue:
            array[preIndex+1] = array[preIndex]    # 前一个索引对应元素往后移
            preIndex -= 1    # 待比较元素的前一个索引前移
        array[preIndex+1] = currentValue    # 当array[preIndex] < currentValue时，循环结束，将currentValue放在preIndex后

    return array

if __name__ == '__main__':
    array = [1, 3, 8, 5, 2, 10, 7, 16, 7, 4, 5]
    print("Original array: ", array)
    array = InsertionSort(array)
    print("InsertionSort: ", array)
