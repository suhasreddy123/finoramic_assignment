class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    result = []
    def binaryTreePathSum(self, root, target):
        if root is None:
            return self.result
        self.dfs(root, [], target)
        return self.result

    def dfs(self, node, tmp, target):
        tmp.append(node.val)
        #print(tmp)
        if node.left is None and node.right is None:
            if target == sum(tmp):
                print (tmp)
                self.result.append(tmp)
            print("b",tmp)
            tmp.pop()
            print("a",tmp)
            return

        if node.left:
            self.dfs(node.left, tmp, target)
        if node.right:
            self.dfs(node.right, tmp, target)
        tmp.pop()

if __name__ == "__main__":
    result=[]
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    result = Solution().binaryTreePathSum(root, 22)
