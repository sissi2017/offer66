# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code hererray
        for num in range(len(array)):
            item = array[num]
            print(item)
            for i in range(len(item)):
                print(item[i])
                if target == item[i]:
                    return True

        return False

a=Solution()
target = 7
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print(a.Find(target,array))