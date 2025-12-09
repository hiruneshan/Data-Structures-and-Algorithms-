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


"""
Given a non-empty Binary Search Tree (BST) of unique integer values and a target value (which may not exist in the tree), implement an iterative method to find both:

The floor of the target: the greatest value in the BST that is ≤ the target.

The ceil of the target: the least value in the BST that is ≥ the target.

If there is no valid floor (all values are greater than the target), return None for the floor.
If there is no valid ceil (all values are less than the target), return None for the ceil.

Your solution must run in O(log n) time on a balanced BST by following a single path from the root to a leaf, leveraging the BST property (left < root < right). You must not traverse the entire tree.

Example Tree (preserve whitespace):

        15
       /  \
      10   20
     /  \   \
    8   12  25
          \
          19

"""


def find_floor_ceil(self, target):
    if self.root is None:
        return 0

    curr = self.root
    floor = None
    ceiling = None

    while curr:

        if curr.data == target:
            return curr.data, curr.data
        # floor
        elif curr.data <= target:
            floor = curr.data
            curr = curr.right

        else:
            ceiling = curr.data
            curr = curr.left
    return floor, ceiling


#augmented BST
# lass BST:
#     class Node:
#         def __init__(self, value, size=1):
#             self.value = value
#             self.size = size
#             self.left = None
#             self.right = None
#
#     def __init__(self):
#         self.root = None

    def find_rank(self, target):
        """
        Returns the count of nodes with values <= target.
        Iterative, O(log n) on average for balanced BST.
        """
        rank = 0
        current = self.root

        while current:
            if current.value > target:
                # Go left, because current and right subtree are too large
                current = current.left
            else:
                # current.value <= target:
                # Add left subtree size (if exists) + 1 (current)
                left_size = current.left.size if current.left else 0
                rank += left_size + 1
                # Move right to find more <= target
                current = current.right

        return rank

