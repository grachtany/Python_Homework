number = int(input('Введите номер билетика: '))
part_1 = number//1000
one = part_1//100
two = part_1 % 100//10
three = part_1 % 10
part_2 = number % 1000
four = part_2//100
five = part_2 % 100//10
six = part_2 % 10
if one + two + three == four + five + six:
    print('Билетик счастливый')
else:
    print('Билетик не счастливый')
