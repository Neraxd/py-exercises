# fib using generator


def fib_gen():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a,b = b , a+b
        yield b


fib = fib_gen()
for f in fib:
    print(f)
