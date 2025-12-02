class BT:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def diameter(self) -> int:
        self.max_diameter = 0

        def height(node):
            if node is None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            current_diameter = left_height + right_height + 1

            if current_diameter > self.max_diameter:
                self.max_diameter = current_diameter
            return max(left_height, right_height) + 1

        height(self.root)
        return self.max_diameter

    def sum_single_child_nodes(self, node):

        if node is None:
            return 0

        my_sum = 0

        if node.left is not None and node.right is None:
            my_sum += node.value

        if node.left is None and node.right is not None:
            my_sum += node.value

        sum_from_left = self.sum_single_child_nodes(node.left)

        sum_from_right = self.sum_single_child_nodes(node.right)

        return my_sum + sum_from_left + sum_from_right

    # another way to calc the single node children
    def sum_single_child_nodes1(self, node):
        if node is None:
            return 0

        # Sum for left and right subtrees
        left_sum = self.sum_single_child_nodes1(node.left)
        right_sum = self.sum_single_child_nodes1(node.right)

        # Check if exactly one child exists
        has_one_child = (node.left is None) ^ (node.right is None)

        # Include current node's value if it has exactly one child
        return left_sum + right_sum + (node.value if has_one_child else 0)

        # if we are not using a value from the func call, we are using _, in order to ignore it

    def count_unival_subtrees(self):
        _, total_count = self.helper(self.root)
        return total_count

    def helper(self, node):
        if node is None:
            return True, 0

        left_uni, left_count = self.helper(node.left)
        right_uni, right_count = self.helper(node.right)

        is_uni = True

        if node.left and node.left.value != node.value:
            is_uni = False

        if not node.right and node.right.value != node.value:
            is_uni = False

        if not left_uni or not right_uni:
            is_uni = False

        total = left_count + right_count + (1 if is_uni else 0)
        return is_uni, total

    # def countSingleChildNodes(self, root): --> correct however next one is better
        #     if root is None:
        #         return 0

        #     my_count = 0

        #     if node.left is not None and node.right is None:
        #         my_count += 1

        #     if node.left is None and node.right is not None:
        #         my_count += 1

        #     left = self.countSingleChildNodes(node.left)
        #     right = self.countSingleChildNodes(node.right)

    #    return my_count + left + right

    def countSingleChildNodes(self, root):
        # Base case
        if root is None:
            return 0

        # Recurse on children
        left_count = self.countSingleChildNodes(root.left)
        right_count = self.countSingleChildNodes(root.right)

        has_left = root.left is not None
        has_right = root.right is not None
        current = 1 if (has_left ^ has_right) else 0  # XOR: true if exactly one is true

        return left_count + right_count + current

        # more coode less efficent
        # def get_sum(node):
        #     if node is None:
        #         return 0

        #     my_count = 0

        #     if node.value % 2 == 0:
        #         if node.left:
        #             if node.left.left:
        #                 my_count += node.left.left.value
        #             if node.left.right:
        #                 my_count += node.left.right.value

        #         if node.right:
        #             if node.right.left:
        #                 my_count += node.right.left.value
        #             if node.right.right:
        #                 my_count += node.right.right.value

        #     left = get_sum(node.left)
        #     right = get_sum(node.right)

        #     return left + right + my_count

        # less code and more efficient

    def sum_even_main_func(self):
        return self.sum_even_grandParent(self.root, None, None)

    def sum_even_grandParent(self, node, parent, grandparent):

        if node is None:
            return 0

        total = 0
        if grandparent and grandparent.value % 2 == 0:
            total += node.value

        left_sum = self.sum_even_grandParent(node.left, node, parent)
        right_sum = self.sum_even_grandParent(node.right, node, parent)

        return total + left_sum + right_sum

    #if the given nodes are nodes, if they were values we will not be using .value
    def lowestCommonAncestor(self, root, n1, n2):


        def rec_helper(subtree, n1, n2):

            if subtree is None:
                return None

            if n1.value < subtree.data and n2.value < subtree.data:
                return rec_helper(subtree.left, n1, n2)

            elif n1.value > subtree.data and n2.value > subtree.data:
                return rec_helper(subtree.right, n1, n2)

            else:
                return subtree.data

        return rec_helper(self.root, n1, n2)

    def _find_floor_recursive(self, node, target):

        def find_floor_helper(subtree, target, floor_tar):

            if subtree is None:
                return floor_tar

            if node.value > target:
                return find_floor_helper(subtree.left, target, floor_tar)

            elif node.value == target:
                return node.value

            else:
                return find_floor_helper(subtree.right, target, node.value)

        return find_floor_helper(self.root, target, self.root.value)




    def sum_single_child_nodes(self):
        self.sum_value = 0

        def helper(node):

            if node is None:
                return

            if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
                self.sum_value += node.data

            helper(node.left)
            helper(node.right)

        helper(self.root)
        return self.sum_val



    def count_unival_subtrees(self) -> int:
        self.count = 0

        def helper1(subtree):
            if subtree is None:
                return None

            if subtree.left and subtree.right:

                if subtree.left.value == subtree.right.value:
                    self.count += 1

            helper1(subtree.left)
            helper1(subtree.right)

        helper1(self.root)


