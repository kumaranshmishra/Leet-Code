class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
          flag = 0 
          for i in range (len(hours)):
             if hours[i] >= target :
                 flag = flag+1

          return flag