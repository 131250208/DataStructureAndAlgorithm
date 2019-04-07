class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        dir_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count_trans = 0
        res = []
        i, j = 0, -1
        num_total = len(matrix) * len(matrix[0])

        def legal(i, j):
            if 0 <= i <= len(matrix) - 1 and 0 <= j <= len(matrix[0]) - 1 and matrix[i][j] != "@":
                return True
            return False

        while True:
            direct = dir_list[count_trans % 4]
            while True:
                i += direct[0]
                j += direct[1]
                if legal(i, j):
                    num = matrix[i][j]
                    res.append(num)
                    matrix[i][j] = "@"
                    if len(res) == num_total:
                        return res
                else:
                    i -= direct[0]
                    j -= direct[1]
                    break
            count_trans += 1
        return res

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.spiralOrder(matrix))
