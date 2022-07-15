#ye hai normal tareka

def even_generator():
    n = 0

    n += 2
    yield n

    n += 2
    yield n

    n += 2
    yield n

    n += 2
    yield n



numbers = even_generator()

print(next(numbers))
print(next(numbers))
print(next(numbers))






#ye hai mentos tareeka

def even_generator(max):
    
    n = 2

    while n <= max:
        yield n
        n += 2



numbers = even_generator(8)

print(next(numbers))
print(next(numbers))
print(next(numbers))








#ultra pro method

def generate_fibbo():
    n1 = 0
    n2 = 1

    while True:
        yield n1
        n1, n2 = n2, n1+n2


seq = generate_fibbo()

last = int(input('Enter the last value'))

for numbers in range(0,last):
    print(next(seq))
