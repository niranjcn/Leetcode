from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clone = {}

        def dfs(node):
            if node in clone:
                return clone[node]
            
            clone[node] = Node(node.val)

            for nei in node.neighbors:
                clone[node].neighbors.append(dfs(nei))

            return clone[node]
        return dfs(node)