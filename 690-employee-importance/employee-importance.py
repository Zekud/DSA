"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {emp.id: emp for emp in employees}
        # print(emp_map.items())
        total = 0
        def dfs(id):
            nonlocal total
            employee= emp_map[id]
            total+=employee.importance
            for subordinate in employee.subordinates:
                dfs(subordinate)
        
        dfs(id)
        return total

        