x = list(input('введите данные'))
y = int(len(x)-1)
if (len(x)) %2 != 0:
    z = x.pop(y)
    for i in range(0, len(x), 2):
        x[i], x[i+1] = x[i+1], x[i]
    x.append(z)
    print(x)
else:
    for i in range(0, len(x), 2):
         x[i], x[i + 1] = x[i + 1], x[i]
    print(x)