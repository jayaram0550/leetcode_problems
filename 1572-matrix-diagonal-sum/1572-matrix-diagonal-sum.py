class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        d = 0
        e = 0
        r = len(mat)

        for i in range(r):
            for j in range(r):
                if i == j:
                    s += mat[i][j]
                if i + j == r - 1:
                    d += mat[i][j]
                if i == j and i + j == r - 1:
                    e = mat[i][j]

        return s + d - e
