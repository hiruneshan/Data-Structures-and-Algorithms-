def func(self, target):
    if self.root is None:
        return 0

    curr = self.root
    self.value = 0
    while curr:
        if curr.data > target:
            self.value = curr.data
            curr = curr.left

        else:
            curr = curr.right
    return self.value

"""
Given a non-empty Binary Search Tree (BST) and a target value (which may or may not exist in the tree), implement an iterative function find_floor(target) that returns the floor of the target.
The floor of a target is defined as the greatest value in the BST that is less than or equal to the target. If no such value exists in the tree, return None.

You must leverage the BST property (left subtree values < node value < right subtree values) and achieve O(log n) time complexity by traversing down a single path.

Example Tree (shown here preserving whitespace):

       20
      /  \
     10   30
       \    \
       15    40
"""
def find_floor(self, target):
    if self.root is None:
        return 0

    curr = self.root
    self.value = 0
    while curr:
        if curr.data < target:
            self.value = curr.data
            curr = curr.right

        else:
            curr = curr.left
    return self.value

"""
Given a binary search tree (BST) and two integer values val1 and val2, implement an iterative method node_distance(self, val1, val2) that returns the number of edges in the path connecting the two nodes with those values. If either value is not present in the BST, return -1. Your solution must use loops (no recursion) and leverage the BST property (left subtree values < node value < right subtree values) to achieve O(log n) time by traversing down a single path for each search.

Example Tree:

         15
        /  \
       6    23
      / \   / \
     4   7 17 30
    /       \
   2         19
"""


def node_distance(self, val1, val2):

    if self.root is None:
        return 0

    node = None

    self.count = 0

    curr = self.root
    while curr:

        if val1 < curr.data and val2 < curr.data:
            curr = curr.left

        elif val1 > curr.data and val2 > curr.data:
            curr = curr.right

        else:
            node = curr
            break

    distance_1 = dist_from_node(node, val1)
    distance_2 = dist_from_node(node, val2)

    return distance_1 + distance_2


    #from node to go to both the nodes

def dist_from_node(self, node, target):
    if node is None:
        return None

    distance = 0
    curr = node

    while curr:
        if target == curr.data:
            return distance

        if target < curr.data:
            curr = curr.left

        else:
            curr = curr.right

        distance += 1
    return -1





