"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert the given value into the tree
    def insert(self, value):
        # insert
        # left case
        # check if our value is less than root value
            if value < self.value:
            # move to the left and check if it is None
                if not self.left:
                # insert node here set the self.left to the new node
                    self.left = BSTNode(value)
            # otherwise
                else:
                # do an insert on the root's left node recursive call to the left node using self.left
                    self.left.insert(value)
        # right case
        # otherwise
            else:
            # move to the right and check if it is None
                if not self.right:
                # insert node here set the self.right to the new node
                    self.right = BSTNode(value)
            # otherwise
                else:
                # do an insert on the root's right node recursive call to insert using self.right
                    self.right.insert(value)
      

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # contains
        # check the value root node (self.value) against the target
        if self.value == target:
        # if the root node value and target are the same
            return True
        
        # left case
        # check if our target is less than the root val (self.value)
        if target < self.value:
            # check if there is no child to the left (self.left) is None
            if not self.left :
                return False
            # otherwise
            else:
                # call contains on the left child (self.left)
                return self.left.contains(target)
        
        # right case
        # otherwise
        else:
            # check if there is no child to the right (self.right) is None
            if not self.right:
                return False
            # otherwise
            else:
                # call contains on the right child (self.right)
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
    #check to see if the right value is none
        if not self.right:
    #if it is none return self.value as the max number
            return self.value
    #otherwise
        else:
    #call get_max on the right child
            return self.right.get_max()
        
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass