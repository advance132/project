#计算指定的年月日是这一年的第几天。
def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year%4==0 and year%100!=0 or year%400==0
def main(year,month,date):
    '''
    计算某年某月某日是这一年的第几天
    :param year: 年份
    :param month: 月份
    :param date: 日期
    :return: 这一年的第几天
    '''
    day = 0
    if is_leap_year(year):
        Year = [31,29,31,30,31,30,31,31,30,31,30,31 ]
    else:
        Year = [31,28,31,30,31,30,31,31,30,31,30,31 ]
    if month < 1 or month > 12 or date < 1 or date > Year[month - 1]:
        return False
    for i in range(month-1):
        day += Year[i]
    day = day + date
    return day
if __name__ == '__main__':
    print(main(2020, 3, 1))
    print(main(2021, 6, 30))
    print(main(2021, 2, 29))