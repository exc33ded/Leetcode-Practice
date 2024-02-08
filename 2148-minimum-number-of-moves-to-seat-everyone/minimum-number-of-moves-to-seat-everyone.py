class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        sum_ = 0
        for x, y in zip(seats, students):
            sum_ += abs(x-y)

        return sum_