# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def dfs(self, node, arr):
        if not node:
            return
        else:
            # Traverse in order
            self.dfs(node.left, arr)
            arr.append(node)
            self.dfs(node.right, arr)
            return

    def __init__(self, root):
        self.arr = []
        self.dfs(root, self.arr)        

    def next(self):
        """
        @return the next smallest number
        """
        node = self.arr.pop(0)
        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return len(self.arr) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()