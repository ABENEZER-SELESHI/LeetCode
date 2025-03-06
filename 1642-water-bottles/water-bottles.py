class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = 0
        f_bottles = numBottles
        e_bottles = 0
        while numBottles >= 0:

            # drinking
            drink += f_bottles
            e_bottles += f_bottles

            # exchange
            f_bottles = e_bottles // numExchange
            e_bottles = e_bottles % numExchange

            numBottles = f_bottles + e_bottles

            if f_bottles == 0 and numBottles % numExchange < numExchange:
                break
        
        return drink