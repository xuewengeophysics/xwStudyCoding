"""
Summary: 快速排序（Quick Sort）
Author: Xue Wen
Date:   2019-02-20
Reference:
[1] Cormen, Leiserson, 算法导论.
[2] https://github.com/amusi/coding-note/tree/master/Data%20Structures%20and%20Algorithms/sort

通俗理解：逐步前后分段排序
基本思想：通过一趟排序将待排列表分隔成独立的两部分，其中一部分的所有元素均比另一部分的所有元素小，
          则可分别对这两部分继续重复进行此操作，以达到整个序列有序。（这个过程，我们可以使用递归快速实现）

步骤：
快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：
1、从数列中挑出一个元素，称为 “基准”（pivot），这里我们通常都会选择最后一个元素作为prvot；
2、重新排序数列，将比基准值小的所有元素放在基准前面，比基准值大的所有元素放在基准的后面（相同的数可以到任一边）。
   这样操作完成后，该基准就处于新数列的中间位置，即将数列分成了两部分，这个操作称为分区（partition）操作。
3、递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数按上述操作进行排序。
   这里的递归结束的条件是序列的大小为0或1。此时递归结束，排序就完成了。

稳定性：不稳定（由于关键字的比较和交换是跳跃进行的，所以快速排序是一种不稳定的排序方法～）

复杂度分析：
1、时间复杂度：平均O(nlogn)；最好O(nlogn)；最差O(n^2)。
2、空间复杂度：平均O(nlogn)；最好O(nlogn)；最差O(n)。

"""
def QuickSort(array, start, end):
    if start < end:
        pivotLocation = partition(array, start, end)
        QuickSort(array, start, pivotLocation-1)
        QuickSort(array, pivotLocation+1, end)

# 数组分段
def partition(array, start, end):
    # 将最右边的值设置为基准值
    pivot = array[end]
    less_index = start - 1
    # 从左往右扫描
    for j in range(start, end):
        if array[j] <= pivot:
            less_index = less_index + 1
            # 目的是将小于pivot的数存在less_index中，大于pivot的数存在j中
            array[less_index], array[j] = array[j], array[less_index]    # 对start而言于不交换；其它情况为大小值互换位置
    # 将less_index+1是一个分界点，并将其与最后一个值交换
    array[less_index+1], array[end] = pivot, array[less_index+1]
    return less_index+1

if __name__ == '__main__':
    array = [1, 3, 8, 5, 2, 10, 7, 16, 7, 4, 5]
    print("Original array: ", array)
    # array = QuickSort(array, 0, len(array)-1)
    # 因为python中的list对象是可变对象，所以在函数做"形参"时，是相当于按引用传递
    # 所以不写成返回值的形式，也是OK的
    QuickSort(array, 0, len(array) - 1)
    print("QuickSort: ", array)
