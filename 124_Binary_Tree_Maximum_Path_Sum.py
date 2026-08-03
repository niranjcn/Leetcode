class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = max(0,dfs(node.left))
            right = max(0,dfs(node.right))

            res = max(res,(left+right+node.val))

            return node.val + max(left,right)
        dfs(root)
        return res