# Дан список чисел. 
# Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# list = [1, 1, 2, 0, -1, 3, 4, 4]
# unic = []
# count = 0

# for element in list:
#     if element not in unic:
#         unic.append(element)
# print(len(unic))

# print(len(set(list)))

list = list(map(int,input('Введите число ').split(' ')))
print(list)