# Задача 2: 
# Найдите сумму цифр трехзначного числа.
# Примеры:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Введите трехзначное чсило: ')
n = int(input())

print ((n%10) + (n//10 % 10) + (n//100 % 10))