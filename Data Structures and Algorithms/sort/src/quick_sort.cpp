/*
Summary: 快速排序（C++ implementation QuickSort）
Author: Xue Wen
Date:   2019-08-25
Reference:
[1] Cormen, Leiserson, 算法导论
[2] https://github.com/TheAlgorithms/C-Plus-Plus/blob/master/Sorting/Quick%20Sort.cpp
通俗理解：逐步前后分段排序
基本思想：通过一趟排序将待排列表分隔成独立的两段，其中前一段的所有元素均比后一段的所有元素小，
        然后分别对这两段重复此操作，以达到整个序列有序。（这个过程，我们可以使用递归快速实现）
步骤：
快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：
1、从数列中挑出一个元素，称为 “基准”（pivot），这里我们通常都会选择最后一个元素作为pivot；
2、重新排序数列，将比基准值小的所有元素放在基准前面，比基准值大的所有元素放在基准的后面（相同的数可以到任一边）。
   这样操作完成后，该基准就处于新数列的中间位置，即将数列分成了两部分，这个操作称为分区（partition）操作。
3、递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列按上述操作进行排序。
   这里的递归结束的条件是序列的大小为0或1。此时递归结束，排序就完成了。
稳定性：不稳定（由于关键字的比较和交换是跳跃进行的，所以快速排序是一种不稳定的排序方法～）
复杂度分析：
1、时间复杂度：平均O(nlogn)；最好O(nlogn)；最差O(n^2)。
2、空间复杂度：平均O(nlogn)；最好O(nlogn)；最差O(n)。
*/

#include <iostream>
using namespace std;

int partition(int array[], int start, int end)
{
    int pivot = array[end];       // 将最后一个元素设置为基准值
    int lessIndex = (start - 1);  // Index of smaller element
    // 从左往右扫描
    for (int j = start; j < end; j++)
    {
        // If current element is smaller than or equal to pivot
        if (array[j] <= pivot)
        {
            lessIndex++;  // increment index of smaller element
            // 目的是将小于等于pivot的数存在[start, lessIndex]中，大于pivot的数存在[lessIndex+1, j]中
            int temp = array[lessIndex];
            array[lessIndex] = array[j];
            array[j] = temp;
        }
    }

    // 此时，大于pivot的数都存在了[lessIndex+1, j]中；
    // 将lessIndex+1作为一个分界点，用于存pivot，将其与最后一个元素(即pivot)交换即可
    int temp = array[lessIndex + 1];
    array[lessIndex + 1] = array[end];
    array[end] = temp;

    return (lessIndex + 1);
}

void quickSort(int array[], int start, int end)
{
    if (start < end)
    {
        int pivotLocation = partition(array, start, end);

        quickSort(array, start, pivotLocation - 1);
        quickSort(array, pivotLocation + 1, end);
    }
}

void show(int array[], int size)
{
    for (int i = 0; i < size ; i++)
        cout << array[i] << " ";
}


int main()
{
    int size = 11;
    int array[11] = {1, 3, 8, 5, 2, 10, 7, 16, 7, 4, 5};
    cout << "\nOriginal array" << endl;
    show(array, size);

    quickSort(array, 0, size - 1);
    cout << "\nQuickSorted array" << endl;
    show(array, size);
    return 0;
}
