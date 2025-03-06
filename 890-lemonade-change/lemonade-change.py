class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # l=r=0
        
        # for r in range(len(bills)):
        #     tot = 0
        #     if bills[r] == 5:
        #         continue
        #     check = False    
        #     while l < r:
        #         tot += bills[l]
        #         l+=1
        #         if tot == (bills[r]-5):
        #             check = True
        #             break
        #         elif tot >= (bills[r]-5):
        #             break
        #     if not check:
        #         return False
        # return True
        count = defaultdict(int)
        for n in bills:
            if n==5:
                count[5] +=1
            elif n==10:
                if 5 in count:
                    count[5]-=1
                    count[10]+=1
                    if count[5] == 0:
                        del count[5]
                else:
                    return False
            else:
                if 10 in count and 5 in count:
                        count[10]-=1
                        count[5]-=1
                        if count[5] == 0:
                            del count[5]
                        if count[10] == 0:
                            del count[10]
                elif 5 in count and count[5] >= 3:
                        count[5]-=3
                        if count[5] == 0:
                            del count[5]

                else:
                    return False
        return True





            



