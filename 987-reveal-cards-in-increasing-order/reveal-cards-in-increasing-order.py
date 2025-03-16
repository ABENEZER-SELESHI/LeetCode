class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
    
        myque = deque()
        
        for card in reversed(deck):
            if myque:
                myque.appendleft(myque.pop())
            myque.appendleft(card)
        
        return list(myque)