class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        if maxDoubles== 0:
            return target-1
        while target != 1:
            
            if maxDoubles == 0:
                moves += (target-1)
                break
            if maxDoubles > 0 and target%2 ==0:
                target //= 2
                moves+=1
                maxDoubles-=1
            else:
                target-=1
                moves+=1
            print(target, moves)
        return moves