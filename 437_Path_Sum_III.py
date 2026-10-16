class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefix = {0: 1}

        def dfs(node, currSum):
            if not node:
                return 0

            currSum += node.val

            count = prefix.get(currSum - targetSum, 0)

            prefix[currSum] = prefix.get(currSum, 0) + 1

            count += dfs(node.left, currSum)
            count += dfs(node.right, currSum)

            prefix[currSum] -= 1

            return count

        return dfs(root, 0)