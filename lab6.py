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
    
    def get_values(self, order):

        result = []

        if order == "PRE":
            self._pre_order(self.root, result)

        elif order == "IN":
            self._in_order(self.root, result)

        elif order == "POST":
            self._post_order(self.root, result)
        
        elif order == "TOP":

            if self.root is None:
                return result
            
            queue = [self.root]
        while len(queue) > 0:

            current = queue.pop(0)
            result.append(current.data)

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:

        return result  

    def _pre_order(self, node, result):

        if node is None:
            return
        
        result.append(node.data)

        self._pre_order(node.left, result)
        self._pre_order(node.right, result)

    def _in_order(self, node, result):

        if node is None:
            return
        
        self._in_order(node.left, result)
        result.append(node.data)
        self._in_order(node.right, result)
    
    def _post_order(self, node, result):

        if node is None:
            return
        
        self._in_order(node.left, result)
        self._post_order(node.right, result)

        result.append(node.data)

    def print(self):

        result = []

        self._in_order(self.root, result)

        for value in result:
            print(value)

    def _remove(self, node, data):

        if node is None:
            return None
        
        if data < node.data:
            node.left = self._remove(node.left, data)

        elif data > node.data:
            node.left = self._remove(node.right, data)
        
        else:
            
            if node.left is None and node.right is None:
                return
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            else:
                
                successor = node.right

                while successor.left is not None:
                    successor = successor.left 
                
                node.data = successor.data

                node.right = self._remove(node.right, successor.data)
            
        return node
    
    def height(self):
        return self._height(self.root)
    
    def height(self, node):

        if node is None:
            return 0
        
        left_height = self._height(node.left)
        right_height = self._height(node.right)

        return max(left_height, right_height) + 1
        
