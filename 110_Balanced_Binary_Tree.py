class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0,True
            
            left,l_bal = dfs(node.left)
            right,r_bal = dfs(node.right)
            
            height =  1 + max(left,right)

            if not l_bal or not r_bal or abs(left-right) > 1:
                return height, False
            
            return height, True
        height, balanced = dfs(root)
        return balanced