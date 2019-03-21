'''
排序链表
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4

示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5

思路：
1. fast-slow 指针找中点
2. 从中点断开链表，对两个链表递归地调用sortList
3. 调用merge归并两个已排序链表
'''

from LinkedListAndTree.nodes import ListNode

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        fast_point = head
        slow_point = head
        break_point = head
        while fast_point and fast_point.next:
            fast_point = fast_point.next.next
            break_point = slow_point # 记录slow的前一位，将作为断开点
            slow_point = slow_point.next

        break_point.next = None # 断开链表
        list1 = self.sortList(head)
        list2 = self.sortList(slow_point)
        return self.merge(list1, list2)

    def merge(self, list1, list2):
        pre_head = ListNode(None)
        point = pre_head
        list1_point = list1
        list2_point = list2
        while list1_point and list2_point:
            if list1_point.val < list2_point.val:
                point.next = list1_point
                list1_point = list1_point.next
            else:
                point.next = list2_point
                list2_point = list2_point.next
            point = point.next

        if list1_point is None:
            point.next = list2_point
        if list2_point is None:
            point.next = list1_point

        return pre_head.next


if __name__ == "__main__":
    n1, n2, n3, n4, n5 = ListNode(-1), ListNode(5), ListNode(3), ListNode(4), ListNode(0)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    sol = Solution()
    print(sol.sortList(n1))
