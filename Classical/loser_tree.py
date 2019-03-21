'''
败者树
线性表实现
'''


class LoserTree:
    def __init__(self, nums):
        self.winner_ind = -1
        self.leaves = nums[:]
        # 用-1先填充内部结点，等待初始化
        # 完全二叉树，内部节点 = 外部节点少 - 1
        self.inner_nodes = [-1 for _ in range(len(nums) - 1)]
        self.num_inner = len(self.inner_nodes)
        self.leaves += [0] # 末尾设置最小值，用于初始化，因为内部节点初始化的下标是leaves的末尾

        for i in range(len(nums) - 1):
            self.adjust(i)

        # 经过一轮调整，胜者一定是预设的最小值，这时只需要将其替换成一个极大值再调整一次即可决出真正的优胜者
        self.leaves[-1] = 99999999
        self.adjust(len(nums) - 1)

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
            if self.leaves[i] > self.leaves[self.inner_nodes[point_parent]]: # 如果比父节点大，即输了
                temp = self.inner_nodes[point_parent]
                self.inner_nodes[point_parent] = i
                i = temp

            # 如果赢了父节点，什么都不做，直接与下一个父节点做比较
            point_parent = (point_parent - 1) // 2

        self.winner_ind = i

        return i

    def get_leaf(self, i):
        return self.leaves[i]


if __name__ == "__main__":
    nums = [2, 1, 1]
    lt = LoserTree(nums)
    print(lt.get_leaf(lt.winner_ind))
