class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node,currSum,path):
            nonlocal res
            if not node:
                return None
            
            currSum += node.val
            path.append((node.val))

            if not node.left and not node.right and currSum == targetSum:
                res.append(list(path))
            
            dfs(node.left,currSum,path)
            dfs(node.right,currSum,path)

            path.pop()
        dfs(root,0,[])
        return res