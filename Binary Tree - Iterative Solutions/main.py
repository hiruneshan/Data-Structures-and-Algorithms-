import queue


class BT:
    class Node:
        def __init__(self, value):
            self.val = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def count_greater_than_ancestors(self):
        queue = queue.Queue()

        count = 0

        if self.root is None:
            return count

        queue.put((self.root, float('-inf')))

        while not queue.empty():

            node, max_path_val = queue.get()

            if node.value > max_path_val:
                max_path_val = node.value
                count = count + 1

            if node.left:
                queue.put((node.left, max_path_val))

            if node.right:
                queue.put((node.right, max_path_val))

        return count

    def max_sum_level(self):

        """
        TODO: Implement this method iteratively.
        It should return the level number (1-indexed) that has the maximum sum of node values.
        """
        my_queue = queue.Queue()

        if self.root is None:
            return 0

        my_queue.put((self.root))
        max_overall = float('-inf')
        best_level = 0
        current_level = 0

        while not my_queue.empty():
            current_level += 1

            level_size = my_queue.qsize()
            current_level_sum = 0
            node = my_queue.get()

            for _ in range(level_size):
                current_level_sum += node.val
                if node.left:
                    my_queue.put(node.left)

                if node.right:
                    my_queue.put(node.right)

            if current_level_sum > max_overall:
                max_overall_sum = current_level_sum
                best_level = current_level

        return best_level

    def sum_single_child_nodes(self):

        queue_1 = queue.Queue()
        count = 0

        if self.root is None:
            return count

        queue_1.put(self.root)

        while not queue_1.empty():
            node = queue_1.get()

            if (node.left is not None and node.right is None):
                count += node.left.value

            if (node.left is None and node.right is not None):
                count += node.right.value

            if node.left:
                queue_1.put(node.left)

            if node.right:
                queue_1.put(node.right)

        return count


def count_path_with_sum(self, target: int) -> int:
    if self.root is None:
        return None

    stack = [(self.root, target)]
    count = 0

    while stack:
        curr, rem = stack.pop()

        if curr.left is None and curr.right is None:
            if curr.data == rem:
                count += 1

        new_rem = rem - curr.data

        if curr.left:
            stack.append((curr.left, new_rem))
        if curr.right:
            stack.append((curr.right, new_rem))

    return count


def count_path_with_sum2(self, target: int) -> int:
    if self.root is None:
        return None

    stack = [(self.root, target)]
    count = 0

    while stack:
        curr, rem = stack.pop()

        new_rem = rem - curr.data

        if curr.left is None and curr.right is None:
            if new_rem == 0:
                count += 1

        if curr.left:
            stack.append((curr.left, new_rem))

        if curr.right:
            stack.append((curr.right, new_rem))

    return count


def sum_root_to_leaf_numbers(self):
    if self.root is None:
        return None

    stack = [(self.root, 0)]
    total_sum = 0

    while stack:
        Node, num = stack.pop()

        # checking if the node is a leaf
        num = num * 10 + Node.data

        if Node.left is None and Node.right is None:
            total_sum += num

        if Node.left:
            stack.append((Node.left, num))

        if Node.right:
            stack.append((Node.right, num))

    return total_sum

    # only difference is the way carry forward num is calculated


def sum_root_to_leaf_numbers2(self):
    if not self.root:
        return 0

    total_sum = 0
    stack = [(self.root, self.root.value)]

    while stack:
        node, current_num = stack.pop()

        # If it's a leaf, add the formed number
        if not node.left and not node.right:
            total_sum += current_num

        # Push right child first so left is processed next (optional order)
        if node.right:
            new_num = current_num * 10 + node.right.value
            stack.append((node.right, new_num))
        if node.left:
            new_num = current_num * 10 + node.left.value
            stack.append((node.left, new_num))

    return total_sum

"""
Given a binary tree, implement an iterative method sum_at_level(k) that returns the sum of all node values at the kth level of the tree. The root is considered to be at level 1. You may assume that the tree and integer k are provided, and that k is a positive integer. Your solution must use loops (e.g., while or for) and must not use recursion.

Example Tree (shown here preserving whitespace):

       5
      / \
     3   8
    / \   \
   1   4   9
      /
     2

"""


def sum_at_level(self, k):

    if self.root is None:
        return 0

    stack = [self.root]
    self.sum = 0
    level_num = 1

    while stack:
        level_len = len(stack)
        for _ in range(level_len):
            node = stack.pop(0)

            if level_num == k:
                self.sum += node.data

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        if level_num == k:
            return self.sum

        level_num += 1

    return 0 #or -1


"""
Given a binary tree where each node contains an integer value, write an iterative method max_ancestor_diff() that computes the maximum absolute difference between the value of any node and the value of any of its ancestors. An ancestor of a node is any node in the path from the root to that node (excluding the node itself).

Example Tree (shown here preserving whitespace):

         8
        / \
       3   10
      / \    \
     1   6    14
        / \   /
       4   7 13
"""


def max_ancestor_diff(self):
    if self.root is None:
        return 0

    self.max_difference = 0
    # sending node, min and max
    stack = [(self.root, self.root.value, self.root.value)]

    while stack:
        node, curr_min, curr_max = stack.pop()

        self.max_difference = max(self.max_difference,
                                  abs(curr_min - node.value),
                                  abs(curr_max - node.value))

        new_min = min(curr_min, node.value)
        new_max = max(curr_max, node.value)

        if node.left:
            stack.append((node.left, new_min, new_max))

        if node.right:
            stack.append((node.right, new_min, new_max))

    return self.max_differnce




