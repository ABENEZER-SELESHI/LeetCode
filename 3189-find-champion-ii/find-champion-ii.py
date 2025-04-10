class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        store = [i for i in range(n)]
        track = set(store)
        # return track
        # return store
        
        for w, l in edges:
            if l in track:
                track.remove(l)
        
        store = list(track)
        if len(store) != 1:
            return -1
        else:
            return store[0]
