class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root, res):
            if not root:
                return None
            
            dfs(root.left,res)
            res.append(root.val)
            dfs(root.right,res)
        
        dfs(root,res)
        return res