class Solution:
    def validStrings(self, n: int) -> List[str]:
        self.res = []
        self.unique = set()

        def adjacent(store):
            if len(store) == n:
                if tuple(store) not in self.unique:
                    self.res.append("".join(store[:]))
                    self.unique.add(tuple(store[:]))
                return
            if store == []:
                adjacent(["1"])
                adjacent(["0"])
            else:
                if store[-1] == "1":
                    
                    # store.append("1")
                    adjacent(store+["1"])
                    
                    # store.pop()
                    # store.append("0")
                    adjacent(store+["0"])
                elif store[-1] == "0":

                    # store.append("1")
                    adjacent(store+["1"])
        adjacent([])
        return self.res
