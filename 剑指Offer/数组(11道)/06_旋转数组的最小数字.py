"""
题目描述:
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

思路：
如果一个元素比前一个元素小，那么这个元素就是最小值。
1、找到数组中间元素，如果它大于最左侧指针指向的元素，那么中间元素位于前面的递增子数组；
   此时最小元素应该位于该中间元素之后，然后我们把最左侧指针指向该中间元素，移动之后最左侧指针仍然位于前面的递增子数组中。
2、如果中间元素小于最左侧指针指向的元素，那么中间元素位于后面的递增子数组；
   此时最小元素应该位于该中间元素之前，然后我们把最右侧指针指向该中间元素，移动之后最右侧指针仍然位于后面的递增子数组中。
3、最左侧指针总是指向前面递增数组的元素，最右侧指针总是指向后面递增数组的元素，最终它们会指向两个相邻的元素。
4、当最右侧指针指向的元素比它前一个元素小，这就是循环结束的条件。

"""

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        array_len = len(rotateArray)
        if array_len == 0:
            return 0
        elif array_len == 1 or array_len == 2:
            return rotateArray[array_len-1]
        else:
            left = 0
            middle = array_len // 2
            right = array_len - 1

            while rotateArray[right-1] <= rotateArray[right]:
                if rotateArray[middle] > rotateArray[left]:
                    left = middle
                else:
                    right = middle
                middle = (right + left) // 2
        return rotateArray[right]


if __name__ == '__main__':
    array = [5, 6, 7, 8, 8, 9, 9, 1, 1, 2, 3, 4]
    result = Solution()
    print(result.minNumberInRotateArray(array))
