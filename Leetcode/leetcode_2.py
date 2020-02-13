'''
两数相加

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

思路：大整数相加
结果：136ms 通过
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        point1 = l1
        point2 = l2

        pre_head = ListNode(None)
        res_point = pre_head
        c = 0
        while point1 is not None or point2 is not None:
            add1 = 0
            add2 = 0
            if point1 is not None:
                add1 = point1.val
                point1 = point1.next
            if point2 is not None:
                add2 = point2.val
                point2 = point2.next

            sum = add1 + add2 + c
            c = sum // 10
            bit = sum % 10
            res_point.next = ListNode(bit)
            res_point = res_point.next

        if c != 0:
            res_point.next = ListNode(c)

        return pre_head.next


if __name__ == "__main__":
    sol = Solution()
    n11, n12, n13 = ListNode(1), ListNode(2), ListNode(4)
    n21, n22, n23 = ListNode(1), ListNode(3), ListNode(4)
    n11.next = n12
    n12.next = n13
    n21.next = n22
    n22.next = n23

    print(sol.addTwoNumbers(n11, n21))
