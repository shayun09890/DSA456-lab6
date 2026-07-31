class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:

    def __init__ (self):
        self.root = None

    def is_empty(self):

        return self.root is None

    def insert(self, data):

        if self.root is None:
            self.root = Node(data)
            return

        current = self.root

        while True:

            if data < current.data:

                if current.left is None:
                    current.left = Node(data)
                    return

                current = current.left
            elif data > current.data:

                if current.right is None:
                    current.right = Node(data)
                    return
                current = current.right
            else: return

    def is_present(self, data):

        current = self.root

        while current is not None:

            if current.data == data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
                
        return False

            
