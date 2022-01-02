from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        count = m * n
        path = []

        def is_valid(i, j):
            return 0 <= i <= m - 1 and 0 <= j <= n - 1 and matrix[i][j]

        i, j = 0, -1
        while count:
            if not is_valid(i + dirs[dir_idx % 4][0], j + dirs[dir_idx % 4][1]):
                dir_idx += 1

            i += dirs[dir_idx % 4][0]
            j += dirs[dir_idx % 4][1]
            path.append(matrix[i][j])
            matrix[i][j] = None
            count -= 1
        return path
