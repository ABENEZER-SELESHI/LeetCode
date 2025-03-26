class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        # muahhhahaahahaahhaaaaaa:)
        def parenthor(left, right, store):
            # if right < left:
            #     return
            if len(store) == 2*n:
                res.append(store[:])
                return
            if left == 0:
                parenthor(left, 0, store + ")"*right)
            elif left < right:
                parenthor(left, right-1, store + ")")
                # store.pop()
                parenthor(left-1, right, store + "(")
                
                
            else:
                parenthor(left-1, right, store + "(")
        
        parenthor(n, n, "")
        return res