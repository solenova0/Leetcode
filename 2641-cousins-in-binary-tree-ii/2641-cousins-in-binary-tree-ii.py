# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        level_sums = []
        queue = deque([root])
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level_sums.append(level_sum)
        
        root.val = 0
        queue = deque([root])
        depth = 0
        
        while queue:
          
            next_level_sum = level_sums[depth + 1] if depth + 1 < len(level_sums) else 0
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                sib_sum = (node.left.val if node.left else 0) + \
                          (node.right.val if node.right else 0)
                
                if node.left:
                    node.left.val = next_level_sum - sib_sum
                    queue.append(node.left)
                if node.right:
                    node.right.val = next_level_sum - sib_sum
                    queue.append(node.right)
            
            depth += 1
            
        return root