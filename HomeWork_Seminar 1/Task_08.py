# Задача 8: 
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k
# долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# Примечание: каждое считывание производится с новой строки

# 3 2 4 -> yes
# 3 2 1 -> no

print('Введите число: ')
m = int(input())
print('Введите число: ')
n = int(input())
print('Введите число: ')
k = int(input())

if k<m*n and k%m==0 or k%n==0:
   print('YES')
else:
    print('NO')

