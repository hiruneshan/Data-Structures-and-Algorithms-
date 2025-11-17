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

