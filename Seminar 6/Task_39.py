# Даны два массива чисел. Требуется вывести те элементы первого масива(в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число  N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива

# Ввод:
# 7
# 3 1 3 4 2 4 12

# 6
# 4 15 43 1 15 1

# Вывод:
# 3 3 2 12

print('Введите число n: ')
n = int(input())

list1 = list(map(int, input().split()))
print('Введите число m: ') 
m = int(input())
list2 = list(map(int, input().split()))

# for i in range(n):
#     flag = False
#     for j in range(m):
#        if list1[i]==list2[j]:
#           flag = True
#           break
#     if not flag:
#       print(list1[i], end =' ')

s1 = set(list2)
for i in range(n):
    if list1[i] not in s1:
       print(list1[i], end =' ')

