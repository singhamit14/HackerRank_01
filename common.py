def squares(n):
    
    print('Generating squares from 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2

n = 10
print(squares(n))






















