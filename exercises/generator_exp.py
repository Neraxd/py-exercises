def is_prime(n):
    if n < 2:  # 0 and 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # check up to √n
        if n % i == 0:
            return False
    return True


gen = (i**2 for i in range(1, 51) if is_prime(i))

# next() starts where it left off
print(next(gen))
print(next(gen))

for g in gen:
    print(g)
