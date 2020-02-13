'''
1. 一个dict + 一个bucket list
2. dict维护key2node, node里维护value
3. bucket list维护count2bucket，bucket里装所有相同count的结点
4. 为了实现O（1）时间删除结点和添加结点到bucket，bucket用双向链表实现
'''


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = Node
        self.next = Node

    def add1(self):
        self.val += 1

    def dec1(self):
        self.val -= 1

    def get_val(self):
        return self.val

    def get_key(self):
        return self.key


class Bucket:
    def __init__(self):
        self.pre = None
        self.next = None

        self.head = Node("head", -1)
        self.tail = Node("tail", -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.__size = 0

    def add2tail(self, n):
        self.tail.pre.next = n
        n.next = self.tail
        n.pre = self.tail.pre
        self.tail.pre = n
        self.__size += 1

    def remove(self, n):
        n.pre.next = n.next
        n.next.pre = n.pre
        self.__size -= 1

    def check(self):
        if self.__size == 0: # 如果bucket为空，从bucket list中删除该bucket
            self.pre.next = self.next
            self.next.pre = self.pre
            return True
        return False

    def get_1st(self):
        return self.head.next

    def get_size(self):
        return self.__size


class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Bucket()
        self.tail = Bucket()
        self.head.next = self.tail
        self.tail.pre = self.head

        self.count2bucket = {0: self.head}
        self.key2node = {}

    def _add2tail(self, n):
        if n.get_val() not in self.count2bucket:  # 检查bucket_list是否存在对应的bucket，不存在则创建并添加到count2bucket
            bucket = Bucket()
            if n.get_val() - 1 in self.count2bucket:# 如果是+1过来的，把新bucket加载前一个bucket后面
                pre_bucket = self.count2bucket[n.get_val() - 1]
                pre_bucket.next.pre = bucket
                bucket.pre = pre_bucket
                bucket.next = pre_bucket.next
                pre_bucket.next = bucket
            elif n.get_val() + 1 in self.count2bucket: # 如果是-1过来的，加在后一个bucket的前面
                next_bucket = self.count2bucket[n.get_val() + 1]
                next_bucket.pre.next = bucket
                bucket.pre = next_bucket.pre
                bucket.next = next_bucket
                next_bucket.pre = bucket
            self.count2bucket[n.get_val()] = bucket
        self.count2bucket[n.get_val()].add2tail(n)

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.key2node:# 如果key存在，从原来的bucket中删除对应结点，将结点加到下一个bucket中
            n = self.key2node[key]
            key_bucket = n.get_val()
            bucket = self.count2bucket[key_bucket]
            bucket.remove(n)
            n.add1()
            self._add2tail(n)
            if bucket.check():
                del self.count2bucket[key_bucket]

        else:# 如果key不存在，则直接创建并添加到对应bucket中
            n = Node(key, 1)
            self.key2node[key] = n
            self._add2tail(n)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.key2node:# 如果key存在，从原来的bucket中删除对应结点，将结点加到上一个bucket中
            n = self.key2node[key]
            key_bucket = n.get_val()
            bucket = self.count2bucket[key_bucket]
            bucket.remove(n)
            n.dec1()
            if n.get_val() == 0:
                del self.key2node[key]
            else:
                self._add2tail(n)
            if bucket.check():# 检查bucket是否为空，为空则删除
                del self.count2bucket[key_bucket]

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.tail.pre == self.head:
            return ""
        return self.tail.pre.get_1st().get_key()

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.head.next == self.tail:
            return ""
        return self.head.next.get_1st().get_key()

if __name__ == "__main__":
    sol = None
    instruction_list = ["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]
    parameters_list = [[],["hello"],["hello"],[],[],["leet"],[],[]]

    for ind, ins in enumerate(instruction_list):
        if ins == "AllOne":
            sol = AllOne()
        if ins == "inc":
            sol.inc(parameters_list[ind][0])
        if ins == "dec":
            sol.dec(parameters_list[ind][0])
        if ins == "getMaxKey":
            print(sol.getMaxKey())
        if ins == "getMinKey":
            print(sol.getMinKey())