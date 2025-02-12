class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        count = 0
        for i in range(len(seats)):
            count+= abs(students[i]-seats[i])
        return count