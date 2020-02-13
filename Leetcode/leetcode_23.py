from Leetcode.nodes import ListNode

class LoserTree:
    max_num = 99999999

    def __init__(self, nodes):
        nodes = [n for n in nodes if n is not None]

        self.winner_ind = -1
        # 用-1先填充内部结点，等待初始化
        # 完全二叉树，内部节点 = 外部节点少 - 1
        self.inner_nodes = [-1 for _ in range(len(nodes) - 1)]
        self.num_inner = len(self.inner_nodes)
        self.leaves = nodes + [ListNode(-self.max_num)] # 末尾设置最小值，用于初始化，因为内部节点初始化的下标是leaves的末尾

        for i in range(len(nodes) - 1):
            self.adjust(i)

        # 经过一轮调整，胜者一定是预设的最小值，这时只需要将其替换成一个极大值再调整一次即可决出真正的优胜者
        self.leaves[-1] = ListNode(self.max_num)
        self.adjust(len(nodes) - 1)

    def adjust(self, i):
        '''
        调整函数，不断与父节点比较，败者留在该父节点，胜者进入下一轮。
        :param i: 外部节点下标
        :return:
        '''

        # 计算出该外部节点对应的父节点下标
        point_parent = (self.num_inner + i - 1) // 2 # 加上内部节点数作为偏移量
        while point_parent >= 0: # 循环直到root节点为止
            # 如果输了父节点，作为败者留在该父节点，即与父节点的下标做swap再进入下一轮
            # 注意：leaves里存的是待比较的值，而inner_nodes存的是leaves的下标（败者的下标
            if self.leaves[i].val > self.leaves[self.inner_nodes[point_parent]].val: # 如果比父节点大，即输了
                temp = self.inner_nodes[point_parent]
                self.inner_nodes[point_parent] = i
                i = temp

            # 如果赢了父节点，什么都不做，直接与下一个父节点做比较
            point_parent = (point_parent - 1) // 2

        self.winner_ind = i

        return i


class Solution:
    def mergeKLists(self, lists):
        lt = LoserTree(lists)
        head = ListNode(-1)
        point_win = head

        while True:
            winner_ind = lt.winner_ind
            winner = lt.leaves[winner_ind]
            if winner.val == lt.max_num: # 如果胜者到了极大值，说明已经排序完毕
                break
            else:
                point_win.next = winner
                point_win = point_win.next

            # 移动对应链表的指针，重新调整败者树
            lt.leaves[winner_ind] = lt.leaves[winner_ind].next
            if lt.leaves[winner_ind] is None:
                lt.leaves[winner_ind] = ListNode(lt.max_num)
            lt.adjust(winner_ind)

        return head.next


if __name__ == "__main__":
    lists = [
        [1],
    ]
    node_lists = []
    for l in lists:
        head = ListNode(-1)
        point = head
        for node in l:
            point.next = ListNode(node)
            point = point.next
        node_lists.append(head.next)

    # nums = [ListNode(2), ListNode(4), ListNode(6)]
    sol = Solution()
    print(sol.mergeKLists(node_lists))
