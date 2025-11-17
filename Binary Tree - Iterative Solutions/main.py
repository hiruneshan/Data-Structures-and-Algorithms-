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







