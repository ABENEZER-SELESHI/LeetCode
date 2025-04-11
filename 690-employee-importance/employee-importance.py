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
        
        graph = defaultdict(list)

        # [val, sub1, sub2, ..., subn]

        for employee in employees:
            graph[employee.id].append(employee.importance)
            graph[employee.id].extend(employee.subordinates)
        
        def dfs(node):

            self.visited.add(node)

            self.count += graph[node][0]
            if len(graph[node]) > 1:
                for i in range(1, len(graph[node])):
                    num = graph[node][i]

                    if num not in self.visited:
                        dfs(num)
        self.count = 0
        self.visited = set()
        dfs(id)
        return self.count

        
