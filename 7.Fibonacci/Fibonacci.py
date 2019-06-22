# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n==0:
            return 0 
        elif n==1:
            return 1
        else:
            fib0 = 0
            fib1 = 1
            for _ in range(2,n+1):
                fib0,fib1 = fib1,fib0+fib1
            return fib1
