input_list = [1, 1, 2, 3, 4, 5, 5]
final_list = []
for i in input_list:
    if input_list.count(i) == 1:
        final_list.append(i)
print(f'{input_list} -> {final_list}')