# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self,target, array):
        # write code hererray
        if target is None or array is None:
            return False
        col = 0
        row = len(array)-1
        while row>=0 and col< len(array[0]):
            if target == array[row][col]:
                return True
            elif target>array[row][col]:
                col+=1
            elif target <array[row][col]:
                row-=1
        return False
