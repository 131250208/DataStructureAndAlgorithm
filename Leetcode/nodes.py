class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        ll = [str(self.val), ]
        point = self.next
        while point is not None:
            ll.append(str(point.val))
            point = point.next
        return "->".join(ll)


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        output = ""
        queue = [self]
        current = 0
        while current != len(queue):
            node = queue[current]
            current = current + 1

            if not node:
                output += "null, "
                continue

            output += str(node.val) + ", "
            queue.append(node.left)
            queue.append(node.right)
        return "[" + output[:-2] + "]"
