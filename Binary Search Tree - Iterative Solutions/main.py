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



