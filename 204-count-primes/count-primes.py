class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        is_prime = [True] * n
        is_prime[0],is_prime[1] = False,False
        i = 2
        while i**2 <= n:
            if is_prime[i]:
                d = i*i
                while d < n:
                    is_prime[d] = False
                    d+=i
            i+=1
        return sum(is_prime)
