class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        store = 0
        
        n = len(costs)
        al = n//2
        bl = n//2

        costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)

        for a, b in costs:
            if a <= b:
                if al > 0:
                    store += a
                    al -= 1
                else:
                    store += b
                    bl -= 1
            else:
                if bl > 0:
                    store += b
                    bl -= 1
                else:
                    store += a
                    al -= 1

        return store