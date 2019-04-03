# -*- coding:utf-8 -*-
import numpy as np
class Solution:
    # array 二维列表
    def Find(self, target, array):
        array = np.array(array)
        row = len(array) - 1
        col = len(array[0]) - 1
        i = row
        j = 0
        while i >= 0 and j <= col:
            if target < array[i][j]:
                i = i - 1
            elif target > array[i][j]:
                j = j + 1
            else:
                return True

a=Solution()
target = 7
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print(a.Find(target,array))

# 实际上python当中没有数组的概念, 而是列表(List), 二维列表相当于二维数组 。
# python中创建二维数组

# 由于数组元素是分别按行按列递增的，故可以：
#
# 从最后一行第一列开始遍历
# 记给定的整数为target，数组元素为array[i][j]
# 如果 target < array[i][j] 则行数减1
# 如果 target > array[i][j] 则列数加1
# 如果 target == array[i][j] 则返还True
