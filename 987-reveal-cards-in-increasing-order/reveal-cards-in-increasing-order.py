class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque()
        for i in range(len(deck)-1,-1,-1):
            if len(queue)>=2:
                last=queue.pop()
                queue.appendleft(last)
                queue.appendleft(deck[i])
            else:
                queue.appendleft(deck[i])
        return list(queue)

        