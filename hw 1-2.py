# less 1

length, width = map(float, input('Введите стороны прямоугольника через пробел: ').split())
p = length + length + width + width
s = length * width
print(f'Пермиметр прямоугольник равен = {p} см, площадь равна = {s} кв. см')

# less 2

number = input('Введите число: ')
# number = 46275
if len(number) == 5:
    units = int(number[-1])
    dozens = int(number[-2])
    hundreds = int(number[-3])
    thousands = int(number[-4])
    doz_of_thous = int(number[-5])
    print((dozens ** units) * hundreds / (doz_of_thous - thousands))
else:
    print('Введите пятизначное число :(')

