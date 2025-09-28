# Transpose a Matrix

# Because it forces you to see how zip(*iterables) really works with unpacking.

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
# ]
# turn it into this:
# [(1, 4), (2, 5), (3, 6)]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

trasnposed = list(zip(*matrix))
print(trasnposed)
