'''
Необходимо написать консольное приложение, которое принимает аргументом римское число и возвращает сконвертированное
арабское число.
Бонусом может послужить конвертирование в обратном порядке (из арабских в римские).
Программа должна быть рабочей и не должна иметь сторонних библиотек, связанных с работой римских чисел. По возможности,
код должен сопровождаться разумными комментариями и прочими инструкциями.
'''
KORT_CORR = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),  # кортеж соответствующих арабских чисел римским
             (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
             (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


def arab_to_roman(number):
    if number <= 0:
        return ''
    answer = ''
    for arab, roman in KORT_CORR:
        while number >= arab:  # цикл обработки числа
            answer += roman  # дозапись в строку соответствующего римского символа арабского числа
            number -= arab  # вычитание обработанного числа
    return answer


def roman_to_arab(ent_num):
    ent_num = ent_num.upper()  # перевод строки в верхний регистр, на случай, если ввод был выполнен в нижнем регистре
    answer = 0
    for arab, roman in KORT_CORR:
        while ent_num.startswith(roman):
            answer += arab  # запись соответствующего арабского символа из кортежа
            ent_num = ent_num[len(roman):]  # запись в строку необработанных символов
    return answer


repeat = True
while repeat:
    if input('Please enter [1] if you want to translate ROMAN NUMBER TO ARABIC, '
             'or any other symbol to translate ARABIC NUMBER to ROMAN: ') == '1':
        roman = str(input('Please enter roman number: '))
        arab = roman_to_arab(roman)
        print(arab)
        if input('Do you want to translate more numbers? [y/n] : ') != 'y':
            repeat = False
    else:
        arab = int(input('Please enter arabic number: '))
        roman = arab_to_roman(arab)
        print(roman)
        if input('Do you want to translate more numbers? [y/n] : ') != 'y':
            repeat = False
