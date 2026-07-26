class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def isSame(a,b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            
            return (
                a.val == b.val
                and isSame(a.left,b.left)
                and isSame(a.right,b.right)
            )
        return (
            isSame(root,subRoot)
            or self.isSubtree(root.left,subRoot)
            or self.isSubtree(root.right,subRoot)
        )