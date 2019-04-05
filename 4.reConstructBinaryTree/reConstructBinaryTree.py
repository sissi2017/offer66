class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        node = TreeNode(pre[0])
        root_index = tin.index(pre[0])
        right_length = len(tin) - root_index - 1
        if root_index > 0:
            node.left = self.reConstructBinaryTree(pre[1: root_index + 1], tin[0:root_index])  # 构造左子树
        if right_length > 0:
            node.right = self.reConstructBinaryTree(pre[root_index + 1:], tin[root_index + 1:])  # 构造右子树
        return node
