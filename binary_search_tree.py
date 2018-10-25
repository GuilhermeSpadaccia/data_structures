"""
Implementation of a Binary Search Tree 

Author: Guilherme Spadaccia
"""

class btree_node():
    """
    Class: btree_node

    Each instance of this class may have as son two other btree_node objects
    one on left attribute and other on right onde. This son node must be add
    using the add_node method.
    """
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    """
    Method: add_node

    Add a new node following the BST rules
    """
    def add_node(self, node):
        if node.key < self.key:
            if self.left == None:
                self.left = node
            else:
                self.left.add_node(node)
        else:
            if self.right == None:
                self.right = node
            else:
                self.right.add_node(node)
    
    """
    Method: search_by_key

    Find a key on the binary tree and returns its value.
    """
    def search_by_key(self, key):
        print("Visited node: ", self.key)

        if self.key == key:
            return(self.value)
        else:
            if key < self.key:
                value = self.left.search_by_key(key)
            else:
                value = self.right.search_by_key(key)

            return(value)

    """
    Method: get_min

    Returns the lowest value on the tree. 
    """
    def get_min(self):
        if self.left != None:
            return(self.left.get_min())
        else:
            return(self.key)
    
    """
    Method: get_max

    Returns the highest value on the tree. 
    """
    def get_max(self):
        if self.right != None:
            return(self.right.get_max())
        else:
            return(self.key)


root = btree_node(8, value='root')
node1 = btree_node(3, value='node1')
node2 = btree_node(1, value='node2')
node3 = btree_node(6, value='node3')
node4 = btree_node(4, value='node4')
node5 = btree_node(1, value='node5')
node6 = btree_node(10, value='node6')
node7 = btree_node(14, value='node7')
node8 = btree_node(13, value='node8')
node9 = btree_node(12, value='node9')

root.add_node(node1)
root.add_node(node2)
root.add_node(node3)
root.add_node(node4)
root.add_node(node5)
root.add_node(node6)
root.add_node(node7)
root.add_node(node8)
root.add_node(node9)

print("Found node: ", root.search_by_key(1)) # Must print 'root'
print("Found node: ", root.search_by_key(4)) # Must print 'node3'
print("Found node: ", root.search_by_key(14)) # Must print 'node7'

print("Min value: ", root.get_min()) # Must print '10'
print("Max value: ", root.get_max()) # Must print '125'