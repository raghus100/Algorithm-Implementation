from collections import deque
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
        self.q = deque()

    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)

        else:
            self.q.append(self.root)
            self.insert_node(self.root, val)

    def insert_node(self, node, val):
        while(self.q):
            temp_node = self.q.popleft()
            if temp_node.left is None:
                temp_node.left = TreeNode(val)
                temp_node.left.parent = temp_node
                break
            elif temp_node.right is None:
                temp_node.right = TreeNode(val)
                temp_node.right.parent = temp_node
                break
            else:
                self.q.append(temp_node.left)
                self.q.append(temp_node.right)
        self.q.clear()

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

if __name__ == '__main__':
    val = [3,5,1,6,2,0,8,None,None,7,4]
    t = Tree()
    for i in val:
        t.insert(i)
    t.print_inorder(t.root)