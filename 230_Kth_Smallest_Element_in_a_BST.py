class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(node):
            if not node:
                return
                
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return res[k-1]