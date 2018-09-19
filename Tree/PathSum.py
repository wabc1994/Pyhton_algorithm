"""112. Path Sum"""

class Solution:

    def hasPathSum(self,root,sum):
        """
        //递归方法
        :param root:
        :param sum:
        :return:
        """
        if not root :
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.va

    def hasPathSum_1(self,root,sum):
        """
        DFS的非递归实现，用栈实现。
        :param root:
        :param sum:
        :return:
        """
        "第一次入展"
        stack = [(root, sum)]
        "栈不为空，"
        stack = [(root, sum)]
        while len(stack) > 0:
            "弹出后面的情况"
            node, tmp_sum = stack.pop()
            if node:
                if not node.left and not node.right and node.val == tmp_sum:
                    return True
                stack.append((node.right, tmp_sum - node.val))
                stack.append((node.left, tmp_sum - node.val))

        return False


    def hasPathSum_2(self,root,sum):
        """
        DFS的非递归实现，用队列实现。
        :param root:
        :param sum:
        :return:
        """
        "弹出后面的情况"

        queue = [(root, sum)]
        while len(queue) > 0:
            node, tmp_sum = queue.pop()
            if node:
                if not node.left and not node.right and node.val == tmp_sum:
                    return True
                "在位置后面弹出一个数据"
                queue.insert(0, (node.right, tmp_sum - node.val))
                queue.insert(0, (node.left, tmp_sum - node.val))

        return False
