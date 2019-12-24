n = input('Введите строку состоящую из слов разделенными пробелами: ')
n =(n.split())
x = 1
for el in n:
    print(x, str(el[:10]))
    x = x +1
