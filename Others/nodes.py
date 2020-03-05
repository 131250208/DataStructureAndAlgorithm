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

import Queue
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        output = []
        queue = Queue.deque()
        queue.append(self)

        while len(queue):
            node = queue.pop()
            if not node:
                output.append("#")
                continue
            output.append(node.val)
            queue.appendleft(node.left)
            queue.appendleft(node.right)
        return str(output)

def buildATree(numList):
    nodeList = []
    for n in numList:
        if n != "#":
            nodeList.append(TreeNode(n))
        else:
            nodeList.append(None)

    for i, node in enumerate(nodeList):
        node.left = nodeList[2*i + 1] if 2*i + 1 < len(nodeList) else None
        node.right = nodeList[2*i + 2] if 2*i + 2 < len(nodeList) else None
    return nodeList[0]

if __name__ == "__main__":
    numList = [10, 5, 12, 4, 7]
    tr = buildATree(numList)
    print tr