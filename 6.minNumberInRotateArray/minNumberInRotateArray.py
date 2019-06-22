# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0:
            return 0
        head = 0
        rear = len(rotateArray)-1
        if rotateArray[head]<rotateArray[rear]:
            return rotateArray[head]
        while(head!=rear-1):
            mid = (head+rear)//2
            if rotateArray[mid]>=rotateArray[head]:
                head = mid
                continue
            if rotateArray[mid]<=rotateArray[rear]:
                rear = mid
                continue
        return rotateArray[rear]