"""
Given a binary tree, write a recursive function to compute the sum of all leaf-node values that occur at the minimum depth from the root.

The minimum depth is defined as the number of nodes along the shortest path from the root node down to the nearest leaf node.

A leaf node is a node with no children (both left and right pointers are None).

Example Tree (shown here preserving whitespace):

      1
     / \
    2   3
   /   / \
  4   5   6
         /
        7
"""
def sum_min_depth_leaves(self):
        if self.root is None:
            return None

        def helper(node):

            if node is None:
                return (float('inf'), 0)

            if node.left is None and node.right is None:
                return (1, node.value)

            left_depth, left_val = helper(node.left)
            right_depth, right_val = helper(node.right)

            if left_depth < right_depth:
                return (left_depth + 1, left_val)

            if right_depth < left_depth:
                return (right_depth + 1, right_val)

            else:
                return (left_depth + 1, right_val + left_val)

        minDepth, sumLevels = helper(self.root)
        return sumLevels

"""
Recursive Binary Tree Question
Problem Statement:
Given a binary tree, compute the sum of all node values that have an even-valued grandparent. A grandparent of a node is the parent of its parent. If there is no grandparent or the grandparent’s value is odd, that node does not contribute to the sum.

Example Tree (shown here preserving whitespace):

            6
          /   \
         7     8
        / \   / \
       2   7 1   3
      / \         \
     9   1         5


"""
def rec_method(self):
    if self.root is None:
        return 0

    self.total = 0

    def helper(node, parent, grandParent):
        if node is None:
            return

        if grandParent and grandParent.value % 2 == 0:
            self.total += grandParent.value

        helper(node.left, node, parent)
        helper(node.right, node, parent)

    helper(self.root, None, None)
    return self.total


"""
Given a binary tree of integers, write a recursive function to find the maximum sum of values along any path from the root down to a leaf. A leaf is a node with no children. Your function should return this maximum root-to-leaf path sum.

Example Tree (shown here preserving whitespace):

       5
      / \
     3   8
    / \   \
   1   4   10
"""


def max_root_to_leaf_sum(self, root):

    if root is None:
        return 0

    def helper(subtree):
        if subtree is None:
            return float('-inf')

        if subtree.left is None and subtree.right is None:
            return subtree.value

        left = helper(subtree.left)
        right = helper(subtree.right)

        return subtree.value + max(left, right)
    return helper(root)



def max_subtree_sum(self):
    if self.root is None:
        return 0

    self.max_subtree = '-inf'

    def helper(node):
        if node is None:
            return 0

        left = helper(node.left)
        right = helper(node.right)
        curr_max = node.value + left + right

        self.max_subtree = max(self.max_subtree, curr_max)

        return curr_max

    helper(self.root)
    return self.max_subtree


