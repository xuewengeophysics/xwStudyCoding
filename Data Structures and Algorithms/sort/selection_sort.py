"""
Summary: 选择排序（Selection Sort）
Author: Xue Wen
Date:   2019-02-17
Reference:
[1] https://github.com/amusi/coding-note/tree/master/Data%20Structures%20and%20Algorithms/sort

通俗理解：最小（大）元素置首
基本思想：首先，在未排序的序列中找到最小（大）元素，存放到排序序列的起始位置；
          然后，再从剩余未排序元素中继续寻找最小（大）元素，放到当前序列的起始位置；
          以此类推，直到所有元素均排序完毕。
步骤：
1、每轮找出一个最小值，因此有n-1轮；
2、第i轮排序，将最小值下标min_index设为i，然后与当前无序序列逐个比较，找出最小值R[j]，此时最小值下标min_index置为j；
   并将它与当前序列第1个记录R[i]交换；
3、第n-1轮结束时，数组有序化了。

说明：
1、有n个元素，那么第1轮迭代，需要比较n-1次（因为第一个元素不用相互比较）；
2、此次迭代完成后确定了第一个元素为最小值；
3、第2轮迭代，需要比较n-2次，因为第1轮迭代已经确定好了第一个元素为最小值，所以不再加入序列进行排序；
4、第i轮比较迭代，需要比较n-i次，此时确定的前面i个元素是有序的较小元素；
5、第n-1轮比较迭代，需要比较n-(n-1)次，此时完成选择排序操作。

时间复杂度：O(n^2) = (n-1)*(n-1)

改进：当某一轮迭代中没有交换位置的操作，说明已经排好序了，就没必要再循环了，break退出循环即可。

复杂度分析：
1、时间复杂度：O(n2)。注：无论什么数据进去，选择都是O(n2)的时间复杂度，所以若要使用它，建议数据规模越小越好。
2、空间复杂度：O(1)

"""

def SelectionSort(array):
    array_len = len(array)
    for i in range(array_len - 1):    # n-1轮
        min_index = i
        for j in range(i+1, array_len):    # 找出最小值的下标
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array

if __name__ == '__main__':
    array = [1, 3, 8, 5, 2, 10, 7, 16, 7, 4, 5]
    print("Original array: ", array)
    array = SelectionSort(array)
    print("SelectionSort: ", array)
