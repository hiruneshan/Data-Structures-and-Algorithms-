class BST:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

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
