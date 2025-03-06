class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        mx = max(max(heights), min(heights)*n)

        right = []
        result_right = [0]*n
        result_left = [0]*n
        for i in range(n):
            result_right[i] = n-1-i
            result_left[i] = n-1-i

        # left = 0
        # right = 0

        # forward
        for i, height in enumerate(heights):
            while right and heights[right[-1]] > height:
                index = right.pop()
                result_right[index] = i - index - 1
            right.append(i)
        
        # backward
        heights.reverse()
        # print(heights)
        left = []
        for i, height in enumerate(heights):
            while left and heights[left[-1]] > height:
                index = left.pop()
                result_left[index] = i - index - 1
            left.append(i)
        # left[::-1]
        result_left.reverse()

        # return result_left

        store = []
        for i in range(n):
            store.append(result_right[i] + result_left[i] + 1)
        res = []
        heights.reverse()
        for i in range(n):
            res.append(heights[i]*store[i])
        
        return max(res)
