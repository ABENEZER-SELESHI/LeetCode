class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = []
        tens = []

        for bill in bills:
            if bill == 5:
                fives.append(bill)
            elif bill == 10:
                if not fives:
                    return False
                tens.append(bill)
                fives.pop()
            else:
                if (not tens and len(fives) < 3) or not fives:
                    return False
                if tens:
                    tens.pop()
                    fives.pop()
                else:
                    for i in range(3):
                        fives.pop()
        return True
