class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []

        def ip(address, ind, store):
            if len(store) == 4 and ind < len(address):
                return
            if ind >= len(address) and len(store) == 4:
                res.append(".".join(store[:]))
                return
            
            print(store)
            
            for i in range(ind+1, ind + 4):
                if i <= len(address):
                    temp = address[ind:i]
                    print(temp)
                    if 0 <= int(temp) <= 255:
                        if len(temp) == 1 or (len(temp) > 1 and temp[0] != "0"):
                            # print(temp)
                            ip(address, i, store + [temp])
        ip(s, 0, [])

        return res
