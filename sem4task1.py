import math
def pi_on_given_accuraccy(d):
    my_string = str(d)
    my_length = len(my_string)
    if (my_length <= 5 and my_string[2] != '-') or (my_length == 6):
        pi = round(math.pi, my_length - 2)
        return(pi)  
    else:
        pi = round(math.pi, int(my_string[4]))
        return(pi)
d = float(input('Введите число заданной точности: '))
print(f'При d = {d}, π = {pi_on_given_accuraccy(d)}')