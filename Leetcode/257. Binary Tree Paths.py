from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def search_path(node, current_path):
            if current_path != "":
                current_path += "->"
            current_path += str(node.val)
            if node.left:
                search_path(node.left, current_path)
            if node.right:
                search_path(node.right, current_path)
            if not node.left and not node.right:
                paths.append(current_path)
        search_path(root, "")
        return paths