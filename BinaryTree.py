'''
BinaryTree structure is copied from https://github.com/heineman/python-algorithms
'''
class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, val):
        if val <= self.value:
            self.left = self.addToSubTree(self.left, val)
        elif val > self.value:
            self.right = self.addToSubTree(self.right, val)

    def addToSubTree(self, parent, val):
        if parent is None:
            return BinaryNode(val)
        parent.add(val)
        return parent

    def remove(self, val):
        if val < self.value:
            self.left = self.removeFromParent(self.left, val)
        elif val > self.value:
            self.right = self.removeFromParent(self.right, val)
        else:
            # If I have no left subtree...
            if self.left is None:
                return self.right 
            # find largest value in left subtree
            child = self.left
            while child.right:
                child = child.right
            # This is the largest value
            childKey = child.value
            # We remove the largest value from left sub tree
            self.left = self.removeFromParent(self.left, childKey)
            # replace value of deleted node with largest value
            self.value = childKey
        # return the subtree after it's been removed
        return self

    def removeFromParent(self, parent, val):
        if parent:
            return parent.remove(val)
        return None

    def inorder(self):
        if self.left:
            for v in self.left.inorder():
                yield v

        yield self.value

        if self.right:
            for v in self.right.inorder():
                yield v

    def isLeaf(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False

    def __repr__(self):
        """Useful debugging function to produce linear tree representation."""
        leftS = ''
        rightS = ''
        if self.left:
            leftS = str(self.left)
            if self.right:
                rightS = str(self.right)
        return "(L:" + leftS + " " + str(self.value) + " R:" + rightS + ")"

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root == None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    def remove(self, value):
        if self.root is not None:
            self.root = self.root.remove(value)

    def getMin(self):
        if self.root is None:
            raise ValueError('Binary Tree is Empty')
        n = self.root
        while n.left:
            n = n.left
        return n.value

    def getMax(self):
        if self.root is None:
            raise ValueError('Binary Tree is Empty')
        n = self.root
        while n.left:
            n = n.left
        return n.value

    def __contains__(self, target):
        node = self.root
        while node is not None:
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return True
        return False

    def __iter__(self):
        if self.root:
            for v in self.root.inorder():
                yield v

    def __repr__(self):
        if self.root is None:
            return "binary:()"
        return "binary:" + str(self.root)
