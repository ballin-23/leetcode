def minHeightBst(array):
    middle = len(array) // 2
    tree = BST(array[middle])
    left = array[:middle]
    right = array[middle+1:]
    if len(left) > 0:
        tree.left = minHeightBst(left)
    if len(right) > 0:
        tree.right = minHeightBst(right)
    return tree


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
