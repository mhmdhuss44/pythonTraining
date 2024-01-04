class Node:
    def __init__(self, key):
        # value and two sons in a binary tree
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        return self.search_helper(self.root, key)

    def search_helper(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search_helper(root.left, key)
        return self.search_helper(root.right, key)

    def insert(self, key):
        self.root = self.insert_helper(self.root, key)

    def insert_helper(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_helper(root.left, key)
        elif key > root.key:
            root.right = self.insert_helper(root.right, key)
        return root

    def delete(self, key):
        self.root = self.delete_helper(self.root, key)

    def delete_helper(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete_helper(root.left, key)
        elif key > root.key:
            root.right = self.delete_helper(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self.min_value(root.right).key
            root.right = self.delete_helper(root.right, root.key)
        return root

    # function to help us find the min (left most in bst)
    def min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

def inorder_pas(root):
    if root:
        inorder_pas(root.left)
        print(root.key, end=" ")
        inorder_pas(root.right)


if __name__ == '__main__':

    bstTemp = BinarySearchTree()
    arr = [50, 30, 20, 40, 70, 60, 80]

    # we build the tree
    for val in arr:
        bstTemp.insert(val)

    print("Binary Search Tree after insertion:")

    inorder_pas(bstTemp.root)
    print()

    # search
    search_key = 40
    result = bstTemp.search(search_key)
    if result:
        print(f"value {search_key} found in the tree.")
    else:
        print(f"value {search_key} not found in the tree.")

    # delete
    delete_val = 30
    bstTemp.delete(delete_val)
    print(f"Binary Search Tree after deleting key {delete_val}:")
    inorder_pas(bstTemp.root)
