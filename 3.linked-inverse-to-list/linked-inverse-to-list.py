# -*- coding:utf-8 -*-

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        list = []
        while listNode:
            list.append(listNode.val)
            listNode = listNode.next
        return list[::-1]
#构造链表函数
#读取链表，写到list,再将list反序