
class Solution:
    def preorderTraversal(self, root):
        result = []

        def preorder(node):
            if node:
                result.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return result

        