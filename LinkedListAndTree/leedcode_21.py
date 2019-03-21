'''
合并两个有序链表
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

结果：
通过
'''


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


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        point_l1 = l1
        point_l2 = l2

        res = []
        while point_l1 is not None and point_l2 is not None:
            if point_l1.val < point_l2.val:
                res.append(point_l1)
                point_l1 = point_l1.next
            else:
                res.append(point_l2)
                point_l2 = point_l2.next

        if point_l1 is None and point_l2 is not None:
            res.append(point_l2)
        if point_l2 is None and point_l1 is not None:
            res.append(point_l1)

        for ind in range(len(res)):
            if ind != len(res) - 1:
                res[ind].next = res[ind + 1]

        ll_merged = res[0] if len(res) > 0 else None
        return ll_merged


if __name__ == "__main__":
    sol = Solution()
    n11, n12, n13 = ListNode(1), ListNode(2), ListNode(4)
    n21, n22, n23 = ListNode(1), ListNode(3), ListNode(4)
    n11.next = n12
    n12.next = n13
    n21.next = n22
    n22.next = n23

    print(sol.mergeTwoLists(n11, n21))