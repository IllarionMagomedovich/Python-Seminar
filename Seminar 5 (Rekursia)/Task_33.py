# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменят оценки Василия, но наоборот: все максимальные - на минимальные.

# input: 5 -> 1 3 3 3 4

# output: 1 3 3 3 1

n = int(input('Введите кол-во оценок: '))

qwerty = [0] * n

for i in range (n):
    qwerty[i] = int(input('ВВедите оценки: '))
max_num=max(qwerty)
min_num=min(qwerty)

for i in range(n):
    if qwerty[i]==max_num:
        qwerty[i]=min_num
print(qwerty)