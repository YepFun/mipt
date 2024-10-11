import re

def Ru(date):
    day = int(date[0]) * 10 + int(date[1])
    month = int(date[3]) * 10 + int(date[4])
    year = int(date[6]) * 1000 + int(date[7]) * 100 + int(date[8]) * 10 + int(date[9])
    return day, month, year

def US(date):
    day = int(date[5]) * 10 + int(date[6])
    month = int(date[8]) * 10 + int(date[9])
    year = int(date[0]) * 1000 + int(date[1]) * 100 + int(date[2]) * 10 + int(date[3])
    return day, month, year

def Jp(date):
    day = int(date[8]) * 10 + int(date[9])
    month = int(date[5]) * 10 + int(date[6])
    year = int(date[0]) * 1000 + int(date[1]) * 100 + int(date[2]) * 10 + int(date[3])
    return day, month, year

def IsValid(day, month, year):
    return 1 <= day <= 28 and 1 <= month <= 13 and 1900 < year < 2099

def DateFormat(date):
    if re.match(r'\d{2}[\s\-/.]\d{2}[\s\-/.]\d{4}', date):
        day, month, year = Ru(date)
        if IsValid(day, month, year):
            print("RU")
            return
        print("NOT VALID")
        return

    # Проверяем форматы для США и Японии
    if re.match(r'\d{4}[\s\-/.]\d{2}[\s\-/.]\d{2}', date):
        day_us, month_us, year_us = US(date)
        day_jp, month_jp, year_jp = Jp(date)
        valid = []
        if IsValid(day_jp, month_jp, year_jp):
            valid.append("JP")
        if IsValid(day_us, month_us, year_us):
            valid.append("US")
        if len(valid) > 0:
            print(" ".join(valid))
            return
    print("NOT VALID")

date = input()
DateFormat(date)
