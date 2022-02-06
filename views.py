"""
from decimal import Decimal, ROUND_UP


def deposit_calculation(period, amount, rate): #функция округляет до 2-го знакаб но в большую сторону
    depos_calc = []
    summa = amount
    for month in range(period):
        summa = summa*(1+(rate/12)/100)
        s = float(Decimal(summa).quantize(Decimal('.01'), rounding=ROUND_UP))
        depos_calc.append(s)
    return depos_calc
"""

import datetime
from dateutil.relativedelta import relativedelta
from flask import abort


def deposit_calculation(period, amount, rate): #список из значений по периодам
    if period > 60:
        return abort(400, 'Период превышает 60 месяцев')
    if period < 1:
        return abort(400, 'Период менее 1 месяца')
    if amount < 10000:
        return abort(400, 'Сумма вклада менее 10000')
    if amount > 3000000:
        return abort(400, 'Сумма вклада более 3000000')
    if rate > 8 or rate < 1:
        return abort(400, 'Ставка по вкладу некорректная')
    depos_calc = []
    summa = amount
    try:
        for month in range(period):
            summa = summa*(1+(rate/12)/100)
            s = ("%.2f" % round(summa, 2))
            depos_calc.append(float(s))
        return depos_calc
    except TypeError:
        return abort(400, 'Формат данных введен неверно, введите его в типе int или float')


def format_for_datetime(date): #возвращает кортеж для создания объекта datetime
    try:
        date = date.split('.')[::-1]
    except AttributeError:
        return abort(400, 'Формат даты введен неверно, введите его строкой')
    try:
        date = tuple(map(int, date))
        return(date)
    except ValueError:
        return abort(400, 'Формат даты введен неверно, введите в виде 31.01.2022')


def list_date(data, period):#возвращает список дат в заданном порядке и формате
    try:
        start_day = datetime.date(*data)
    except ValueError:
        return abort(400, 'Дата введена неверно, введите корректную дату')
    list_date = []
    try:
        for month in range(period):
            day = start_day + relativedelta(months=month)
            new = day.strftime("%d.%m.%Y")
            list_date.append(new)
        return list_date
    except TypeError:
        return abort(400, 'Период введен некорректно, введите его в формате int')


def dict_data_base(date, period, amount, rate):#возвращает словарь со значениями под нужный формат
    try:
        sum_deposit = deposit_calculation(period, amount, rate)
        format_dates = format_for_datetime(date)
        date_list = list_date(format_dates, period)
        dict_data = dict(zip(date_list, sum_deposit))
        return dict_data
    except TypeError:
        return abort(400, 'Формат вводных данных должен быть int')



""" #Проверка работоспособности
print(format_date('31.01.2021'))
print(list_date((2021, 1, 31), 3))
print(deposit_calculation(3, 10000, 6))

date = '31.01.2022'
period = 3
amount = 100000
rate = 6
print(dict_data_base(date, period, amount, rate))
"""


