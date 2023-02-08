# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

print('Введите слово: ')
text = input().split()
res = {}

for char in text:
    if char in res:
        print(f'{char}_{res[char]}', end = ' ')
    else:
        print(f'{char}', end = ' ')
    res[char] = res.get(char, 0)+1    


