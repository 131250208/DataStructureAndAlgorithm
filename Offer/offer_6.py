class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return []
        que = []
        que.append(listNode.val)

        point = listNode.next
        while point is not None:
            que.append(point.val)
            point = point.next

        res = []
        while len(que) != 0:
            res.append(que.pop())

        return res
            