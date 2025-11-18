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










