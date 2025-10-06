class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        memo = defaultdict(lambda:0)

        for i in range(len(arr)):
            val = arr[i] % k
            if val == 0:
                if memo[0] == 0:
                    memo[0] += 1
                else:
                    memo[0] -= 1
                continue
            if memo[k-val] == 0:
                memo[val] += 1
            else:
                memo[k-val] -= 1
                
        for k, v in memo.items():
            if v > 0:
                return False
        return True