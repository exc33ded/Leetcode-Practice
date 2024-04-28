class Solution:
    def numberOfRightTriangles(self, a: List[List[int]]) -> int:
        N = len(a)
        M = len(a[0])

        # Stores the count of 1s for
        # each row[] and column[]
        rows = [0] * N
        columns = [0] * M

        # Find the number of 1s in
        # each of the rows[0, N - 1]
        for i in range(N):
            for j in range(M):

                # Increment row[i]
                if (a[i][j] == 1):
                    rows[i] += 1

        # Find the number of 1s in
        # each of the columns[0, N - 1]
        for i in range(M):
            for j in range(N):

                # Increment columns[i]
                if (a[j][i] == 1):
                    columns[i] += 1

        # Stores the count of triangles
        answer = 0

        for i in range(N):
            for j in range(M):

                # If current cell has value 1
                if (a[i][j] == 1):

                    # Update the answer
                    answer += ((rows[i] - 1) *
                          (columns[j] - 1))

        # Return the count
        return answer