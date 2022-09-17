n = int(input('Введите число: '))
def list_of_prime_factors(n):
    final_list = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            final_list.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        final_list.append(n)
    return(final_list)
print(f'{n} -> {list_of_prime_factors(n)}')
