days_of_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
                 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def get_year_month():   # 월, 연도 입력
    str_year = input('연도를 입력하세요(-1 입력시 종료) > ')
    year = int(str_year)
    str_month = input('월을 입력하세요 > ')
    month = int(str_month)
    return year, month


def cal_leap_year(year):   # 윤년 구하기
    if year % 4 == 0:
        days_of_month[2] = 29
        if year % 100 == 0:
            days_of_month[2] = 28
            if year % 400 == 0:
                days_of_month[2] = 29


def get_start_day(year, month):    # 1일의 요일 받기
    year -= 1
    weekday = 1 + \
        ((year + year // 4 - year // 100 + year // 400) % 7)
    if month != 1:
        for i in range(1, month):
            weekday = (weekday + (days_of_month[i] % 7)) % 7
    return weekday


def get_schedule(year, month):
    schedule_list = []
    f = open('schedule.txt', 'r')
    while True:
        line = f.readline()
        if not line:
            break
        if year == int(line[0:4]) and month == int(line[5:7]):
            schedule_list.append(int(line[8:10]))
    f.close()
    return schedule_list


def print_calendar(year, month):    # 입력된 년,월로 달력 출력
    schedule_list = get_schedule(year, month)
    schedule_list.sort()
    print('\t\t< {}  {} >' .format(year, month))
    print('Mo\tTu\tWe\tTh\tFr\tSa\tSu')
    weekday = get_start_day(year, month)
    for i in range(weekday):
        print('\t', end='')
    cal_leap_year(year)
    for days in range(1, days_of_month[int(month)] + 1):
        for schedule_days in schedule_list:
            if days == schedule_days:
                print('.', end='')
                break
        if (days + weekday) % 7 == 0:
            print(days, '\t')
        else:
            print(days, end='\t')
    print()
