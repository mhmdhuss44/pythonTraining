# first we create a simple class for our tree
class tempTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_lca(root, node1, node2):
    if root is None:
        return None
    # of one of them is our node then we return it
    if root.value == node1 or root.value == node2:
        return root

    # Recursive calls for each subtree
    left_lca = find_lca(root.left, node1, node2)
    right_lca = find_lca(root.right, node1, node2)

    # If both we get that botj are not null , then we have the currect node
    if left_lca is not None and right_lca is not None:
        return root

    # else we return the subtree of the not none node
    if left_lca is not None:
        return left_lca
    else :
        return right_lca



if __name__ == '__main__':
    # building a tree
    root = tempTree(3)
    root.left = tempTree(5)
    root.right = tempTree(1)
    root.left.left = tempTree(6)
    root.left.right = tempTree(2)
    root.right.left = tempTree(0)
    root.right.right = tempTree(8)
    root.left.right.left = tempTree(7)
    root.left.right.right = tempTree(4)

    result = find_lca(root, 5, 1)
    print("LCA of 5 and 1 is:", result.value)
