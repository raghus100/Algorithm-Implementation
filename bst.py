class TreeNode:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.parent = None
        self.val = val

class Tree:
    def __init__(self):
        self.root = None
        self.size = None

    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self.insert_node(self.root, val)

    def del_value(self, val):
        if self.root.val == val:
            pass

    def print_inorder(self, root):
        parent = None
        if not root:
            return
        self.print_inorder(root.left)
        if root.parent:
            parent = root.parent.val
        print("parent %s: val %s:" %(parent, root.val))
        #print(root.val)
        self.print_inorder(root.right)


    def print_postorder(root):
        pass

    def pass_preorder(root):
        pass

    def insert_node(self,node, val):
        if node is None:
            node = TreeNode(val)
        if node.val > val:
            if node.left is None:
                node.left = TreeNode(val)
                node.left.parent = node
            else:
                self.insert_node(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
                node.right.parent = node
            else:
                self.insert_node(node.right, val)

if __name__ == '__main__':
    val = [10,5,15,3,7,13,18,1,6]
    t = Tree()
    for i in val:
        t.insert(i)
    t.print_inorder(t.root)
