class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        digits = "123456789"
        low_len,high_len = len(str(low)),len(str(high))
        for i in range(low_len,high_len+1):
            start = 0
            while start <= len(digits)-i:
                num = int(digits[start:start+i])
                if low<=num<=high:
                    result.append(num)
                start+=1
        return result
        