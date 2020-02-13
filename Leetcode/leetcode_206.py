'''
反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

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
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        point = head
        stack = []
        while point is not None:
            stack.append(point)
            point = point.next

        start = stack.pop()
        point = start
        while len(stack) != 0:
            next_node = stack.pop()
            point.next = next_node
            point = point.next

        point.next = None
        return start


if __name__ == "__main__":
    n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    sol = Solution()
    print(sol.reverseList(n1))
