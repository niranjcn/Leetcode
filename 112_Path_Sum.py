class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,currSum):
            if not node:
                return False

            currSum += node.val

            if not node.left and not node.right:
                return currSum == targetSum

            left = dfs(node.left, currSum)
            right = dfs(node.right, currSum)

            return left or right

            return targetSum == currSum
        return dfs(root,0)