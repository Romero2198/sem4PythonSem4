from random import randint
def new_list(k_1, my_list_1):
    while k_1 != 0:
        my_list_1.append(randint(0, 100))
        k_1 -= 1
k = int(input('Введите k: '))
my_list = []
k += 1
new_list(k, my_list)
result = ''
for i in range(len(my_list)):
    k -= 1
    if my_list[i] != 0:
        result += f'{my_list[i]} '
        if k == 0:
            result += '= 0'
        elif k == 1:
            result += f'* x + '
        else:
            result += f'* x ^ {k - 1} + '
if my_list[-1] == 0:
    result += '= 0'
print(result)
print(my_list)
with open('Text.txt', 'w') as file:
    file.write(result)