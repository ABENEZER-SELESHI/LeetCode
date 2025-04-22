class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def winner(left, right, turn):
            if left > right:
                return 0
            if turn:
                pl = nums[left] + winner(left + 1, right, False)
                pr = nums[right] + winner(left, right - 1, False)
                return max(pl, pr)
            else:
                pl = winner(left + 1, right, True)
                pr = winner(left, right - 1, True)
                return min(pl, pr)
        
        total = sum(nums)
        score1 = winner(0, len(nums) - 1, True)
        return score1 >= total - score1