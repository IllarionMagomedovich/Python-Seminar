
# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# 2 2
# 4

def sum_digit(a,b):
    if  a==0 or b==0:
        return ' '
    if b > 0:
        return (a+1, b-1)
    else:
         return (a-1,b+1)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
res = a + b
print(f'{sum_digit(a,b)}--> {res}')
    
