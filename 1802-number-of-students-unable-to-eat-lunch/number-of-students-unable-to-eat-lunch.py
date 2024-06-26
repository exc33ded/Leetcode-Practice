class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = 0
        while len(students) != 0:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                cnt = 0
            else:
                students.append(students.pop(0))
                cnt += 1

            if len(students) == cnt:
                return cnt
        return 0