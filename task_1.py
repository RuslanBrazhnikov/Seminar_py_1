num = int(input('Введите число: '))

if num > 5 and num < 8:
    print('Да')
elif num > 7:
    print('Число выше предела!')
elif num <= 0:
    print('Некорректное число!')
else:
    print('Нет')