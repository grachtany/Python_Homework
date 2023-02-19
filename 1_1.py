n = int(input(f'Введите трехзначное число: '))
one = n//100
two = n % 100//10
three = n % 10
print(f'Сумма цифр трехзначного числа {n} -> {one + two + three}')
