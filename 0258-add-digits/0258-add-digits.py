class Solution(object):
    def addDigits(self, num):
        list1 = list(str(num))
        summ = 0
        for i in list1:
            summ += int(i)
        while len(str(summ)) > 1:
            listQ = list(str(summ))
            summ = 0
            for i in listQ:
                summ += int(i)
        return summ