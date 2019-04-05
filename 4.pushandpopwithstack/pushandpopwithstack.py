class Solution:
    stack1=[]
    stack2=[]
    def push(self, node):
        self.stack1.append(node)
        # write code here
    def pop(self):
        # return xx
        if len(self.stack2)>0:
            return self.stack2.pop()
        else:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
            return self.pop()
