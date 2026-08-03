class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_idx = 0
        inorder_index = {}
        for i, val in enumerate(inorder):
            inorder_index[val] = i
        
        def dfs(left,right):
            if left > right:
                return None
            nonlocal pre_idx
            root = TreeNode(preorder[pre_idx])
            pre_idx += 1

            mid = inorder_index[root.val]

            root.left = dfs(left,mid - 1)
            root.right = dfs(mid + 1,right)

            return root
        return dfs(0,len(preorder)-1)