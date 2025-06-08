
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.parent = self

    def add_item(self, x):
        if x >= self.val:
            if self.right == None:
                node = BSTNode(x)
                self.right = node
                node.parent = self
            else:
                self.add_item(self.right, x)
        else:
            if self.left == None:
                node = BSTNode(x)
                self.left = node
                node.parent = self
            else:
                self.add_item(self.left, x)

    def find_item(self, x):
        if x > self.val:
            if self.right == None:
                raise Exception("Item does not exist")
            else:
                return self.find_item(self.right, x)

        elif x < self.val:
            if self.left == None:
                raise Exception("Item does not exist")
            else:
                return self.find_item(self.left, x)
        else:
            return self