m = int(input('введите номер месяца в году: '))
if 0 < m <= 12:
    y_dict = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
    for s, ms in y_dict.items():
        if m in ms:
            print(s)
else:
    print('вы ошиблись')
