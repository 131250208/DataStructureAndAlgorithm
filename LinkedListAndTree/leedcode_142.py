'''
环形链表 II

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
说明：不允许修改给定的链表。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。

进阶：
你是否可以不用额外空间解决此题？

思路：
1. fast-slow 指针确定是否有环
2. 如果有环，确定入口：
    设从起点到入口路程是a，从入口到相遇点是b
    1. fast比slow多走了一个环
    2. fast走的路程是slow的两倍
    3. 由1,2得: 环的长度 = a + b = slow走过的路程
    4. slow目前与入口的距离是b
    5. 由3,4得slow再走a步回到入口
    6. 因为起点到入口的距离也是a，所以令一个新指针从起点开始走，与slow会在入口相遇。
'''

from LinkedListAndTree.nodes import ListNode

class Solution(object):
    def detectCycle(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow_point = head
        fast_point = head

        loop = False
        a_b = 1
        while fast_point and fast_point.next:
            a_b += 1
            fast_point = fast_point.next.next
            slow_point = slow_point.next

            if fast_point == slow_point: # 相遇，存在环
                loop = True
                break

        if loop is False:
            return None

        # 用新指针找入口
        new_point = head
        while slow_point != new_point:
            slow_point = slow_point.next
            new_point = new_point.next

        new_point.next = None
        return new_point


if __name__ == "__main__":
    n1, n2 = ListNode(1), ListNode(2)
    n1.next = n2
    n2.next = n1

    sol = Solution()
    print(sol.detectCycle(n1))
