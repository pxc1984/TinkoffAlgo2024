def leap_year(i):
    if (i % 400 == 0) or (i % 4 == 0 and i % 100 != 0):
        return True
    return False


def count_leap_years(y1, y2):
    def f(y):
        return y // 4 - y // 100 + y // 400

    return f(y2) - f(y1)


def birthdays_count(d1, m1, y1, d2, m2, y2):
    if d1 == 29 and m1 == 2:  # костыль, обрабатывающий случай др у Васи 29 февраля как у Пети
        vs_birthdays = count_leap_years(y1, y2)
        if not (leap_year(y2) and (m2 > 2 or (m2 == 2 and d2 >= 29))):
            vs_birthdays -= 1
    else:
        vs_birthdays = y2 - y1 + 1
        if m2 < m1 or (m2 == m1 and d2 < d1):
            vs_birthdays -= 1

    pt_birthdays = count_leap_years(y1, y2)
    if (m2 < 2) or (m2 == 2 and d2 < 29):
        pt_birthdays -= 1
    return pt_birthdays, vs_birthdays


def birthdays_count2(d1, m1, y1, d2, m2, y2):
    if d1 == 29 and m1 == 2:
        #print("Special")
        pt_birthdays = count_leap_years(y1, y2)
        if m2 < m1 or (m2 == m1 and d2 <= d1):
            if pt_birthdays == 0:
                # pt_birthdays -= 1
                pass
            else:
                pt_birthdays += 1
        return pt_birthdays, pt_birthdays
    if m2 < m1 or (m2 == m1 and d2 < d1):
        #print("less")
        vs_birthdays =  y2 - y1
        pt_birthdays = count_leap_years(y1, y2) + 1
        if m2 < 2 or (m2 == 2 and d2 < 29):
            pt_birthdays -= 1
    else:
        vs_birthdays = y2 - y1 + 1
        pt_birthdays = count_leap_years(y1, y2) + 1
        if m2 < 2 or (m2 == 2 and d2 < 29):
            pt_birthdays -= 1
    return pt_birthdays, vs_birthdays


print(*birthdays_count2(*map(int, input().split('.')), *map(int, input().split('.'))))
