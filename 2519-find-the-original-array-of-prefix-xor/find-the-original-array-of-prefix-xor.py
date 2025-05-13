class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        track = 0
        ans = [pref[0]]

        for i in range(1, len(pref)):
            track = pref[i]^pref[i-1]
            ans.append(track)
        
        return ans