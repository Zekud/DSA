class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def kth(n,k):
            if n==1:
                return 0
            prev = kth(n-1,math.ceil(k/2))
            if k%2 ==0:
                if prev == 1:
                    return 0
                else:
                    return 1
            else:
                return prev
        return kth(n,k)

