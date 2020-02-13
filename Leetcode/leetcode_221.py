class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix:
            return 0
        max_len_side = max(max([int(_) for _ in matrix[0]]), max([int(_[0]) for _ in matrix]))
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = min(int(matrix[i - 1][j]), int(matrix[i][j - 1]), int(matrix[i - 1][j - 1])) + 1 if int(matrix[i][j]) == 1 else 0
                max_len_side = max(max_len_side, matrix[i][j])

        return max_len_side**2

if __name__ == "__main__":
    matrix = [[1, 0, 1, 0, 0],
              [1, 0, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 0, 0, 1, 0],]
    sol = Solution()
    print(sol.maximalSquare(matrix))
