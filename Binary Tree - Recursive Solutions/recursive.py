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










