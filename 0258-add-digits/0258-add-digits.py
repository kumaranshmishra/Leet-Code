class Solution(object):
    def addDigits(self, num):
         sum = 0
         if num<10 :
             return num
         while num>0:
              rem = num%10
              sum = rem + sum
              num = num//10
         if sum >=10 :
             return  self.addDigits(sum)
         return sum         


        