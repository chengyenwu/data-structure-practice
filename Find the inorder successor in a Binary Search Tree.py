# Find the inorder successor in a BST
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findmin(self, node):
        current = node
        while current != None:
            if current.left != None:
                current = current.left
        return current
    
    def insert_node(self, node, val):
        if node == None:
            return Node(val)
        else:
            if val <= node.val:
                temp = self.insert_node(node.left, val)
                node.left = temp
                temp.parent = node
            else:
                temp = self.insert_node(node.right, val)
                node.right = temp
                temp.parent = node
        return node
    def inorder_successor(self, node):
        if node.right != None:
            return Solution.findmin(node.right)
        p = node.parent
        while p != None:
            if p.right == node:
                node = p
                p = p.parent
            else:
                break
        return p

solution = Solution()
root = None
root = solution.insert_node(root, 20)
root = solution.insert_node(root, 8)
root = solution.insert_node(root, 22)
root = solution.insert_node(root, 4)
root = solution.insert_node(root, 12)
root = solution.insert_node(root, 10)
root = solution.insert_node(root, 14)

temp = root.left.right.right
successor = solution.inorder_successor(temp)

if successor != None:
    print("Inorder successor of %d is %d" % (temp.val, successor.val))