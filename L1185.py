import calendar


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        da = (calendar.monthrange(year, month)[0] + day) % 7
        result = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return result[da]
