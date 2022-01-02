import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.q = nums
        heapq.heapify(self.q)
        while len(self.q) > k:
            heapq.heappop(self.q)

    def add(self, val: int) -> int:
        if len(self.q) < self.k:
            heapq.heappush(self.q, val)
        elif val > self.q[0]:
            heapq.heapreplace(self.q, val)
        return self.q[0]