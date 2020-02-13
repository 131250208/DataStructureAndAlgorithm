'''
160. 相交链表
编写一个程序，找到两个单链表相交的起始节点。

思路：
设两个链表在相交前的长度分别为a_pre, b_pre, 相交后的长度为common
有：a_pre + common + b_pre = b_pre + common + a_pre
1. 可令两个指针沿以上等号两边的两条路径走，因为路径长度相同，指针相遇点即为相交点
2. 简单来看，就是让两个指针走完两个链表，只不过一个从链表a的头部出发，走完a再走b，另一个同理，但从b的头部出发。
3. 如果两个指针走完都没有相遇，则返回null
'''

from Leetcode.nodes import ListNode

class Solution(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        life_a, life_b = 1, 1 # 两个玩家各有一条命，遇到链尾命-1，可以在另一条链头重新开始，其中一个没有命了，即代表走完两条链，循环结束。
        point_a, point_b = headA, headB

        while True:
            if point_a is None:
                if life_a:
                    point_a = headB
                    life_a -= 1
                else:
                    break
            if point_b is None:
                if life_b:
                    point_b = headA
                    life_b -= 1
                else:
                    break

            if point_a == point_b:
                return point_a

            point_a = point_a.next
            point_b = point_b.next

        return None

if __name__ == "__main__":
    l1 = [ListNode(num) for num in [2, 6, 4]]
    l2 = [ListNode(num) for num in [1, 5]]
    # common = [ListNode(num) for num in [2, 4]]

    for ind in range(len(l1) - 1):
        l1[ind].next = l1[ind + 1]
    for ind in range(len(l2) - 1):
        l2[ind].next = l2[ind + 1]
    # for ind in range(len(common) - 1):
    #     common[ind].next = common[ind + 1]

    # l1[-1].next = common[0]
    # l2[-1].next = common[0]

    sol = Solution()
    print(sol.getIntersectionNode(l1[0], l2[0]))
