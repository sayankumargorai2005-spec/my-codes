class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # Number of rows
        m = len(matrix)

        # Number of columns
        n = len(matrix[0])

        # Boundaries
        top, bottom, left, right = 0, m - 1, 0, n - 1

        result = []

        while top <= bottom and left <= right:

            # Left to Right
            for i in range(left, right + 1):
                result.append(matrix[top][i])

            top += 1

            # Top to Bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])

            right -= 1

            # Right to Left
            if top <= bottom and left <= right:

                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])

                bottom -= 1

                # Bottom to Top
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])

                left += 1

        return result