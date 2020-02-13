'''
用dict + double linked list
dict用来缓存value
dll用来充当一个可以o（1）时间删除任意结点的队列，用以计算最近最少使用的node
'''

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.dict: # 如果key不存在dict中，返回-1
            return -1
        # 如果可以存在，更新使用队列并返回值
        n = self.dict[key]
        self._update(n)
        return n.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:# 已经存在的key
            self.dict[key].val = value
            self._update(self.dict[key])# 更新一下使用队列
            return

        # 如果是新的key
        self.dict[key] = Node(key, value)
        self._add_2_tail(self.dict[key])# 添加到使用队列的末尾

        if len(self.dict) > self.capacity:# 如果大于最大容量，弹出使用队列队顶结点并从dict中删除
            n = self._pop_left()
            del self.dict[n.key]

    def _pop_left(self):
        '''
        弹出队顶结点
        :return: 队顶的node
        '''
        n = self.head.next
        self.head.next = n.next
        n.next.pre = self.head
        return n

    def _add_2_tail(self, n):
        '''
        将node添加到队尾
        :param n: node
        :return: none
        '''
        self.tail.pre.next = n
        n.pre = self.tail.pre
        n.next = self.tail
        self.tail.pre = n

    def _remove(self, n):
        '''
        从队列中删除当前node
        :param n: node
        :return: none
        '''
        n.pre.next = n.next
        n.next.pre = n.pre

    def _update(self, n):
        '''
        更新当前node在队列中的位置
        :param n: node
        :return: none
        '''
        self._remove(n)
        self._add_2_tail(n)

if __name__ == "__main__":
    cache = None
    instruction_list = ["LRUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
    parameters_list = [[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]

    for ind, ins in enumerate(instruction_list):
        if ins == "LRUCache":
            cache = LRUCache(parameters_list[ind][0])
        if ins == "put":
            cache.put(parameters_list[ind][0], parameters_list[ind][1])
        if ins == "get":
            print(cache.get(parameters_list[ind][0]))
