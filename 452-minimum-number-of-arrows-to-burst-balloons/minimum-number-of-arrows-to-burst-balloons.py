class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key=lambda x: x[1])

        arrow = points[0][1]
        count = 1

        for left, right in points:
            if left > arrow:
                arrow = right
                count += 1
            elif right < arrow:
                arrow = right
        return count
