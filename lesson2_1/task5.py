my_list = [8,7,5,3,3,2]
print(f'текущий рейтинг: {my_list}')
x = int(input('Введите число: '))
for i in range(len(my_list)):
    if x > my_list[i]:
        my_list.insert(i, x)
        break
    elif x <= my_list[-1]:
        my_list.append(x)
        break
print(f'Новый рейтинг: {my_list}')