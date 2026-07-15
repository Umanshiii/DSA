'''
Given two dates within the same year, your task is to 
calculate the total number of days between them. 
For example, if the inputs are (Month: 1, Day: 15) and (Month: 3, Day: 10), 
we want to find the exact count of days that separate them.
'''

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def get_total_days(date):
            y, m, d = map(int, date.split('-'))
            total_days = (y - 1) * 365 + d
            for i in range(m - 1):
                total_days += monthDays[i]
            if m <= 2:
                y -= 1
            total_days += (y // 4) - (y // 100) + (y // 400)
            
            return total_days

        return abs(get_total_days(date1) - get_total_days(date2))